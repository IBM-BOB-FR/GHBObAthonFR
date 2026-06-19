# Standards API REST

Standards spécifiques pour le développement d'API REST dans ce projet.

## Stack Technique

### Backend
- **Framework** : FastAPI 0.109+
- **Base de données** : PostgreSQL 15+
- **ORM** : SQLAlchemy 2.0+
- **Cache** : Redis 7+
- **Validation** : Pydantic 2.0+

### Authentification
- **Méthode** : JWT (JSON Web Tokens)
- **Librairie** : python-jose
- **Hash** : bcrypt via passlib

### Tests
- **Framework** : pytest
- **Coverage** : pytest-cov (minimum 80%)
- **API Testing** : httpx (client async)

## Structure du Projet

```
project/
├── app/
│   ├── __init__.py
│   ├── main.py              # Point d'entrée FastAPI
│   ├── config.py            # Configuration (Pydantic Settings)
│   ├── dependencies.py      # Dépendances FastAPI
│   ├── models/              # Modèles SQLAlchemy
│   │   ├── __init__.py
│   │   └── article.py
│   ├── schemas/             # Schémas Pydantic
│   │   ├── __init__.py
│   │   └── article.py
│   ├── repositories/        # Couche d'accès aux données
│   │   ├── __init__.py
│   │   └── article_repository.py
│   ├── services/            # Logique métier
│   │   ├── __init__.py
│   │   └── article_service.py
│   ├── routers/             # Routes API
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── articles.py
│   └── utils/               # Utilitaires
│       ├── __init__.py
│       ├── security.py
│       └── logging.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   └── integration/
├── alembic/                 # Migrations de base de données
├── .env.example
├── requirements.txt
└── README.md
```

## Conventions d'API

### Versioning
- Préfixe : `/api/v1/`
- Exemple : `/api/v1/articles`

### Endpoints Standards

```
GET    /api/v1/articles           # Liste paginée
GET    /api/v1/articles/{id}      # Détail
POST   /api/v1/articles           # Création (auth requise)
PUT    /api/v1/articles/{id}      # Mise à jour (auth requise)
DELETE /api/v1/articles/{id}      # Suppression (auth requise)
```

### Pagination

```python
GET /api/v1/articles?skip=0&limit=10

Response:
{
    "items": [...],
    "total": 100,
    "skip": 0,
    "limit": 10
}
```

### Filtrage et Tri

```python
GET /api/v1/articles?author=john&sort=-created_at
```

## Schémas de Réponse

### Succès

```json
{
    "id": 1,
    "title": "Mon article",
    "content": "Contenu...",
    "author_id": 1,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
}
```

### Erreur

```json
{
    "detail": "Article not found",
    "error_code": "ARTICLE_NOT_FOUND",
    "status_code": 404
}
```

### Erreur de Validation

```json
{
    "detail": [
        {
            "loc": ["body", "title"],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```

## Authentification

### Login

```
POST /api/v1/auth/login
Content-Type: application/json

{
    "username": "user@example.com",
    "password": "password123"
}

Response:
{
    "access_token": "eyJ...",
    "token_type": "bearer",
    "expires_in": 1800
}
```

### Utilisation du Token

```
GET /api/v1/articles
Authorization: Bearer eyJ...
```

## Documentation

### OpenAPI/Swagger

- Accessible à `/docs` (Swagger UI)
- Accessible à `/redoc` (ReDoc)
- Schéma JSON à `/openapi.json`

### Descriptions Requises

```python
@router.post(
    "/articles",
    response_model=ArticleResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Articles"],
    summary="Create a new article",
    description="Create a new blog article with title, content, and author information",
    responses={
        201: {"description": "Article created successfully"},
        400: {"description": "Invalid input data"},
        401: {"description": "Authentication required"},
    }
)
```

## Processus de Review

### Avant le Merge

1. **Tests** : Tous les tests passent (unitaires + intégration)
2. **Coverage** : Minimum 80% de couverture
3. **Linting** : Ruff sans erreurs
4. **Formatting** : Black appliqué
5. **Type Checking** : mypy sans erreurs
6. **Documentation** : OpenAPI à jour
7. **Security** : Pas de secrets en dur
8. **Performance** : Pas de N+1 queries

### Checklist PR

- [ ] Tests ajoutés/mis à jour
- [ ] Documentation mise à jour
- [ ] Migrations de base de données (si nécessaire)
- [ ] Variables d'environnement documentées
- [ ] Logs appropriés ajoutés
- [ ] Gestion d'erreurs complète
- [ ] Validation des entrées
- [ ] Autorisation vérifiée

## Performance

### Optimisations Requises

- **Eager Loading** : Utiliser `joinedload()` pour éviter N+1
- **Indexation** : Index sur les colonnes fréquemment recherchées
- **Caching** : Redis pour les données fréquentes
- **Pagination** : Toujours paginer les listes
- **Compression** : Gzip pour les réponses > 1KB

### Exemple

```python
# Bon : Eager loading
articles = db.query(Article).options(
    joinedload(Article.author)
).all()

# Mauvais : N+1 queries
articles = db.query(Article).all()
for article in articles:
    print(article.author.name)  # Query pour chaque article
```

## Monitoring

### Métriques à Tracker

- Temps de réponse par endpoint
- Taux d'erreur (4xx, 5xx)
- Nombre de requêtes par minute
- Utilisation CPU/Mémoire
- Connexions base de données

### Logging

```python
import logging

logger = logging.getLogger(__name__)

logger.info(
    "Article created",
    extra={
        "article_id": article.id,
        "user_id": current_user.id,
        "action": "create_article"
    }
)
```

## Sécurité

### Obligatoire

- HTTPS en production
- CORS configuré (pas de wildcard)
- Rate limiting (100 req/min par IP)
- JWT avec expiration (30 min)
- Validation stricte des entrées
- Pas de données sensibles dans les logs
- Headers de sécurité configurés

### Interdit

- Secrets en dur dans le code
- SQL brut (utiliser l'ORM)
- Désactivation de la validation
- Wildcard CORS en production
- Logs de mots de passe
- Tokens sans expiration