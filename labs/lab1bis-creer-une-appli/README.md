# Lab 1 : Créer une application Todo avec Bob

## Vue d'ensemble

Dans ce lab, vous apprendrez à utiliser les fonctionnalités alimentées par l'IA de Bob pour construire une application Todo full-stack complète à partir de zéro. Vous découvrirez les différents modes de Bob, les auto-approbations, le codage littéraire et l'intégration GitHub.

**Durée** : 45 minutes  
**Difficulté** : Débutant à Intermédiaire

## Ce que vous allez construire

Une application Todo full-stack avec :

- **Backend** : API REST Python Flask avec base de données SQLite
- **Frontend** : Application JavaScript moderne monopage
- **Fonctionnalités** : Créer, lire, mettre à jour et supprimer des todos
- **Contrôle de version** : Dépôt GitHub avec commits appropriés

## Objectifs d'apprentissage

À la fin de ce lab, vous serez capable de :

- ✅ Comprendre les trois modes de Bob (Architect, Code, Ask)
- ✅ Utiliser les auto-approbations pour un développement rapide
- ✅ Pratiquer les techniques de codage littéraire
- ✅ Intégrer GitHub en utilisant les serveurs MCP
- ✅ Construire une application full-stack complète

## Prérequis

Avant de commencer, assurez-vous d'avoir :

