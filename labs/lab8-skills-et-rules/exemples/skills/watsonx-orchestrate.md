---
name: watsonx-orchestrate
description: >-
  Build, import, test, debug, and publish IBM watsonx Orchestrate agents, tools,
  flows, toolkits (MCP), connections, models, and knowledge bases using the
  watsonx Orchestrate Agent Development Kit (ADK) and the `orchestrate` CLI.
  Use this whenever the user mentions watsonx Orchestrate, wxO, the orchestrate
  CLI, the ADK, `ibm-watsonx-orchestrate`, native/external/assistant agents,
  agent YAML, the `@tool` / `@flow` decorators, the Developer Edition, or wants
  to create / import / chat-test / deploy a wxO agent or tool. Also covers
  embedding/consuming a deployed agent from a custom application via the wxO
  runtime REST API (`/chat/completions`, `/orchestrate/runs`, streaming) — as
  opposed to the drop-in embedded web-chat widget.
metadata:
  enabled: true
---

# IBM watsonx Orchestrate (wxO) — Build · Test · Debug · Publish

Authoritative, end-to-end guide for delivering production agents on IBM watsonx
Orchestrate with the Agent Development Kit (ADK). It is grounded in the real ADK
source and CLI (`ibm-watsonx-orchestrate`), not guesswork.

> **Golden rule:** the ADK changes fast. The CLI specifics here were verified
> against **`ibm-watsonx-orchestrate` 2.10.0**. When a command, flag, or YAML
> field is uncertain — or you're on a different version — **verify against the
> live tool** with `orchestrate <group> --help` and
> `orchestrate <group> <cmd> --help` before running it. Treat third-party blog
> syntax as approximate; trust `--help` and this skill's references. Check your
> version with `orchestrate --version` / `pip show ibm-watsonx-orchestrate`.

---

## 1. Mental model — what you are building

watsonx Orchestrate runs **agents** that route user requests to **tools**,
**collaborator agents**, and **knowledge bases**, powered by an **LLM**.

| Resource | What it is | Defined as |
|----------|------------|------------|
| **Agent** | An LLM-driven assistant. Kinds: `native` (built here), `external` (A2A / external chat), `assistant` (watsonx Assistant) | YAML (`kind: native`) or Python `Agent` |
| **Tool** | A capability the agent can call | Python `@tool`, OpenAPI spec, Flow, or Langflow |
| **Flow** | A multi-step orchestrated workflow exposed as a tool | Python `@flow` (`build_<name>(aflow: Flow) -> Flow`) |
| **Toolkit** | A bundle of tools from an **MCP server** | `orchestrate toolkits add -k mcp …` |
| **Connection** | Stored credentials/config for an external service | YAML (`kind: connection`) + `connections` CLI |
| **Model** | An LLM made available to agents (e.g. watsonx.ai, Groq) | YAML (`kind: model`) via the AI Gateway |
| **Knowledge base** | Documents for RAG/grounding | YAML (`kind: knowledge_base`) |

The two surfaces you work through:

- **The `orchestrate` CLI** — manages every resource in the *active environment*.
- **The Developer Edition** — a full local wxO that runs on Docker (`orchestrate server start`) so you can iterate before touching production.

---

## 2. Prerequisites

- **Python 3.11–3.13** (`<3.14`). Use the highest installed version in that range —
  **not** a bare `python3`, which may be the system 3.9 and will fail the ADK install.
- The CLI entrypoint is `orchestrate`. Confirm: `orchestrate --version` and `orchestrate --help`.
- Network access to your wxO instance (SaaS or on-prem) — or Docker for the local Developer Edition.
- **Never** add `ibm-watsonx-orchestrate` itself to a tool's `requirements.txt` — the runtime provides it.

