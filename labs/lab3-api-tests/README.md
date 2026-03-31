# 🌐 Lab 3 : Création d'API et Tests

> **Durée estimée** : 75-90 minutes  
> **Difficulté** : ⭐⭐⭐ Avancé  
> **Objectif** : Créer des APIs REST professionnelles avec tests complets

---

## 📋 Objectifs d'Apprentissage

À la fin de ce lab, vous serez capable de :

- ✅ Créer une API REST avec Flask ou FastAPI
- ✅ Implémenter les opérations CRUD
- ✅ Ajouter l'authentification et l'autorisation
- ✅ Écrire des tests d'API complets
- ✅ Documenter automatiquement l'API
- ✅ Gérer les erreurs et la validation

---

## 🚀 Mise en Place

### Prérequis

- Avoir complété les Labs 0, 1 et 1 bis
- Python 3.8+ installé
- Connaissances de base en HTTP et REST
- Disposer de l'utilitaire `curl`
- Environnement virtuel Python activé (`.venv` à la racine du projet)

### Installation des Dépendances

```bash
# Activer l'environnement virtuel (à la racine du projet)
# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat

# Installer les dépendances
pip install -r labs/lab3-api-tests/requirements.txt
```

**Contenu de requirements.txt** :

```txt
# API Framework
flask==3.1.0
flask-cors==5.0.0

# Authentication
flask-jwt-extended==4.7.1
werkzeug==3.1.3

# Testing
pytest==8.3.4
pytest-cov==6.0.0
requests==2.32.3

# Documentation (Exercice 4)
flasgger==0.9.7.1
```

---

## 📝 Exercice 1 : API de Base (20 min)

### Objectif

Créer une API REST simple pour gérer des tâches (TODO list).

### Instructions

1. **Créez la structure de base** :

   ```
   Crée une API Flask dans api/ avec :
   - app.py : Configuration de l'application
   - models.py : Modèle Task avec id, title, description, completed, created_at
   - routes.py : Routes CRUD pour les tâches
   - __init__.py : Initialisation du package
   ```

2. **Implémentez les endpoints** :

   ```
   Implémente ces endpoints dans routes.py :
   - GET /tasks : Liste toutes les tâches
   - GET /tasks/<id> : Récupère une tâche
   - POST /tasks : Crée une nouvelle tâche
   - PUT /tasks/<id> : Met à jour une tâche
   - DELETE /tasks/<id> : Supprime une tâche
   ```

   **Structure de Stockage** :

   ```python
   # Utilise ces variables globales dans routes.py
   tasks_storage: List[Task] = []
   next_task_id = 1
   ```

   💡 **Note importante** : Dans l'Exercice 2, il vous sera demandé d'ajouter l'authentification. Il est donc préférable de prévoir un champ `user_id` dans le modèle Task dès maintenant (peut être None pour l'instant).

3. **Ajoutez la validation** :

   ```
   Ajoute la validation des données :
   - title : requis, 1-100 caractères
   - description : optionnel, max 500 caractères
   - completed : booléen, défaut False

   Retourne des erreurs 400 avec des messages clairs.
   ```

   **Exemples de messages d'erreur** :

   ```python
   # Titre vide
   {"error": "Title is required"}

   # Titre trop long
   {"error": "Title must be between 1 and 100 characters"}

   # Description trop longue
   {"error": "Description must not exceed 500 characters"}
   ```

4. **Testez manuellement** :
   ```
   Démarre le serveur et teste les endpoints avec curl ou Postman.
   ```

### ⚠️ Note sur Content-Type

Flask retourne 415 (Unsupported Media Type) si le header `Content-Type: application/json` est manquant.

Vous pouvez demander à Bob d'en tenir compte :
```
Dans tes requêtes, assures toi d'inclure ce header :

curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Test"}'

Ou ajoutes un gestionnaire d'erreur dans `app.py` :

@app.errorhandler(415)
def unsupported_media_type(error):
    return jsonify({'error': 'Content-Type must be application/json'}), 400
```

### ✅ Critères de Validation

- [ ] Tous les endpoints CRUD fonctionnent
- [ ] Validation des données en place
- [ ] Codes de statut HTTP appropriés (200, 201, 400, 404)
- [ ] Réponses JSON bien formatées