- [ ] Python 3.8+ installé
- [ ] Node.js 14+ installé (pour npm)
- [ ] Git installé et configuré
- [ ] Bob installé et en cours d'exécution
- [ ] Compte GitHub (pour l'intégration MCP)
- [ ] Éditeur de texte ou IDE ouvert

Si vous n'avez pas terminé la configuration, consultez [prerequisites.md](../../prerequisites.md).

## Structure du lab

```
Chronologie du Lab 1 (45 minutes)
├── Étape 1 : Introduction et planification (5 min)
├── Étape 2 : Développement du backend (15 min)
├── Étape 3 : Développement du frontend (15 min)
├── Étape 4 : Intégration GitHub (5 min)
└── Étape 5 : Tests et vérification (5 min)
```

---

## Étape 1 : Introduction aux modes de Bob (5 minutes)

### Comprendre les modes de Bob

Bob dispose de trois modes distincts, chacun optimisé pour différentes tâches :

> **🎯 Différenciateur Bob : [Modes personnalisables](../../bob-differentiators.md#1--extensible-architecture)**
> Le système de modes de Bob est l'un de ses principaux différenciateurs. Contrairement à d'autres assistants IA, Bob vous permet de créer des modes personnalisés adaptés aux flux de travail spécifiques de votre équipe. Les trois modes intégrés que vous utiliserez dans ce lab ne sont qu'un début—vous pouvez créer des modes spécialisés pour la revue de code, la documentation, la conception d'architecture, et plus encore. En savoir plus dans le lab6.

#### 🎯 Mode Plan

**Quand l'utiliser** : Planification, conception, stratégie

- Créer des structures de projet
- Concevoir des endpoints API
- Planifier des schémas de base de données
- Prendre des décisions architecturales

#### 💻 Mode Code

**Quand l'utiliser** : Écrire, modifier, refactoriser du code

- Implémenter des fonctionnalités
- Créer des fichiers
- Modifier du code existant
- Corriger des bugs

#### ❓ Mode Ask

**Quand l'utiliser** : Apprendre, comprendre, obtenir de l'aide

- Expliquer des concepts de code
- Obtenir de la documentation
- Comprendre les erreurs
- Apprendre les meilleures pratiques

### Basculer entre les modes

Vous avez **plusieurs options** pour changer de mode :

**1. Menu déroulant :**

- Cliquez sur le sélecteur de mode (en bas de la fenêtre Bob)
- Sélectionnez le mode dont vous avez besoin

**2. Commandes slash :**

- Tapez `/plan` pour passer en mode Plan
- Tapez `/code` pour passer en mode Code
- Tapez `/ask` pour passer en mode Ask
- La commande change le mode et efface le champ de saisie

**3. Raccourci clavier :**

- **macOS** : `⌘ + .`
- **Windows/Linux** : `Ctrl + .`
- Chaque pression fait défiler les modes disponibles

**💡 Astuce :** Les commandes slash sont le moyen le plus rapide de changer de mode ! Tapez simplement `/` suivi du nom du mode.

**Avant de démarrer, créez un repertoire `my_todo_app` et ouvrez le via Bob. C'est dans ce repertoire que Bob créera toutes les ressources de l'application que vous allez développer.**

En outre, si jamais vous êtes coincé ou si vous n'avez pas le temps de compléter le lab, une version fonctionnelle de l'application est disponible [ici](./solution).

### Votre première tâche : Planification du projet

**Passez en mode Plan** et demandez à Bob :

```
Je veux créer une application Todo avec un backend Python Flask et un frontend JavaScript.
Aidez-moi à planifier :
1. La structure des répertoires du projet
2. Les endpoints API nécessaires
3. Le schéma de base de données
4. Les recommandations de pile technologique
```

**Réponse attendue de Bob :**

Bob devrait fournir :

- Structure de répertoires avec dossiers backend/ et frontend/
- Endpoints API REST (GET, POST, PUT, DELETE)
- Schéma de base de données pour les todos (id, title, description, completed, created_at)
- Recommandations pour Flask, SQLite, CORS, etc.

**💡 Conseil** : Prenez des notes sur les recommandations de Bob. Vous utiliserez ce plan dans les prochaines étapes. Vous pouverz aussi demander à Bob de documenter ce plan dans un fichier markdown.

---

## Étape 2 : Développement du backend avec le mode Code (15 minutes)

Construisons maintenant le backend Flask en utilisant le mode Code de Bob.

### 2.1 : Passer en mode Code

Passez au mode Code dans l'interface de Bob.

### 2.2 : Créer la structure du backend

**Prompt pour Bob :**

```
Créez un backend Flask pour l'application Todo avec les fichiers suivants :
1. app.py - Application Flask principale avec CORS activé
2. models.py - Modèle Todo SQLAlchemy
3. database.py - Initialisation de la base de données
4. requirements.txt - Dépendances Python

Le modèle Todo doit avoir : id, title, description, completed (booléen), created_at (timestamp)
```

**Ce que Bob va créer :**

Bob devrait générer ces fichiers dans le répertoire `backend/`. Examinez chaque fichier au fur et à mesure que Bob les crée.

### 2.3 : Comprendre les auto-approbations

Les **auto-approbations** permettent à Bob d'effectuer plusieurs modifications sans demander confirmation à chaque fois.

Pour activer les auto-approbations :

1. Trouvez les paramètres d'auto-approbation de Bob au-dessus du champ de saisie du chat ou dans les paramètres de Bob, onglet **'Chat'**
2. Autorisez pour cette session **Read** et **Write**, vous pouvez changer ces paramètres à tout moment
3. Bob créera maintenant plusieurs fichiers rapidement

**⚠️ Important** : Examinez les fichiers après que Bob les ait créés pour vous assurer qu'ils correspondent à vos exigences.

### 2.4 : Implémenter les endpoints API REST

**Prompt pour Bob :**

```
Si ce n'est pas déjà fait, implémentez les endpoints API REST suivants dans app.py :
- GET /api/todos - Lister tous les todos
- POST /api/todos - Créer un nouveau todo
- PUT /api/todos/<id> - Mettre à jour un todo
- DELETE /api/todos/<id> - Supprimer un todo

Incluez une gestion appropriée des erreurs et des réponses JSON.
```

### 2.5 : Examiner le code généré

Bob devrait avoir créé quelque chose de similaire à cette structure :

**app.py** (Sections clés) :

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import todo
from database import db, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

init_db(app)

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = todo(
        title=data.get('title'),
        description=data.get('description', ''),
        completed=False
    )
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201

# Endpoints supplémentaires...
```

### 2.6 : Tester la configuration du backend

Créez un environnement virtuel et installez les dépendances :

```bash
# Naviguez vers le répertoire backend
cd backend

# Créez un environnement virtuel
python -m venv venv

# Activez l'environnement virtuel
# macOS/Linux
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat

# Installez les dépendances
pip install -r requirements.txt

# Lancez l'application
python app.py
```

Le serveur devrait démarrer sur `http://localhost:5000`. Demandez un autre port à Bob si ce port là est déjà pris.

**✅ Point de contrôle** : Le backend fonctionne sans erreurs.

---

## Étape 3 : Développement du frontend (15 minutes)

Créons maintenant l'interface utilisateur en utilisant JavaScript.

### 3.1 : Créer la structure du frontend

**Prompt pour Bob (toujours en mode Code) :**

```
Créez un frontend pour l'application todo avec :
1. index.html - Structure HTML principale avec un design propre et moderne
2. styles.css - Style CSS responsive
3. app.js - JavaScript pour les interactions API

Incluez :
- Champ de saisie pour les nouveaux todos
- Liste pour afficher les todos
- Boutons pour les actions de complétion et de suppression
- Design responsive pour mobile et desktop
```

### 3.2 : Comprendre le codage littéraire

Le **codage littéraire** signifie écrire du code qui s'explique lui-même à travers des commentaires et une structure claire.

**Prompt pour Bob :**

```
Dans app.js, utilisez le codage littéraire pour expliquer :
- Comment fonctionnent les appels API
- Pourquoi nous utilisons async/await
- Comment la gestion des erreurs est implémentée
- Le but de chaque fonction

Ajoutez des commentaires détaillés qui aideraient un débutant à comprendre le code.
```

### 3.3 : Examiner le code du frontend

Bob devrait créer des fichiers similaires à ceci :

**app.js** (avec codage littéraire) :

```javascript
/**
 * Application Todo - JavaScript Frontend
 *
 * Ce fichier gère toutes les interactions entre l'interface utilisateur
 * et l'API backend Flask. Nous utilisons des fonctionnalités JavaScript modernes
 * comme async/await pour un code asynchrone plus propre.
 */

// URL de base de l'API - pointe vers notre backend Flask
const API_URL = "http://localhost:5000/api/todos";

/**
 * Récupère tous les todos depuis l'API backend
 *
 * Cette fonction démontre le pattern async/await :
 * - Le mot-clé 'async' nous permet d'utiliser 'await' à l'intérieur
 * - 'await' met en pause l'exécution jusqu'à ce que la promesse soit résolue
 * - Cela rend le code asynchrone plus lisible et synchrone
 *
 * @returns {Promise<void>}
 */
async function fetchTodos() {
  try {
    // Effectue une requête GET vers le backend
    const response = await fetch(API_URL);

    // Parse la réponse JSON
    const todos = await response.json();

    // Met à jour l'UI avec les todos récupérés
    displayTodos(todos);
  } catch (error) {
    // Gère toutes les erreurs (problèmes réseau, erreurs serveur, etc.)
    console.error("Erreur lors de la récupération des todos:", error);
    showError("Échec du chargement des todos. Veuillez réessayer.");
  }
}

/**
 * Crée un nouvel élément todo
 *
 * Cette fonction montre comment effectuer une requête POST avec des données JSON.
 * Nous utilisons l'API Fetch qui retourne des promesses, la rendant parfaite
 * pour la syntaxe async/await.
 *
 * @param {string} title - Le titre du todo
 * @param {string} description - La description du todo
 */
async function createTodo(title, description) {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title, description }),
    });

    if (response.ok) {
      // Rafraîchit la liste des todos
      await fetchTodos();
      // Efface le formulaire de saisie
      clearForm();
    }
  } catch (error) {
    console.error("Erreur lors de la création du todo:", error);
    showError("Échec de la création du todo. Veuillez réessayer.");
  }
}

// Fonctions supplémentaires avec explications détaillées...
```

### 3.4 : Tester le frontend

Ouvrez `frontend/index.html` dans votre navigateur :

```bash
# Depuis le répertoire lab1
cd frontend

# Ouvrez dans le navigateur par défaut
# macOS
open index.html

# Linux
xdg-open index.html

# Windows (CMD)
start index.html

# Windows (PowerShell)
Start-Process index.html
```

**✅ Point de contrôle** : Le frontend se charge et affiche l'UI.

---

## Étape 4 : Intégration GitHub avec MCP (10 minutes): OPTIONNEL

Utilisons maintenant le serveur MCP GitHub de Bob pour gérer le contrôle de version.

### 4.1 : Comprendre les serveurs MCP

> **🔧 Différenciateur Bob : [Intégration de serveurs MCP](../../bob-differentiators.md#mcp-server-integration)**
> L'intégration MCP (Model Context Protocol) de Bob est un différenciateur puissant qui vous permet de connecter des outils et services externes directement dans votre flux de travail. Contrairement à d'autres assistants IA qui travaillent de manière isolée, Bob peut s'intégrer avec les API internes de votre entreprise, les bases de données, les systèmes de documentation, et plus encore. Cela signifie que Bob s'adapte à VOTRE environnement, et non l'inverse.

**MCP (Model Context Protocol)** permet à Bob d'interagir avec des services externes comme GitHub.

Avantages :

- Bob peut créer des dépôts
- Bob peut effectuer des commits
- Bob peut pousser du code
- Tout cela via des commandes en langage naturel
- **Extensible** : Connectez-vous à n'importe quel service avec un serveur MCP (JIRA, bases de données, outils de déploiement, etc.)
- **Transparent** : Pas de changement de contexte entre les outils

Pour configurer un serveur MCP permettant l'interaction avec github.com, passez en mode "Code" et utilisez le prompt :

**Prompt pour Bob :**

```
configure mon projet et notamment mcp.json pour donner accès à un serveur mcp permettant d'interagir avec github.com
```

### 4.2 : Initialiser le dépôt Git

Passer en mode "Advanced"

**Prompt pour Bob :**

```
Utilisez le serveur MCP GitHub pour :
1. Initialiser un dépôt git dans le répertoire de ce projet de gestion de todos"
2. Créer un fichier .gitignore pour Python et Node.js
3. Créer un commit initial avec le message "Implémentation initiale de l'application Todo"
```

### 4.3 : Créer un dépôt GitHub

**Prompt pour Bob :**

```
Créez un nouveau dépôt GitHub appelé "bob-todo-app" et poussez le code.
Incluez un README.md décrivant le projet.
```

**Ce que Bob va faire :**

1. Créer `.gitignore` avec les entrées appropriées
2. Initialiser le dépôt git
3. Ajouter tous les fichiers au staging
4. Créer le commit initial
5. Créer le dépôt GitHub (si MCP est configuré)
6. Pousser le code vers GitHub

### 4.4 : Vérifier sur GitHub

1. Allez sur votre compte GitHub
2. Trouvez le dépôt `bob-todo-app`
3. Vérifiez que tous les fichiers sont présents
4. Vérifiez l'historique des commits

**✅ Point de contrôle** : Le code est sur GitHub avec des commits appropriés.

---

## Étape 5 : Tests et vérification (5 minutes)

Testons l'application complète de bout en bout.

### 5.1 : Démarrer le backend

```bash
# Dans le répertoire backend avec venv activé
python app.py
```

Le serveur devrait fonctionner sur `http://localhost:5000`

### 5.2 : Ouvrir le frontend

Ouvrez `frontend/index.html` dans votre navigateur.

### 5.3 : Tester les opérations CRUD

**Créer un todo :**

1. Entrez un titre : "Apprendre Bob"
2. Entrez une description : "Compléter les trois labs"
3. Cliquez sur "Ajouter todo"
4. ✅ Le todo apparaît dans la liste

**Marquer comme terminé :**

1. Cliquez sur le bouton "Terminé" sur un todo
2. ✅ Le todo s'affiche comme terminé (barré ou avec une coche)

**Supprimer un todo :**

1. Cliquez sur le bouton "Supprimer" sur un todo
2. ✅ Le todo est retiré de la liste

**Rafraîchir la page :**

1. Rafraîchissez le navigateur
2. ✅ Les todos persistent (stockés dans la base de données)

### 5.4 : Vérifier la console du navigateur

Ouvrez les outils de développement du navigateur (F12) :

- ✅ Pas d'erreurs JavaScript
- ✅ Les appels API réussissent (codes de statut 200)
- ✅ Les données sont correctement formatées

### 5.5 : Vérifier la base de données

```bash
# Dans le répertoire backend
python
>>> from app import app, db
>>> from models import Todo
>>> with app.app_context():
...     todos = Todo.query.all()
...     for todo in todos:
...         print(f"{todo.id}: {todo.title}")
```

✅ Les todos sont stockés dans la base de données

---

## Félicitations ! 🎉

Vous avez terminé avec succès le Lab 1 ! Vous avez appris à :

- ✅ Utiliser le mode Architect de Bob pour la planification
- ✅ Utiliser le mode Code de Bob pour l'implémentation
- ✅ Activer et utiliser les auto-approbations
- ✅ Appliquer les principes de codage littéraire
- ✅ Intégrer GitHub en utilisant les serveurs MCP
- ✅ Construire une application full-stack complète

## Ce que vous avez construit

```
bob-todo-app/
├── backend/
│   ├── app.py              # API REST Flask
│   ├── models.py           # Modèles de base de données
│   ├── database.py         # Initialisation DB
│   ├── requirements.txt    # Dépendances
│   └── todos.db           # Base de données SQLite
├── frontend/
│   ├── index.html         # Structure UI
│   ├── styles.css         # Style
│   └── app.js             # Logique frontend
└── .gitignore             # Règles d'ignorance Git
```

## Points clés à retenir

### Modes de Bob

- **Architect** : Parfait pour la planification et les décisions de conception
- **Code** : Idéal pour l'implémentation et la création de fichiers
- **Ask** : Excellent pour l'apprentissage et la compréhension
- **Modes personnalisés** : Créez vos propres modes spécialisés ([En savoir plus](../../bob-differentiators.md#customizable-modes))

### Auto-approbations

- Accélère considérablement le développement
- Utile pour créer plusieurs fichiers liés
- Toujours examiner le code généré

### Codage littéraire

- Rend le code auto-documenté
- Aide les membres de l'équipe à comprendre votre code
- Utile pour l'apprentissage et l'enseignement

### GitHub MCP

- Rationalise le contrôle de version
- Opérations git en langage naturel
- S'intègre parfaitement avec Bob
- **Extensible** : Fait partie de la capacité d'[intégration de serveurs MCP](../../bob-differentiators.md#mcp-server-integration) de Bob

> **💡 En coulisses : Optimisation intelligente des ressources**
> Pendant que vous construisiez cette application, Bob a automatiquement sélectionné le bon modèle d'IA pour chaque tâche—utilisant des modèles puissants pour les décisions d'architecture complexes et des modèles plus légers pour les opérations de fichiers simples. Cette [sélection automatique de modèle](../../bob-differentiators.md#automatic-model-selection) optimise à la fois la qualité et le coût sans que vous ayez à y penser. Vous pouvez économiser jusqu'à 60% sur les coûts d'IA tout en maintenant d'excellents résultats !

## Prochaines étapes

### Améliorez votre application

Essayez ces améliorations :

1. Ajouter des catégories ou des tags aux todos
2. Implémenter des dates d'échéance
3. Ajouter l'authentification utilisateur
4. Créer un système de priorités
5. Ajouter des fonctionnalités de recherche et de filtrage

### Continuez l'apprentissage

- **[Lab 2 : Optimisation du code →](../lab2-refactoring/README.md)** - Maîtriser le refactoring avec Bob et améliorer la qualité du code
- **[Lab 3 : Création d'APIs REST →](../lab3-api-tests/README.md)** - Créer des APIs REST professionnelles avec tests complets

## Dépannage

### Problèmes de backend

**Problème** : `ModuleNotFoundError: No module named 'flask'`

```bash
# Assurez-vous que l'environnement virtuel est activé
# macOS/Linux
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat

# Installez les dépendances
pip install -r requirements.txt
```

**Problème** : `Address already in use`

```bash
# Tuez le processus utilisant le port 5000
# macOS/Linux
lsof -ti:5000 | xargs kill -9

# Windows (CMD)
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Windows (PowerShell)
Get-NetTCPConnection -LocalPort 5000 | Select-Object -ExpandProperty OwningProcess | ForEach-Object { Stop-Process -Id $_ -Force }
```

**Problème** : Erreurs de base de données

```bash
# Supprimez et recréez la base de données
rm todos.db
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
```

### Problèmes de frontend

**Problème** : Erreurs CORS dans la console du navigateur

- Assurez-vous que Flask-CORS est installé : `pip install flask-cors`
- Vérifiez que CORS est activé dans `app.py`
- Vérifiez que le backend fonctionne sur le port 5000

**Problème** : Les appels API échouent

- Vérifiez que le backend fonctionne
- Vérifiez que API_URL dans `app.js` correspond à l'URL du backend
- Ouvrez les outils de développement du navigateur et vérifiez l'onglet Réseau

**Problème** : Les todos ne persistent pas

- Vérifiez la console du navigateur pour les erreurs
- Vérifiez que le fichier de base de données existe
- Testez les endpoints API directement avec curl ou Postman

### Problèmes Git/GitHub

**Problème** : Git non initialisé

```bash
git init
git add .
git commit -m "Commit initial"
```

**Problème** : L'authentification GitHub échoue

- Vérifiez que GitHub MCP est configuré dans Bob
- Vérifiez le token d'accès personnel GitHub
- Essayez un git push manuel pour tester les identifiants

## Ressources supplémentaires

- [Documentation Flask](https://flask.palletsprojects.com/)
- [API Fetch JavaScript](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API)
- [Documentation SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentation Bob](https://bob.ibm.com/docs/ide)

## Retour d'information

Comment s'est passé ce lab ? Nous aimerions connaître votre avis :

- Qu'est-ce qui a bien fonctionné ?
- Qu'est-ce qui était confus ?
- Qu'aimeriez-vous voir ajouté ?

---

**Prêt pour le prochain défi ?** → [Commencer le Lab 2 : Analyse de sécurité](../lab2-refactoring/README.md)

_Dernière mise à jour : Mars 2026_
