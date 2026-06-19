# Exercice 4 : API REST Complète pour Blog

## Description

Cette solution démontre une API REST moderne et complète pour la gestion d'articles de blog, en appliquant **tous les skills et rules** définis dans le lab 8.

## Architecture

L'application suit une **architecture en couches** :

- **Models** : Modèles de domaine (User, Article)
- **Repositories** : Accès aux données (UserRepository, ArticleRepository)
- **Services** : Logique métier (AuthService, ArticleService)
- **Routes** : Endpoints API REST

## Fonctionnalités

### Authentification JWT
- ✅ Inscription utilisateur
- ✅ Connexion avec JWT
- ✅ Protection des endpoints

### Gestion des Articles
- ✅ CRUD complet (Create, Read, Update, Delete)
- ✅ Pagination
- ✅ Autorisation (seul l'auteur peut modifier/supprimer)
- ✅ Validation des données avec Pydantic

### Sécurité
- ✅ Mots de passe hashés avec bcrypt
- ✅ JWT avec expiration
- ✅ CORS configuré
- ✅ Validation stricte des entrées
- ✅ Gestion d'erreurs complète

### Documentation
- ✅ OpenAPI/Swagger automatique
- ✅ Docstrings Google style
- ✅ Type hints partout

### Tests
- ✅ Tests unitaires et d'intégration
- ✅ Couverture > 80%
- ✅ Tests d'authentification
- ✅ Tests d'autorisation

## Installation

```bash
# Installer les dépendances
pip install -r requirements.txt

# Copier le fichier d'environnement
cp .env.example .env
```

## Utilisation

### Lancer l'API

```bash
python blog_api.py
```

L'API sera disponible sur `http://localhost:8000`

### Documentation

- Swagger UI : `http://localhost:8000/docs`
- ReDoc : `http://localhost:8000/redoc`

### Lancer les Tests

```bash
# Tous les tests
pytest test_blog_api.py -v

# Avec couverture
pytest test_blog_api.py --cov=blog_api --cov-report=html
```

## Exemples d'Utilisation

### 1. Inscription

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "email": "john@example.com",
    "password": "password123"
  }'
```

### 2. Connexion

```bash
curl -X POST "http://localhost:8000/api/v1/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john&password=password123"
```

### 3. Créer un Article

```bash
curl -X POST "http://localhost:8000/api/v1/articles" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mon Premier Article",
    "content": "Contenu de l'article...",
    "published": true
  }'
```

### 4. Lister les Articles

```bash
curl "http://localhost:8000/api/v1/articles?skip=0&limit=10"
```

### 5. Mettre à Jour un Article

```bash
curl -X PUT "http://localhost:8000/api/v1/articles/1" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Titre Mis à Jour",
    "published": true
  }'
```

### 6. Supprimer un Article

```bash
curl -X DELETE "http://localhost:8000/api/v1/articles/1" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Skills et Rules Appliqués

### Skills Utilisés

1. **python-style.md** (Exercice 1)
   - PEP 8, type hints, docstrings Google style
   - Black formatting, Ruff linting

2. **tdd-workflow.md** (Exercice 3)
   - Tests écrits en premier
   - Couverture > 80%
   - Red-Green-Refactor

3. **api-development.md** (Exercice 4)
   - Standards REST
   - Validation Pydantic
   - Documentation OpenAPI
   - Gestion d'erreurs

4. **security.md** (Exercice 4)
   - JWT authentication
   - Password hashing
   - Input validation
   - CORS configuration

### Rules Appliquées

1. **01-architecture.md** (Exercice 2)
   - Architecture en couches
   - Séparation des responsabilités
   - Repository pattern

2. **02-conventions.md** (Exercice 2)
   - PascalCase pour les classes
   - snake_case pour les fonctions
   - UPPER_SNAKE_CASE pour les constantes

3. **03-bonnes-pratiques.md** (Exercice 2)
   - Validation des entrées
   - Exceptions personnalisées
   - Logging avec contexte
   - Pas de secrets en dur

4. **04-api-standards.md** (Exercice 4)
   - Versioning `/api/v1/`
   - Codes HTTP appropriés
   - Pagination
   - Documentation complète

## Structure du Code

```
ex4-workflow-complet/
├── .bob/
│   ├── skills/
│   │   ├── api-development.md
│   │   └── security.md
│   └── rules/
│       └── 04-api-standards.md
├── app/
│   ├── __init__.py
│   └── config.py
├── blog_api.py              # API complète (704 lignes)
├── test_blog_api.py         # Tests complets (349 lignes)
├── requirements.txt         # Dépendances
├── .env.example            # Configuration exemple
└── README.md               # Ce fichier
```

## Points Clés

### Architecture en Couches

```python
Models (Domain)
    ↓
Repositories (Data Access)
    ↓
Services (Business Logic)
    ↓
Routes (API Endpoints)
```

### Sécurité

- ✅ Mots de passe **jamais en clair**
- ✅ JWT avec **expiration**
- ✅ **Validation stricte** des entrées
- ✅ **Autorisation** vérifiée (seul l'auteur peut modifier)
- ✅ **Logging** des événements de sécurité

### Qualité du Code

- ✅ **Type hints** partout
- ✅ **Docstrings** Google style
- ✅ **Tests** unitaires et d'intégration
- ✅ **Couverture** > 80%
- ✅ **Logging** structuré

## Améliorations Possibles

Pour aller plus loin, vous pourriez ajouter :

1. **Base de données réelle** : PostgreSQL avec SQLAlchemy
2. **Cache** : Redis pour les articles fréquents
3. **Rate limiting** : Protection contre les abus
4. **Migrations** : Alembic pour la base de données
5. **CI/CD** : GitHub Actions pour les tests automatiques
6. **Monitoring** : Prometheus + Grafana
7. **Containerisation** : Docker + Docker Compose

## Conclusion

Cette solution démontre une API REST **professionnelle** qui :

- Suit les **meilleures pratiques** de l'industrie
- Applique **tous les skills et rules** du lab
- Est **testée** et **documentée**
- Est **sécurisée** et **maintenable**
- Peut servir de **template** pour vos projets

🎉 **Bravo ! Vous maîtrisez maintenant la création d'API REST avec Bob !**