### 💡 Exemple de Requête

```bash
# Créer une tâche
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Apprendre Bob", "description": "Compléter tous les labs"}'

# Lister les tâches
curl http://localhost:5000/tasks
```

---

## 🔐 Exercice 2 : Authentification JWT (20 min)

### Objectif

Ajouter l'authentification avec JWT (JSON Web Tokens).

### Instructions

1. **Créez le système d'authentification** :

   ```
   Crée api/auth.py avec :
   - Modèle User (username, password_hash, email)
   - Fonction de hachage de mot de passe (bcrypt)
   - Génération et validation de JWT
   ```

   **Configuration JWT Requise** :

   ```
   Ajoute cette configuration dans `app.py` :
   
   from datetime import timedelta
   from flask_jwt_extended import JWTManager

   app.config['JWT_SECRET_KEY'] = 'dev-secret-key-change-in-production'
   app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
   app.config['JWT_TOKEN_LOCATION'] = ['headers']
   app.config['JWT_HEADER_NAME'] = 'Authorization'
   app.config['JWT_HEADER_TYPE'] = 'Bearer'

   jwt = JWTManager(app)

   Et configure les callbacks JWT dans `auth.py`
   ```

   Exemple de configuration pour les callbacks JWT :

   ```python
   
   from flask_jwt_extended import JWTManager

   def init_jwt(app):
       jwt = JWTManager(app)

       @jwt.user_identity_loader
       def user_identity_lookup(user_id):
           return str(user_id)  # Convertir en string pour JWT

       @jwt.user_lookup_loader
       def user_lookup_callback(_jwt_header, jwt_data):
           identity = int(jwt_data["sub"])  # Reconvertir en int
           return get_user_by_id(identity)

       return jwt
   ```

3. **Ajoutez les endpoints d'authentification** :

   ```
   Ajoute ces endpoints :
   - POST /auth/register : Inscription d'un nouvel utilisateur
   - POST /auth/login : Connexion et obtention du token JWT
   - GET /auth/me : Informations de l'utilisateur connecté (protégé)
   ```

4. **Protégez les endpoints de tâches** :

   ```
   Modifie routes.py pour :
   - Exiger un token JWT valide pour toutes les opérations sur les tâches
   - Associer chaque tâche à son créateur (utilise le user_id prévu dans Ex1)
   - Permettre uniquement au créateur de modifier/supprimer ses tâches
   ```

5. **Testez l'authentification** :
   ```
   Teste le flow complet :
   1. Inscription d'un utilisateur
   2. Connexion et récupération du token
   3. Utilisation du token pour créer/modifier des tâches
   4. Vérification que les tâches sont isolées par utilisateur
   ```

### ✅ Critères de Validation

- [ ] Inscription et connexion fonctionnent
- [ ] JWT généré et validé correctement
- [ ] Endpoints protégés refusent les requêtes sans token
- [ ] Isolation des données par utilisateur
- [ ] Mots de passe hachés (jamais en clair)

### 💡 Exemple avec JWT

```bash
# S'inscrire
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "bob", "password": "secret123", "email": "bob@example.com"}'

# Se connecter et extraire le token
TOKEN=$(curl -s -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "bob", "password": "secret123"}' \
  | python3 -c "import sys, json; print(json.load(sys.stdin)['token'])")

# Utiliser le token
curl -X GET http://localhost:5000/tasks \
  -H "Authorization: Bearer $TOKEN"
```

---

## 🧪 Exercice 3 : Tests Automatisés (25 min)

### Objectif

Écrire des tests complets pour l'API.

### Instructions