**Bootstrap an isolated environment + CLI** (idempotent — reuse an existing venv if present):
```bash
# 1) Isolated Python env (reuse venv/ or .venv/ if it already exists)
for PY in python3.13 python3.12 python3.11; do command -v "$PY" >/dev/null && break; done
[ -d venv ] || [ -d .venv ] || "$PY" -m venv venv          # ADK needs Python 3.11–3.13
source venv/bin/activate 2>/dev/null || source .venv/bin/activate

# 2) Install the CLI if missing. Pinned to the version this skill is verified against;
#    drop the pin for the latest, then re-check `orchestrate <cmd> --help`.
orchestrate --version 2>/dev/null || pip install --upgrade "ibm-watsonx-orchestrate==2.10.0"
```
> Each new shell needs `source …/activate` (or call the venv's binaries directly).

Everything below works against **whatever environment is active**. The same
agent/tool artifacts deploy unchanged to local, SaaS, or on-prem — only the
environment you activate and the connection credentials differ.

---

## 2a. Connect to your environment (do this first)

`orchestrate` runs every command against the **active environment**. Pick one of
three targets; **SaaS and on-prem are the production paths**, local is optional.

### SaaS (IBM Cloud) — verified working flow
Use the **API service URL** (the one containing `/instances/<id>`), not the
console URL, and your **IBM Cloud API key**.

```bash
orchestrate env add -n my-saas \
  -u https://api.<region>.watson-orchestrate.cloud.ibm.com/instances/<INSTANCE_ID>
orchestrate env activate my-saas --api-key "$IBM_CLOUD_API_KEY"
orchestrate agents list          # confirm you're connected
```
Auth type is auto-inferred (typically `ibm_iam` for IBM Cloud SaaS). If inference
is wrong, set it explicitly on `env add` with `--type [ibm_iam|mcsp|mcsp_v1|mcsp_v2|cpd]`.

### On-prem (Cloud Pak for Data / CPD)
```bash
orchestrate env add -n my-onprem -u https://<cpd-host>/orchestrate --type cpd \
  [--insecure | --verify /path/to/ca.crt]      # for self-signed / private CAs
# Authenticate with an API key OR username+password (not both):
orchestrate env activate my-onprem --api-key "$CPD_API_KEY"
orchestrate env activate my-onprem -u "$CPD_USER" -p "$CPD_PASSWORD"
```

### Local Developer Edition (optional — offline iteration)
A full local wxO on Docker (Rancher/Colima): 16 GB RAM / 8 cores / 25 GB disk
(≥19 GB if Document Processing `-d`). Needs an entitlement key in `.env`.
```bash
orchestrate server start -e .env --accept-terms-and-conditions
orchestrate env activate local
orchestrate chat start            # local-only chat UI
```

### Environment hygiene
```bash
orchestrate env list                 # the active one is starred; that's where imports land
orchestrate env activate <name>      # switch targets
orchestrate env remove --name <name>
```
> **Always confirm the active env before importing** — the #1 cause of confusion.
> Keep secrets in a gitignored `.env` and pass via `"$VAR"` so keys stay out of
> shell history. Treat the IBM Cloud API key like a password; rotate if exposed.

See **[references/cli-reference.md](references/cli-reference.md)** for the full
command catalog. Need example projects? The public ADK repo's `examples/`
directory and the official docs are the canonical source — see §10.

---

## 3. The canonical lifecycle

Follow this order. Dependencies must exist *before* the thing that references them.

```
scaffold project → write tools (+connections/models/KB) → write agent YAML
   → import connections → import models → import KB → import tools/toolkits
   → import agent → chat-test → debug → (activate remote env) → re-import → deploy
```

### 3.1 Scaffold

```
my_agent/
├── README.md
├── agents/            my_agent.yaml
├── tools/             *.py  (one @flow per file; @tool can be grouped)
├── connections/       *.yaml (kind: connection)
├── knowledge_base/    *.yaml + source docs
├── models/            *.yaml (kind: model) — only if adding a custom model
├── import-all.sh      orchestrate ... import commands, dependency-ordered
└── .env               secrets (gitignored)
```

### 3.2 Write a Python tool

```python
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

@tool(permission=ToolPermission.READ_ONLY)   # or READ_WRITE
def get_weather(city: str) -> dict:
    """
    Get the current weather for a city.

    Args:
        city (str): Name of the city to look up.
    Returns:
        dict: Weather data keyed by metric.
    """
    return {"city": city, "temp_c": 21}
```

Decorator rules and docstring grammar are strict — getting them wrong is the
most common import failure. See §5 and
**[references/agents-tools-schemas.md](references/agents-tools-schemas.md)**.

### 3.3 Write the agent YAML

```yaml
spec_version: v1
kind: native
name: weather_agent
description: Returns weather information for a location.
instructions: >
  You are a helpful weather assistant. When the user asks about weather,
  call the get_weather tool with the city name and present the result clearly.
llm: watsonx/meta-llama/llama-3-3-70b-instruct   # example only — pick one that EXISTS in `orchestrate models list` (§4)
style: default                                    # default | react | planner
tools:
  - get_weather
starter_prompts:
  is_default_prompts: false
  prompts:
    - id: default0
      title: Check weather
      prompt: What's the weather in Boston?
      state: active
welcome_content:
  is_default_message: false
  welcome_message: Welcome to the Weather Agent
  description: Ask me about the weather in any city.
```

Required fields: `spec_version`, `kind`, `name`, `description`. Strongly
recommended: `instructions`, `llm`, `style`, `tools`, plus `starter_prompts` /
`welcome_content` for UX. Full field reference (collaborators, knowledge_base,
guidelines, structured_output, chat_with_docs, voice, channels) is in
**[references/agents-tools-schemas.md](references/agents-tools-schemas.md)**.

### 3.4 Import (dependency-ordered)

```bash
orchestrate env activate local

# 1) connections first (tools/agents reference them)
orchestrate connections import -f connections/my_api.yaml

# 2) custom models (if any)
orchestrate models import -f models/granite.yaml --app-id watsonx_credentials

# 3) knowledge bases
orchestrate knowledge-bases import -f knowledge_base/kb.yaml

# 4) tools — link credentials with --app-id; python tools take -r
orchestrate tools import -k python -f tools/weather.py -r tools/requirements.txt
orchestrate tools import -k python -f tools/api_tool.py --app-id my_api

# 4b) MCP toolkits — group is `toolkits` (plural). `add` for inline config,
#     `import` for a pre-written MCP spec file. (see references/mcp-toolkits.md)
orchestrate toolkits add -k mcp -n my_toolkit --description "My MCP tools" \
  --package-root ./mcp_server --language node \
  --command '["node","dist/index.js","--transport","stdio"]' --tools "*"

# 5) the agent last
orchestrate agents import -f agents/weather_agent.yaml
```

`tools import -k` accepts `python | openapi | flow | langflow`. Use `--safe` on
`tools`/`agents`/`knowledge-bases` import to be prompted before overwriting an
existing resource.

### 3.5 Test

```bash
orchestrate agents list                                 # confirm it imported; see real `name`s
orchestrate agents list -v                              # full JSON incl. ids
orchestrate chat ask -n weather_agent "Weather in Paris?" -r   # non-interactive, -r shows reasoning
```
- **Reference agents/tools by their `name` (snake_case), never the display name.**
  e.g. an agent shown as "FM - Aegis" may have `name: FM_3009a0` — `-n "FM - Aegis"`
  will fail. Find the real `name` with `agents list -v`, or export it:
  `orchestrate agents export -n <name> --kind native -o agent.yaml --agent-only`.
- **Local Developer Edition:** `orchestrate chat start` opens the local chat UI.
- **SaaS / on-prem:** test in the wxO **web console** (Chat / Preview), or
  scriptably with `orchestrate chat ask` against the active remote env.
- MCP-toolkit tools appear namespaced in listings as `toolkit_name:tool_name`.

### 3.6 Verify before handover (post-deploy gate)

**Deployed ≠ verified.** Never report an agent as "done" or "ready for handover"
until it has been tested — or the human explicitly declined. After deploy, **ask
first**, then prove it works:

> "`<agent>` is deployed to `<env>`. Want me to smoke-test it before handover? I'll
> run 1 single-turn + 1 multi-turn test against `<env>` — this sends real prompts
> and may invoke its tools, so I'll keep to **read-only** prompts." — Yes / No

If yes, derive the tests from the agent's own spec (`description`, `instructions`,
`tools`, and especially `starter_prompts` — those *are* example user prompts):

