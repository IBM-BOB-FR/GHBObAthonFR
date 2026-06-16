# 📚 Exemples de Skills et Rules

Ce dossier contient des exemples concrets de Skills et Rules pour vous aider à démarrer.

---

## 📁 Structure

```
exemples/
├── skills/          # Exemples de fichiers skills (YAML)
│   ├── python-best-practices.yaml
│   └── fastapi-development.yaml
└── rules/           # Exemples de fichiers rules (Markdown)
    ├── projet-api-exemple.md
    └── projet-frontend-exemple.md
```

---

## 🧠 Skills (YAML)

Les **skills** sont des fichiers de configuration YAML qui définissent des comportements techniques.

### Exemples Fournis

#### 1. `python-best-practices.yaml`

Skill YAML complet pour le développement Python avec :
- Configuration des outils (Black, Ruff, mypy, pytest)
- Standards de style (PEP 8, docstrings Google)
- Conventions de nommage
- Bonnes pratiques
- Patterns recommandés
- Ce qu'il faut éviter

**Utilisation** :
```bash
# Copier dans votre projet
cp exemples/skills/python-best-practices.yaml .bob/skills/

# Demander à Bob
"Crée une fonction calculate_total() en respectant nos standards Python"
```

#### 2. `fastapi-development.yaml`

Skill YAML pour le développement d'API REST avec FastAPI :
- Architecture en couches
- Validation avec Pydantic
- Gestion des erreurs
- Authentification JWT
- Dependency Injection
- Documentation OpenAPI
- Performance (async/await)
- Tests

**Utilisation** :
```bash
# Copier dans votre projet
cp exemples/skills/fastapi-development.yaml .bob/skills/

# Demander à Bob
"Crée une API REST pour gérer des utilisateurs en suivant nos standards FastAPI"
```

#### 3. `watsonx-orchestrate.md`

Skill Markdown complet (486 lignes) pour IBM watsonx Orchestrate :
- Guide end-to-end pour l'Agent Development Kit (ADK)
- CLI `orchestrate` : agents, tools, flows, toolkits (MCP)
- Lifecycle complet : build → test → debug → publish
- Connexions, modèles, knowledge bases
- Runtime REST API pour embedding d'agents
- Métadonnées professionnelles (name, description, metadata)

**Utilisation** :
```bash
# Copier dans votre projet
cp exemples/skills/watsonx-orchestrate.md .bob/skills/

# Demander à Bob
"Crée un agent watsonx Orchestrate avec un tool Python en suivant le skill"
```

#### 4. `ibm-watsonx-ai.md`

Skill Markdown (370 lignes) pour IBM watsonx.ai :
- SDK Python `ibm-watsonx-ai` complet
- Foundation models : inference, chat, streaming
- Embeddings et RAG
- Tuning (prompt tuning, fine-tuning)
- Déploiement et scoring de modèles
- REST API (`/ml/v1/*` et `/ml/v4/*`)

**Utilisation** :
```bash
# Copier dans votre projet
cp exemples/skills/ibm-watsonx-ai.md .bob/skills/

# Demander à Bob
"Crée un script d'inference avec watsonx.ai en suivant le skill"
```

---

## 📏 Rules (Markdown)

Les **rules** sont des fichiers Markdown qui contiennent des instructions en langage naturel.

### Exemples Fournis

#### 1. `projet-api-exemple.md`

Rules complètes pour un projet d'API de bibliothèque :
- Vue d'ensemble du projet
- Stack technique (FastAPI, PostgreSQL, Redis)
- Architecture en couches
- Conventions de code
- Sécurité (JWT, validation)
- Base de données (migrations, requêtes)
- Performance (caching, async)
- Logging
- Ce qu'il faut éviter
- Checklist avant commit

**Utilisation** :
```bash
# Copier et adapter pour votre projet
cp exemples/rules/projet-api-exemple.md .bob/rules.md

# Éditer pour votre contexte
code .bob/rules.md

# Bob utilisera automatiquement ces rules
```

#### 3. `ai-rag-hygiene.md`