1. **Configurez pytest** :

   ```
   Crée tests/conftest.py avec :
   - Fixture pour l'application de test
   - Fixture pour le client de test
   - Fixture pour créer des utilisateurs de test
   - Fixture pour obtenir des tokens JWT
   ```

   **Exemples de fixtures essentielles générées** :

   ```python
   # tests/conftest.py
   import pytest
   from api.app import create_app

   @pytest.fixture
   def app():
       """Application Flask de test."""
       app = create_app({'TESTING': True})
       yield app

   @pytest.fixture
   def client(app):
       """Client de test."""
       return app.test_client()

   @pytest.fixture
   def auth_token(client):
       """Token JWT valide."""
       # S'inscrire
       client.post('/auth/register', json={
           'username': 'testuser',
           'password': 'testpass123',
           'email': 'test@example.com'
       })
       # Se connecter
       response = client.post('/auth/login', json={
           'username': 'testuser',
           'password': 'testpass123'
       })
       return response.get_json()['token']

   @pytest.fixture
   def auth_headers(auth_token):
       """Headers d'authentification."""
       return {'Authorization': f'Bearer {auth_token}'}
   ```

2. **Testez les endpoints CRUD** :

   ```
   Crée tests/test_api.py avec des tests pour :
   - Création de tâches (succès et échecs)
   - Récupération de tâches (liste et détail)
   - Mise à jour de tâches
   - Suppression de tâches
   - Validation des données
   - Codes de statut HTTP
   ```

3. **Testez l'authentification** :

   ```
   Crée tests/test_auth.py avec des tests pour :
   - Inscription (succès, utilisateur existant, données invalides)
   - Connexion (succès, mauvais mot de passe, utilisateur inexistant)
   - Accès aux endpoints protégés (avec/sans token, token invalide)
   - Isolation des données entre utilisateurs
   ```

4. **Mesurez la couverture** :

   ```
   Exécute les tests avec couverture :
   pytest --cov=api --cov-report=html

   Vise une couverture > 90%
   ```

### ✅ Critères de Validation

- [ ] Au moins 20 tests écrits
- [ ] Tous les tests passent
- [ ] Couverture de code > 90%
- [ ] Tests des cas d'erreur inclus
- [ ] Tests d'intégration pour les flows complets

### 💡 Exemple de Test

```python
def test_create_task_success(client, auth_token):
    """Test de création d'une tâche avec succès"""
    response = client.post(
        '/tasks',
        json={'title': 'Test Task', 'description': 'Test Description'},
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 201
    assert response.json['title'] == 'Test Task'
    assert 'id' in response.json

def test_create_task_without_auth(client):
    """Test de création sans authentification"""
    response = client.post(
        '/tasks',
        json={'title': 'Test Task'}
    )
    assert response.status_code == 401
```

---

## 📚 Exercice 4 : Documentation et Amélioration (20 min)

### Objectif

Documenter l'API et ajouter des fonctionnalités avancées.

### Instructions

1. **Ajoutez Swagger/OpenAPI** :

   ```
   Intègre flask-swagger-ui ou flasgger pour :
   - Générer automatiquement la documentation
   - Créer une interface interactive
   - Documenter tous les endpoints avec leurs paramètres
   ```

2. **Ajoutez la pagination** :

   ```
   Modifie GET /tasks pour supporter :
   - Paramètre page (défaut: 1)
   - Paramètre per_page (défaut: 10, max: 100)
   - Métadonnées de pagination dans la réponse
   ```

3. **Ajoutez le filtrage et le tri** :

   ```
   Ajoute des paramètres de requête :
   - ?completed=true/false : Filtrer par statut
   - ?sort=created_at/title : Trier par champ
   - ?order=asc/desc : Ordre de tri
   ```

4. **Ajoutez la gestion des erreurs** :

   ```
   Crée un gestionnaire d'erreurs global qui :
   - Capture toutes les exceptions
   - Retourne des réponses JSON cohérentes
   - Log les erreurs pour le debugging
   - Masque les détails sensibles en production
   ```

5. **Créez la documentation** :
   ```
   Crée API_DOCUMENTATION.md avec :
   - Description de l'API
   - Liste de tous les endpoints
   - Exemples de requêtes/réponses
   - Guide d'authentification
   - Codes d'erreur possibles
   ```

### ✅ Critères de Validation

- [ ] Documentation Swagger accessible
- [ ] Pagination fonctionnelle
- [ ] Filtrage et tri opérationnels
- [ ] Gestion d'erreurs robuste
- [ ] Documentation markdown complète

---

## 🎯 Exercice Bonus : Fonctionnalités Avancées (Optionnel)

### Mission

Ajouter des fonctionnalités professionnelles à l'API.

### Instructions