```bash
# Test 1 — single-turn (read-safe prompt; -r surfaces the reasoning / tool routing)
orchestrate chat ask -n <agent> "<derived prompt>" -r
```
**Test 2 — multi-turn (context retention).** Verified on ADK 2.10.0: the `chat ask`
**CLI cannot do scripted multi-turn** — it neither accepts a client-supplied
thread id nor surfaces the auto-created one. Two working paths:
- **Scripted (recommended):** drive the SDK `RunClient` — `create_run(msg, agent_id)`
  → capture `thread_id` → `create_run(msg2, agent_id, thread_id=…)` →
  `get_run_status(run_id)`; the reply text is at
  `result.data.message.content[0].text`. (Full snippet in the reference.)
- **Interactive:** the local chat UI (`orchestrate chat start`) or the SaaS/on-prem web console.

Make the follow-up **context-dependent** (e.g. *"which movie was it written for?"* —
"it" only resolvable from turn 1).

**Pass = behavior, not exact text** (LLMs are non-deterministic): no error,
on-topic, the **expected tool was called** (visible via `-r`; `-l` for custom
agents), and the multi-turn follow-up **uses prior context**. Then emit a short
`TEST_REPORT.md` (prompts, response excerpts, tool-call evidence, env, timestamp,
pass/fail) and **report status honestly**: "deployed and tested (2/2)", "deployed;
test 2 failed — …", or "deployed; not tested at your request".