Rules concises (10 lignes) pour RAG et embeddings :
- Pin embedding model et dimension
- Provenance et citation des sources
- Chunking délibéré avec overlap
- Pas de secrets/PII dans le vector store
- Grounding des réponses dans le contexte
- Métadonnées : Owner, Last-reviewed, Scope, Persona

**Utilisation** :
```bash
# Copier et adapter
cp exemples/rules/ai-rag-hygiene.md .bob/rules.md

# Bob appliquera automatiquement ces règles
```

#### 4. `backend-api-discipline.md`

Rules concises (11 lignes) pour API/FastAPI backend :
- Validation stricte avec Pydantic
- Authorization deny-by-default
- Pas de stack traces/secrets exposés
- Idempotency keys pour side-effects
- Pagination obligatoire
- Async handlers pour I/O
- Métadonnées professionnelles

**Utilisation** :
```bash
# Copier et adapter
cp exemples/rules/backend-api-discipline.md .bob/rules.md

# Bob respectera ces règles automatiquement
```

#### 5. `projet-frontend-exemple.md`

Rules complètes pour un projet React TypeScript :
- Stack technique (React, TypeScript, Vite)
- Structure du projet
- Conventions TypeScript
- Conventions React (composants, hooks, state)
- Styling (Tailwind, CSS Modules)
- API et data fetching (React Query)
- Forms (React Hook Form + Zod)
- Tests (Vitest, React Testing Library)
- Sécurité
- Performance

**Utilisation** :
```bash
# Copier et adapter
cp exemples/rules/projet-frontend-exemple.md .bob/rules.md

# Adapter à votre projet
code .bob/rules.md
```

---

## 🎯 Comment Utiliser Ces Exemples

### Option 1 : Utiliser Tel Quel

Si l'exemple correspond exactement à vos besoins :

```bash
# Créer la structure
mkdir -p .bob/skills

# Copier le skill
cp exemples/skills/python-best-practices.yaml .bob/skills/

# Copier les rules
cp exemples/rules/projet-api-exemple.md .bob/rules.md
```

### Option 2 : Adapter à Vos Besoins

Recommandé pour la plupart des projets :

```bash
# Copier comme base
cp exemples/skills/python-best-practices.yaml .bob/skills/mon-projet.yaml

# Éditer et personnaliser
code .bob/skills/mon-projet.yaml

# Même chose pour les rules
cp exemples/rules/projet-api-exemple.md .bob/rules.md
code .bob/rules.md
```

### Option 3 : Combiner Plusieurs Exemples

Pour des projets complexes :

```bash
# Créer plusieurs skills
cp exemples/skills/python-best-practices.yaml .bob/skills/
cp exemples/skills/fastapi-development.yaml .bob/skills/

# Créer des rules qui référencent les deux
cat > .bob/rules.md << 'EOF'
# Règles du Projet

Ce projet utilise Python (voir python-best-practices.yaml) 
et FastAPI (voir fastapi-development.yaml).

## Spécificités de Notre Projet
[Vos règles spécifiques ici]
EOF
```

---

## 💡 Conseils d'Utilisation

### Pour les Skills

1. **Commencez simple** : Utilisez un skill de base et ajoutez progressivement
2. **Un skill par domaine** : Séparez Python, FastAPI, React, etc.
3. **Versionnez** : Utilisez semantic versioning (1.0.0, 1.1.0, etc.)
4. **Documentez** : Ajoutez des commentaires dans le YAML
5. **Testez** : Vérifiez que Bob applique bien le skill

### Pour les Rules

1. **Soyez spécifique** : Plus c'est précis, mieux Bob comprend
2. **Structurez** : Utilisez des sections claires (Architecture, Conventions, etc.)
3. **Illustrez** : Donnez des exemples de code
4. **Priorisez** : Mettez les règles importantes en premier
5. **Maintenez** : Mettez à jour avec l'évolution du projet

### Combiner Skills et Rules

```
Skills (YAML)              Rules (Markdown)
     ↓                           ↓
Configuration              Instructions
technique                  contextuelles
     ↓                           ↓
        ↘                   ↙
          Bob Personnalisé
                ↓
        Code de Qualité
```

