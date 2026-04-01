# Lab 6 : Création de Serveurs MCP et Modes Personnalisés

## Vue d'ensemble

Dans ce lab avancé, vous apprendrez à étendre les capacités de Bob en créant des serveurs Model Context Protocol (MCP) personnalisés et des modes personnalisés. Cela vous permet d'intégrer Bob avec les outils, API et workflows de votre organisation, rendant Bob encore plus puissant et adapté à vos besoins spécifiques.

> **🔧 Différenciateur Bob : [Architecture Extensible](../bob-differentiators.md#1--extensible-architecture)**
> Ce lab met en valeur le différenciateur le plus puissant de Bob—son architecture extensible. Grâce aux modes personnalisables et aux intégrations de serveurs MCP, Bob s'adapte à VOTRE environnement et workflows. Contrairement à d'autres assistants IA qui fonctionnent de manière isolée, Bob peut se connecter aux API internes, bases de données, systèmes de documentation et outils personnalisés. Cette extensibilité rend Bob particulièrement précieux pour les équipes d'entreprise avec des besoins spécifiques et des chaînes d'outils existantes.

**Durée :** 45-60 minutes (serveur météo) + 30-45 minutes optionnel (serveur JIRA)

**Difficulté :** Intermédiaire à Avancé

**Prérequis :** Avoir complété les labs 0, 1 et 1 bis, comprendre les API REST de base.

## Objectifs d'apprentissage

À la fin de ce lab, vous serez capable de :

1. Comprendre l'architecture du Model Context Protocol (MCP)
2. Créer un serveur MCP simple et fonctionnel
3. Implémenter des outils de serveur MCP
4. Intégrer des API externes avec Bob
5. Configurer et tester des serveurs MCP
6. (Optionnel) Créer des intégrations complexes avec JIRA, bases de données, etc.
7. (Optionnel) Créer des modes Bob personnalisés pour des workflows spécifiques

## Qu'est-ce que MCP ?

**Model Context Protocol (MCP)** est un protocole ouvert qui permet aux assistants IA comme Bob de :

- Accéder à des sources de données externes
- Exécuter des outils et fonctions personnalisés
- S'intégrer avec des services tiers
- Étendre les capacités au-delà des fonctionnalités intégrées

> **🎯 Pourquoi MCP est important**
>    
> MCP est un élément clé de l'[architecture extensible](../bob-differentiators.md#mcp-server-integration) de Bob. Il permet à Bob de s'intégrer avec les outils internes, API et services de votre entreprise. Cela signifie que Bob peut accéder à votre documentation, interroger vos bases de données, créer des tickets dans votre système de suivi, et déployer sur votre infrastructure—le tout en langage naturel. Bob s'adapte à VOTRE environnement, pas l'inverse.

**Concepts Clés :**

- **Serveur MCP** : Un service qui expose des outils et ressources à Bob
- **Outils** : Fonctions que Bob peut appeler pour effectuer des actions
- **Ressources** : Sources de données que Bob peut interroger
- **Prompts** : Modèles de prompts prédéfinis
- **Mode Personnalisé** : Une configuration Bob spécialisée pour des tâches spécifiques

## Structure du Lab

```
lab6-custom-mcp-modes
├── README.md                           # Ce fichier
├── simple-weather-server/              # 🌤️ COMMENCEZ ICI - Serveur météo simple
│   ├── package.json                    # Dépendances Node.js
│   ├── server.js                       # Serveur MCP météo
│   ├── .env.example                    # Configuration exemple
│   ├── test-api.js                     # Script de test
│   ├── diagnose-api.js                 # Diagnostic API
├── mcp-server/                         # 🔧 OPTIONNEL - Serveur avancé
│   ├── package.json                    # Dépendances Node.js
│   ├── server.js                       # Implémentation principale
│   ├── tools/                          # Implémentations d'outils
│   │   ├── jira-tools.js              # Intégration JIRA
│   │   ├── database-tools.js          # Requêtes de base de données
│   │   └── deployment-tools.js        # Automatisation de déploiement
│   └── .env.example                    # Configuration
└── custom-mode/                        # 🎨 OPTIONNEL - Modes personnalisés
    ├── devops-mode.json               # Mode workflow DevOps
    ├── code-review-mode.json          # Mode revue de code
    └── architecture-mode.json         # Mode conception d'architecture
```

## Partie 1 : Comprendre l'Architecture MCP (Lecture Seule)

> **📖 Cette section est informative uniquement. Aucune action n'est requise pour le moment.**

### Étape 1.1 : Bases du Protocole MCP

MCP utilise une architecture client-serveur :

```
┌─────────────┐         Protocole MCP      ┌─────────────┐
│             │◄──────────────────────────►│             │
│ Client Bob  │    JSON-RPC sur stdio      │ Serveur MCP │
│             │    ou HTTP/WebSocket       │             │
└─────────────┘                            └─────────────┘
       │                                          │
       │                                          │
       ▼                                          ▼
  Requêtes Utilisateur                     Services Externes
  - Poser des questions                    - API Météo
  - Exécuter des tâches                    - API JIRA
  - Obtenir des informations               - Base de données
                                          - Outils de déploiement
```

**Composants Clés :**

1. **Outils** : Fonctions que Bob peut appeler

   ```json
   {
     "name": "get_current_weather",
     "description": "Obtenir la météo actuelle pour une ville",
     "parameters": {
       "city": "string",
       "units": "metric | imperial"
     }
   }
   ```

2. **Ressources** : Données auxquelles Bob peut accéder

   ```json
   {
     "uri": "weather://cities/popular",
     "name": "Villes Populaires",
     "mimeType": "application/json"
   }
   ```

## Partie 2 : Créer Votre Premier Serveur MCP - Serveur Météo Simple

> **✅ ACTION REQUISE : Complétez les Étapes 2.1-2.5**

### Étape 2.1 : Initialiser le Serveur Météo

**🔨 ACTION : Configurer le serveur météo MCP**

Le serveur météo est un excellent point de départ car il :
- ✅ Fonctionne immédiatement en mode DEMO (sans clé API)
- ✅ Est simple à comprendre et à tester
- ✅ Démontre tous les concepts MCP essentiels
- ✅ Peut être étendu avec une vraie API météo (gratuite)

```bash
cd lab6-custom-mcp-modes/simple-weather-server
npm install
```

Cela installera :
- `@modelcontextprotocol/sdk` - Implémentation du protocole MCP
- `dotenv` - Gestion des variables d'environnement

### Étape 2.2 : Examiner l'Implémentation du Serveur

**📖 REVUE : Comprendre la structure du serveur**

Ouvrez et examinez [`simple-weather-server/server.js`](simple-weather-server/server.js)

Le serveur implémente **3 outils simples** :

1. **`get_current_weather`** - Obtenir la météo actuelle
   ```javascript
   // Exemple d'utilisation avec Bob :
   // "Quelle est la météo à Paris ?"
   ```

2. **`get_forecast`** - Obtenir les prévisions sur 5 jours
   ```javascript
   // "Montre-moi les prévisions pour Tokyo"
   ```

3. **`convert_temperature`** - Convertir Celsius ↔ Fahrenheit
   ```javascript
   // "Convertis 25 Celsius en Fahrenheit"
   ```

**Et 1 ressource** :
- **`weather://cities/popular`** - Liste de villes populaires

### Étape 2.3 : Tester le Serveur avec l'API Météo

**🔨 ACTION : Tester avec la clé API fournie**

Une clé API OpenWeatherMap est déjà intégrée dans le script de test pour les participants du Bobathon :

```bash
cd lab6-custom-mcp-modes/simple-weather-server
node test-api.js
```

Le script effectuera 3 tests automatiques :
1. ✅ Météo actuelle pour Paris
2. ✅ Prévisions sur 5 jours pour Tokyo
3. ✅ Validation de la clé API

Vous devriez voir des données météo réelles !

**Diagnostic complet** : Pour vérifier votre configuration complète, utilisez :
```bash
node diagnose-api.js
```

Ce script vérifie :
- ✅ Fichiers du serveur
- ✅ Dépendances Node.js
- ✅ Connexion API
- ✅ Configuration complète

### Étape 2.4 : Configurer le Serveur MCP dans Bob

**🔨 ACTION : Connecter le serveur météo à Bob**

1. Ouvrez les Paramètres Bob (icône d'engrenage ⚙️)
2. Naviguez vers la section **MCP**
3. Choisissez **MCPs de Projet** (recommandé pour ce lab)
4. Cliquez pour éditer le fichier de configuration JSON
5. Ajoutez cette configuration :

   ```json
   {
     "mcpServers": {
       "simple-weather": {
         "command": "node",
         "args": ["server.js"],
         "cwd": "/chemin/absolu/vers/lab6-custom-mcp-modes/simple-weather-server"
       }
     }
   }
   ```

   > **💡 Astuce :** Remplacez `/chemin/absolu/vers/` par le chemin complet vers votre dossier lab6

6. Sauvegardez le fichier
7. **Redémarrez Bob** (Cmd+Shift+P → "Reload Window")

> **⚠️ Important :** Les outils MCP ne fonctionnent qu'en **mode Avancé** (🛠️). Assurez-vous de passer en mode Avancé avant de tester !

### Étape 2.5 : Tester avec Bob

**🔨 ACTION : Utiliser le serveur météo avec Bob**

1. **Passez en mode Avancé** (🛠️) dans Bob
2. Testez ces commandes :

   ```
   "Quels serveurs MCP sont connectés ?"
   "Quelle est la météo à Paris ?"
   "Montre-moi les prévisions pour Tokyo"
   "Convertis 25 Celsius en Fahrenheit"
   "Montre-moi les villes populaires"
   ```

Bob utilisera automatiquement les outils du serveur météo !

### Étape 2.6 : Comprendre la Configuration API

**📋 INFORMATION : Clé API pour le Hackathon**

Pour ce lab, une clé API OpenWeatherMap sera fournie par les organisateurs au début du hackathon.

**Clé API** : `[sera communiquée au début du hackathon]`

Cette clé partagée permettra :
- ✅ 1,000 appels/jour
- ✅ 60 appels/minute
- ✅ Accès aux données météo en temps réel
- ✅ Prévisions sur 5 jours

**💡 Pour votre usage personnel après le Bobathon** :

Si vous souhaitez continuer à utiliser ce serveur MCP après l'événement avec votre propre clé API :

1. **Obtenez une clé API gratuite** :
   - Allez sur https://openweathermap.org/api
   - Inscrivez-vous (gratuit, 2 minutes)
   - Copiez votre clé API

2. **Configurez votre clé** :
   ```bash
   cd lab6-custom-mcp-modes/simple-weather-server
   cp .env.example .env
   # Éditez .env et ajoutez : OPENWEATHER_API_KEY=votre_clé
   ```

3. **Redémarrez VS Code** pour que Bob utilise votre clé personnelle

## Partie 3 : (Optionnel) Serveur MCP Avancé avec JIRA

> **💡 OPTIONNEL : Cette partie est pour les utilisateurs avancés qui veulent créer des intégrations complexes**

> **📖 NOTE :** Si vous n'avez pas de configuration JIRA disponible, vous pouvez suivre cette partie en lecture seule pour comprendre les concepts avancés.

### Étape 3.1 : Initialiser le Serveur Avancé

**🔨 ACTION OPTIONNELLE : Configurer le serveur avancé**

```bash
cd lab6-custom-mcp-modes/mcp-server
npm install
```

Ce serveur inclut :
- Intégration JIRA (création/recherche de tickets)
- Outils de base de données (requêtes en lecture seule)
- Automatisation de déploiement
- Ressources de documentation

### Étape 3.2 : Configuration JIRA

**🔨 ACTION OPTIONNELLE : Configurer JIRA**

1. Créez un fichier `.env` :
   ```bash
   cp .env.example .env
   ```

2. Ajoutez vos credentials JIRA :
   ```env
   JIRA_URL=https://votre-domaine.atlassian.net
   JIRA_EMAIL=votre-email@example.com
   JIRA_API_TOKEN=votre-token-jira
   ```

3. Configurez dans Bob (ajoutez à `.bob/mcp.json`) :
   ```json
   {
     "mcpServers": {
       "simple-weather": {
         "command": "node",
         "args": ["server.js"],
         "cwd": "/chemin/vers/simple-weather-server"
       },
       "advanced-server": {
         "command": "node",
         "args": ["server.js"],
         "cwd": "/chemin/vers/mcp-server",
         "env": {
           "LOG_LEVEL": "info"
         }
       }
     }
   }
   ```

### Étape 3.3 : Tester le Serveur Avancé

**🔨 ACTION OPTIONNELLE : Tester avec Bob**

En mode Avancé, testez :

```
"Crée un ticket JIRA pour correction de bug : La page de connexion ne charge pas"
"Recherche les tickets JIRA assignés à moi"
"Montre-moi le schéma de la table users"
"Déploie la version 2.1.0 sur staging"
```

### Étape 3.4 : Outils Disponibles dans le Serveur Avancé

**📖 REVUE : Outils du serveur avancé**

**Outils JIRA** (`tools/jira-tools.js`) :
- `create_jira_ticket` - Créer des tickets
- `search_jira_tickets` - Rechercher avec JQL
- `update_ticket` - Mettre à jour des tickets
- `add_comment` - Ajouter des commentaires

**Outils Base de Données** (`tools/database-tools.js`) :
- `query_database` - Requêtes SELECT en lecture seule
- `get_table_schema` - Obtenir les schémas de tables

**Outils Déploiement** (`tools/deployment-tools.js`) :
- `deploy_application` - Déployer des applications
- `check_deployment_status` - Vérifier le statut
- `rollback_deployment` - Annuler un déploiement

## Partie 4 : (Optionnel) Modes Personnalisés

> **💡 OPTIONNEL : Créer des modes spécialisés pour des workflows spécifiques**

> **🎯 Différenciateur Bob : [Modes Personnalisables](../bob-differentiators.md#customizable-modes)**
> Les modes personnalisés sont un différenciateur clé pour Bob. Vous pouvez créer des modes spécialisés pour la revue de code, la documentation, la conception d'architecture, les workflows DevOps, ou tout processus spécifique à l'équipe. Ces modes peuvent être partagés via le marketplace, assurant un comportement cohérent dans votre équipe.

### Étape 4.1 : Installer un Mode Personnalisé

**💡 OPTIONNEL : Comment installer des modes**

1. Ouvrez les Paramètres Bob
2. Naviguez vers **Modes Personnalisés**
3. Cliquez sur **Importer un Mode**
4. Sélectionnez un fichier :
   - `custom-mode/devops-mode.json` - Workflow DevOps
   - `custom-mode/code-review-mode.json` - Revue de code
   - `custom-mode/architecture-mode.json` - Conception d'architecture

### Étape 4.2 : Modes Disponibles

**Mode DevOps** (`devops-mode.json`) :
- Automatisation de déploiement
- Gestion d'infrastructure
- Surveillance et alertes
- Réponse aux incidents

**Mode Revue de Code** (`code-review-mode.json`) :
- Analyse de code automatisée
- Scan de sécurité
- Vérification des meilleures pratiques
- Suggestions d'amélioration

**Mode Architecture** (`architecture-mode.json`) :
- Assistance à la conception système
- Documentation d'architecture
- Recommandations technologiques
- Analyse de scalabilité

## Dépannage

### Problèmes Courants

1. **Le Serveur ne Démarre Pas**
   - Vérifiez : `npm install` dans le répertoire du serveur
   - Vérifiez les logs dans le terminal
   - Assurez-vous que Node.js est installé : `node --version`

2. **Outils Non Disponibles dans Bob**
   - **Le Plus Courant :** Vérifiez que vous êtes en **mode Avancé** (🛠️)
   - Vérifiez que le serveur MCP est configuré dans `.bob/mcp.json`
   - Vérifiez que le chemin `cwd` est correct (chemin absolu)
   - Redémarrez VS Code complètement

3. **Serveur Météo Retourne 401**
   - C'est normal si vous n'avez pas de clé API
   - Le serveur fonctionne en mode DEMO automatiquement
   - Pour les vraies données, obtenez une clé API gratuite

4. **JIRA ne Fonctionne Pas**
   - Vérifiez les credentials dans `.env`
   - Testez l'API JIRA directement avec curl
   - Vérifiez que le token n'a pas expiré

## Résumé

Dans ce lab, vous avez appris :

✅ Comprendre l'architecture et le protocole MCP

✅ Créer un serveur MCP simple et fonctionnel (météo)

✅ Configurer et tester des serveurs MCP avec Bob

✅ Utiliser les outils MCP en mode Avancé

✅ (Optionnel) Créer des intégrations complexes (JIRA, DB, déploiement)

✅ (Optionnel) Installer et utiliser des modes personnalisés

> **🎯 Extensibilité : Le Superpouvoir de Bob**  
> Vous avez maintenant expérimenté l'[architecture extensible](../../bob-differentiators.md#1--extensible-architecture) de Bob. En créant des serveurs MCP et des modes personnalisés, vous pouvez adapter Bob aux besoins uniques de votre organisation. Cette extensibilité, combinée avec les autres différenciateurs de Bob comme l'[optimisation intelligente des ressources](../../bob-differentiators.md#2--intelligent-resource-optimization), [Bob Findings](../../bob-differentiators.md#3--bob-findings-automated-analysis-engine), et la [modernisation Java d'entreprise](../../bob-differentiators.md#4--enterprise-java-modernization), entre autres, fait de Bob un outil particulièrement puissant pour les équipes de développement.

## Prochaines Étapes

- Explorez d'autres API gratuites (GitHub, Slack, etc.)
- Créez des outils spécifiques à votre organisation
- Partagez des serveurs MCP avec votre équipe
- Créez des modes personnalisés pour vos workflows
- Contribuez à l'écosystème MCP

## Ressources Supplémentaires

- [Spécification du Protocole MCP](https://modelcontextprotocol.io/docs)
- [Documentation du SDK MCP](https://github.com/modelcontextprotocol/sdk)
- [Guide d'Intégration MCP de Bob](https://ibm.com/bob/docs/mcp)
- [Exemples de Serveurs MCP](https://github.com/modelcontextprotocol/servers)
- [Serveurs MCP Communautaires](https://github.com/topics/mcp-server)

---

**Besoin d'Aide ?** Si vous rencontrez des problèmes :

1. **Lancez le diagnostic** : `node diagnose-api.js` dans le dossier `simple-weather-server/`
2. Consultez la section dépannage ci-dessus
3. Vérifiez que vous êtes en mode Avancé (🛠️)
4. Testez avec `node test-api.js` pour vérifier la connexion API



## 🏆 Félicitations !

---

_Lab créé pour le Bobathon 2026_