**Safety:** keep tests **read-only by default** — if the agent has `READ_WRITE`
tools, do not craft prompts that trigger writes unless the human opts in. Full
recipe + report template: **[references/testing-debugging.md](references/testing-debugging.md)**.

### 3.7 Debug → Publish

Debugging in §6; promoting to a production instance in §7. **Run the §3.6 gate (or
record that the human declined) before §7 handover.**

---

## 4. Models / LLMs

- List what the active environment offers: `orchestrate models list`.
- Reference models in agent YAML by their full id, e.g.
  `watsonx/meta-llama/llama-3-3-70b-instruct`, `watsonx/ibm/granite-3-3-8b-instruct`,
  or a gateway provider like `groq/openai/gpt-oss-120b`.
- The `experimental_customer_care` agent style expects `groq/openai/gpt-oss-120b`.
- To add your own watsonx.ai model you create a `watsonx_credentials` connection,
  then a `kind: model` YAML, then `orchestrate models import`. Full walkthrough
  (provider schema, space/project/deployment, CPD on-prem) is in
  **[references/connections-models-kb.md](references/connections-models-kb.md)**.

---

## 5. Critical constraints (these cause silent failures — internalize them)

**Python tools**
- ✅ Every callable that becomes a tool **must** be decorated with `@tool`.
- ✅ Use **Google-style docstrings**: a summary, then `Args:` (each as
  `name (Type): desc`), then `Returns:` (`Type: desc`). **No blank line between
  the `Args:` and `Returns:` blocks** — extra blanks break the parser.
- ✅ Every parameter and the return value **must have type hints**, matching the docstring.
- ✅ Each tool file must be **self-contained**: only stdlib, common third-party
  (`requests`, `pydantic`, …), and `ibm_watsonx_orchestrate` imports. **No
  cross-file local imports** (`from .utils import x` / `from tools.shared import y`).
- ✅ Credentials are **never** function parameters. Declare `expected_credentials=[…]`
  on `@tool` and fetch at runtime via `ibm_watsonx_orchestrate.run.connections`.
- ✅ Define Pydantic models as explicit classes — never `type(...)` dynamic creation.

**Flows**
- ✅ Signature is exactly `def build_<flow_name>(aflow: Flow) -> Flow:` — param
  named `aflow`, returns the flow, function name starts with `build_`.
- ✅ One flow per file. Wire with `aflow.sequence(START, …, END)` / `aflow.edge(...)`.
- ✅ `map_output` / `map_input` expressions are **single-line** — no function defs/calls.
- ✅ `aflow.prompt(...)` requires a `system_prompt`.

**Agent YAML**
- ✅ `spec_version: v1` and `kind: native` are mandatory — omitting them fails import.
- ✅ `tools`/`collaborators`/`knowledge_base` list resources **by name**; the
  referenced resources must already be imported.