```
Ajoute ces fonctionnalités :

1. Rate Limiting :
   - Limite les requêtes par IP/utilisateur
   - Retourne 429 Too Many Requests si dépassé

2. CORS :
   - Configure CORS pour permettre les requêtes cross-origin
   - Définit les origines autorisées

3. Versioning :
   - Implémente le versioning de l'API (v1, v2)
   - Maintiens la compatibilité ascendante

4. Webhooks :
   - Permet aux utilisateurs de s'abonner à des événements
   - Envoie des notifications lors de la création/modification de tâches

5. Export de données :
   - Endpoint pour exporter toutes les tâches en CSV/JSON
   - Génération de rapports

6. Tests de performance :
   - Utilise locust ou pytest-benchmark
   - Mesure les temps de réponse
   - Identifie les goulots d'étranglement
```

### ✅ Critères de Validation

- [ ] Au moins 3 fonctionnalités bonus implémentées
- [ ] Tests pour les nouvelles fonctionnalités
- [ ] Documentation mise à jour
- [ ] Performance acceptable (< 100ms par requête)

---

## 📊 Auto-Évaluation

Avant de passer au Lab suivant, vérifiez :

- [ ] Je sais créer une API REST complète
- [ ] Je comprends l'authentification JWT
- [ ] Je peux écrire des tests d'API complets
- [ ] Je sais documenter une API
- [ ] Je comprends les bonnes pratiques REST
- [ ] Je me sens à l'aise pour continuer

---

## 🎓 Ce que Vous Avez Appris

### Concepts REST

- ✅ **Endpoints RESTful** : GET, POST, PUT, DELETE
- ✅ **Codes de statut HTTP** : 200, 201, 400, 401, 404, 500
- ✅ **Authentification** : JWT, Bearer tokens
- ✅ **Validation** : Données d'entrée, contraintes

### Tests

- ✅ **Tests unitaires** : Fonctions individuelles
- ✅ **Tests d'intégration** : Flows complets
- ✅ **Fixtures pytest** : Configuration réutilisable
- ✅ **Couverture de code** : Mesure de la qualité

### Bonnes Pratiques

- ✅ **Sécurité** : Hachage de mots de passe, validation
- ✅ **Documentation** : Swagger, README
- ✅ **Gestion d'erreurs** : Messages clairs, logging
- ✅ **Performance** : Pagination, optimisation

---

## 💡 Ressources Complémentaires

- **Documentation Flask** : https://flask.palletsprojects.com
- **Documentation FastAPI** : https://fastapi.tiangolo.com
- **JWT** : https://jwt.io
- **REST Best Practices** : https://restfulapi.net
- **Flask-JWT-Extended** : https://flask-jwt-extended.readthedocs.io/
- **pytest Fixtures Guide** : https://docs.pytest.org/en/stable/fixture.html
- **HTTP Status Codes** : https://httpstatuses.com/

---

## 🔧 Problèmes Courants et Solutions

### Erreur 422 avec JWT

**Problème** : `422 Unprocessable Entity` lors de l'utilisation de JWT.

**Solution** : Instruire à Bob de vérifier que la configuration JWT est complète dans `app.py` (voir Exercice 2).

### Erreur 415 Unsupported Media Type

**Problème** : Flask retourne 415 au lieu de 400.

**Solution** : Instruire à Bob d'ajouter systématiquement le header `Content-Type: application/json` ou de configurer un gestionnaire d'erreur (voir Exercice 1).

### Tests JWT échouent

**Problème** : Les tests d'authentification ne passent pas.

**Solution** : Instruire à Bob de s'assurer que :

- La configuration JWT est présente dans l'app de test
- Les callbacks `user_identity_loader` et `user_lookup_loader` sont configurés
- Le token est bien extrait de la réponse JSON

### Isolation des utilisateurs ne fonctionne pas

**Problème** : Les utilisateurs voient les tâches des autres.

**Solution** : Instruire à Bob de vérifier que :

- Chaque tâche a un `user_id`
- Les routes filtrent par `user_id` de l'utilisateur connecté
- Le décorateur `@jwt_required()` est présent sur toutes les routes protégées

---

_Lab créé pour le Bobathon 2026_