**Exemple** :
- **Skill** : "Utilise Black avec max_line_length=88"
- **Rules** : "Dans ce projet, nous utilisons Black car il élimine les débats de style"

---

## 🔄 Workflow Recommandé

### 1. Nouveau Projet

```bash
# 1. Créer la structure
mkdir -p .bob/skills

# 2. Choisir un skill de base
cp exemples/skills/python-best-practices.yaml .bob/skills/

# 3. Créer des rules initiales
cp exemples/rules/projet-api-exemple.md .bob/rules.md

# 4. Adapter à votre contexte
code .bob/skills/
code .bob/rules.md

# 5. Tester avec Bob
# "Crée une fonction test() en respectant nos standards"
```

### 2. Projet Existant

```bash
# 1. Analyser le code existant
# Identifier les patterns et conventions

# 2. Créer des skills correspondants
# Documenter ce qui existe déjà

# 3. Écrire les rules
# Expliquer l'architecture et les décisions

# 4. Tester progressivement
# Commencer par de petites tâches
```

### 3. Équipe

```bash
# 1. Créer un repo de skills partagés
git init team-skills
cd team-skills
mkdir -p skills/common skills/backend skills/frontend

# 2. Copier les exemples comme base
cp ../exemples/skills/*.yaml skills/common/

# 3. Créer des templates de rules
cp ../exemples/rules/*.md templates/

# 4. Documenter l'utilisation
# Créer un README pour l'équipe

# 5. Utiliser dans les projets
cd mon-projet
ln -s ../team-skills/skills/common/*.yaml .bob/skills/
```

---

## 📖 Ressources Supplémentaires

### Documentation Officielle

- **Skills** : https://internal.bob.ibm.com/docs/ide/features/skills
- **Rules** : https://internal.bob.ibm.com/docs/ide/configuration/rules

### Autres Fichiers du Lab

- **README.md** : Guide complet du lab
- **REFERENCE_RAPIDE.md** : Référence condensée
- **EXEMPLES_PRATIQUES.md** : Cas d'usage détaillés
- **GUIDE_FORMATEUR.md** : Pour les formateurs

---

## 🎯 Checklist d'Utilisation

### Avant de Commencer
- [ ] J'ai lu le README.md du lab
- [ ] Je comprends la différence entre skills et rules
- [ ] J'ai identifié mes besoins

### Configuration
- [ ] J'ai créé le dossier `.bob/skills/`
- [ ] J'ai copié ou créé au moins un skill
- [ ] J'ai créé le fichier `.bob/rules.md`
- [ ] J'ai adapté les exemples à mon contexte

### Test
- [ ] J'ai testé avec une demande simple à Bob
- [ ] Bob applique bien mes skills
- [ ] Bob respecte mes rules
- [ ] Le code généré correspond à mes attentes

### Partage (Optionnel)
- [ ] J'ai documenté mes skills/rules
- [ ] J'ai partagé avec l'équipe
- [ ] J'ai créé un repo partagé
- [ ] J'ai formé l'équipe

---

## ❓ FAQ

**Q: Puis-je modifier ces exemples ?**  
R: Oui ! Ce sont des bases à adapter à vos besoins.

**Q: Combien de skills puis-je avoir ?**  
R: Autant que nécessaire. Recommandation : 1 skill par domaine.

**Q: Les rules remplacent-elles les skills ?**  
R: Non, ils sont complémentaires. Skills = config technique, Rules = contexte.

**Q: Comment partager avec mon équipe ?**  
R: Créez un repo Git avec vos skills et clonez-le dans chaque projet.

**Q: Bob utilise-t-il automatiquement mes skills/rules ?**  
R: Oui, s'ils sont dans `.bob/skills/` et `.bob/rules.md`.

---

## 🚀 Prochaines Étapes

1. **Explorez les exemples** : Lisez les fichiers fournis
2. **Testez** : Copiez un exemple et testez avec Bob
3. **Adaptez** : Modifiez selon vos besoins
4. **Créez** : Créez vos propres skills et rules
5. **Partagez** : Partagez avec votre équipe

**Bon développement avec Bob ! 🎉**

---

_Exemples créés pour le Bobathon 2026_