- ✅ `toolkits` are only valid for `experimental_customer_care` style (and the
  schedulable-agent exception).

**Connections YAML**
- ✅ `kind: connection` (singular). Inside `environments.<env>` use
  `security_scheme:` (not `kind:`). At minimum a `draft` environment.
- ✅ OAuth2 needs `auth_type: oauth2_auth_code` (not `authorization_code`).
- ✅ YAML defines *structure*; real secrets are set with
  `orchestrate connections set-credentials`. Never hardcode secrets.

---

## 6. Debugging playbook

| Symptom | Likely cause → fix |
|---------|--------------------|
| `agents import` fails on required field | Missing `spec_version`/`kind`/`name`/`description`, or a referenced tool/KB not imported yet. Import dependencies first. |
| Tool imports but agent never calls it | Vague tool `description`/docstring, or instructions don't mention it. Make the docstring action-oriented; name the tool in `instructions`. |
| Type-hint / docstring parser warnings | Missing type hints or a blank line between `Args:` and `Returns:`. Fix the Google-style docstring (§5). |
| "name cannot contain spaces" | Tool/toolkit/agent `name` must be snake_case, no spaces. |
| Missing dependency at tool runtime | Add it to the tool's `requirements.txt` and re-import with `-r` (never add `ibm-watsonx-orchestrate`). |
| 401/403 on a tool call | Connection not configured/credentialed, or wrong `app_id`. `orchestrate connections list`; re-run `set-credentials`. |
| Works locally, missing in prod | Wrong active env. `orchestrate env list` → `orchestrate env activate <remote>`, then re-import. |
| `No agents with the name 'X' found` | You used the display name. Use the snake_case `name` from `orchestrate agents list -v` (display "FM - Aegis" → `name: FM_3009a0`). |
| Need to see the agent's reasoning | `orchestrate chat ask -n <agent> "…" -r` (`-r` = reasoning, `-l` = capture logs for custom agents). |
| Inspect server | `orchestrate server logs`; `orchestrate server reset` to wipe state; `orchestrate server stop`. |

Iterate fast: edit → re-`import` (overwrites by name) → re-test in chat. Use
`orchestrate agents export -n <name> --kind native -o agent.yaml --agent-only` to
snapshot a working definition into Git, and `--safe` on imports to avoid clobbering.

More: **[references/testing-debugging.md](references/testing-debugging.md)**.

---

## 7. Publishing to production

There is **no `publish` verb** — publishing = activating the target environment
(SaaS or on-prem, see §2a), re-importing the artifacts there, and deploying.

> **Never hand over an untested agent.** Run the §3.6 verification gate after
> deploy (or record that the human declined). "Deployed" is a fact about the
> platform; "verified" is a fact about behavior — only the latter is handover-ready.

```bash
# 1) Activate the target env (registered once per §2a)
orchestrate env activate prod         # SaaS or on-prem

# 2) Re-import the same artifacts (connections → models → KB → tools → agent),
#    setting that env's credentials: orchestrate connections set-credentials ...
./import-all.sh

# 3) Deploy / retire an agent
orchestrate agents deploy   -n weather_agent
orchestrate agents undeploy -n weather_agent
```

Keep **one** set of YAML/Python artifacts; only connection **credentials** and
model `provider_config` differ per environment. Version the artifacts in Git and
treat `import-all.sh` as the source of truth for promotion across dev → SaaS/on-prem.
`orchestrate channels` exposes a deployed agent on channels such as embedded web chat.

---

## 8. Embedding agents in your application (runtime REST API)

This is for **consuming a deployed agent from your own app** — a web/mobile
backend, service, IDE, or another agent owns the UX and calls wxO like any backend
service. It is **distinct from the embedded web-chat widget** (that's a *channel*,
§7 / `orchestrate channels`, a drop-in UI you don't code against).

wxO exposes a runtime REST API under `<service-url>/api/v1`, bearer-token auth:

- **`/orchestrate/{agent_id}/chat/completions`** — OpenAI-compatible; drop-in for
  anything that already speaks OpenAI Chat Completions. Reply at
  `choices[0].message.content`.
- **`/orchestrate/runs`** (+ `GET /orchestrate/runs/{run_id}`) and
  **`/orchestrate/runs/stream`** — richer/async: tool-step outputs, decoding params
  (greedy / `temperature: 0`), guardrails, usage. Reply at
  `result.data.message.content[0].text`.
- **`/completions`**, **`/completions/chat`** — raw Gateway model, no agent/tools.

Both agent families return a **`thread_id`** — send it back to continue a
conversation (multi-turn memory). The Python SDK `RunClient` (used by the §3.6
verification gate) is just a typed wrapper over `/orchestrate/runs`; **Python apps
use `RunClient`, non-Python apps call the HTTP endpoints directly.**

**Rule of thumb:** `chat/completions` for portability, `orchestrate/runs` for
fidelity. **Never expose the bearer token to a browser** — proxy through your
backend, which holds the token and persists `thread_id` per user session.

Full endpoint shapes, auth (local `credentials.yaml` vs SaaS IAM token), base-URL
per environment, streaming event sequences, and the app-backend proxy pattern are
in **[references/runtime-api-embedding.md](references/runtime-api-embedding.md)**.

---

## 9. Working alongside the MCP servers (optional accelerator)

IBM ships two MCP servers that an AI coding assistant can use to author wxO
solutions without memorizing docs or CLI flags:

- **`wxo-docs`** (remote): `SearchIbmWatsonxOrchestrateAdk` for live ADK docs.
- **`orchestrate-adk`** (local): `list_agents`, `list_tools`, `list_toolkits`,
  `list_connections`, `list_models`, `export_agent`, `get_tool_template`,
  `check_version`, etc. — read state from the active environment.

If these MCP tools are available in your session, prefer them for
**discovery** (find existing tools/agents to reuse, fetch the current schema)
and **doc lookup**, then use the `orchestrate` CLI for the actual
import/test/deploy. Config snippets and the full tool list are in
**[references/mcp-toolkits.md](references/mcp-toolkits.md)**.

---

## 10. References (load on demand)

| File | Contents |
|------|----------|
| [references/cli-reference.md](references/cli-reference.md) | Every `orchestrate` group, subcommand, and flag |
| [references/agents-tools-schemas.md](references/agents-tools-schemas.md) | Agent YAML schema (native/external/assistant), `@tool`/`@flow` decorators, flow nodes, doc-processing |
| [references/connections-models-kb.md](references/connections-models-kb.md) | Connection auth schemes, watsonx.ai AI Gateway, KB providers (Milvus/AstraDB/Elasticsearch) & custom RAG tools |
| [references/mcp-toolkits.md](references/mcp-toolkits.md) | Importing MCP servers as toolkits; building MCP servers for tools; the wxO MCP servers |
| [references/runtime-api-embedding.md](references/runtime-api-embedding.md) | Consuming a deployed agent from your app via the runtime REST API (`/chat/completions`, `/orchestrate/runs`, streaming, model-only completions); auth, base URLs, `thread_id` multi-turn, app-backend proxy pattern |
| [references/testing-debugging.md](references/testing-debugging.md) | Post-deploy verification gate (test before handover) + report template, evaluations, programmatic flow testing, failure-mode table |

### Canonical external resources (you have internet access — use them)
- **ADK docs:** https://developer.watson-orchestrate.ibm.com (setup, agent/tool/flow guides, YAML specs)
- **Example projects:** https://github.com/IBM/ibm-watsonx-orchestrate-adk → `examples/` (agent_builder, flow_builder, evaluations, channel-integrations, voice, plugins)
- **SDK source (ground truth for schemas):** same repo → `src/ibm_watsonx_orchestrate/`
- **Live docs MCP server** (optional): `wxo-docs` exposes `SearchIbmWatsonxOrchestrateAdk` — see [references/mcp-toolkits.md](references/mcp-toolkits.md).

When you need a pattern this skill doesn't spell out, fetch a matching example
from the public `examples/` directory rather than inventing one.

**Always prefer live `orchestrate ... --help` over memory when a flag is in doubt.**
This skill's CLI specifics were verified against `ibm-watsonx-orchestrate` 2.10.0
and a live IBM Cloud SaaS instance.
