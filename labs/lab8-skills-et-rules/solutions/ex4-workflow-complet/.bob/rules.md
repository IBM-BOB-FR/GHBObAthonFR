# Règles du Projet - API de Gestion d'Articles de Blog

## 📋 Vue d'Ensemble

API REST pour gérer des articles de blog avec authentification JWT et validation des données.

## 🏗️ Architecture

### Stack Technique
- **Backend** : FastAPI + Python 3.11
- **Database** : PostgreSQL
- **Cache** : Redis
- **ORM** : SQLAlchemy

### Architecture en Couches

```
Routes (API) → Services (Business Logic) → Repositories (Data Access) → Database
```

**Règles strictes** :
1. Les routes ne font QUE valider et appeler les services
2. Les services contiennent TOUTE la logique métier
3. Les repositories sont les SEULS à accéder à la DB

## 📝 Conventions de Code

### Nommage
- **Fichiers** : `snake_case.py` (ex: `article_service.py`)
- **Classes** : `PascalCase` (ex: `ArticleService`)
- **Fonctions** : `snake_case` (ex: `get_article_by_id`)
- **Constantes** : `UPPER_SNAKE_CASE` (ex: `MAX_ARTICLES_PER_PAGE`)

### Modèles Pydantic
- **Request** : Suffixe `Create`, `Update` (ex: `ArticleCreate`)
- **Response** : Suffixe `Response` (ex: `ArticleResponse`)
- **Base** : Suffixe `Base` pour champs communs (ex: `ArticleBase`)

## 🔒 Sécurité

### Authentification
- JWT avec expiration 1 heure
- Refresh tokens (7 jours)
- Bcrypt pour les mots de passe (12 rounds minimum)

### Validation
- Valider TOUTES les entrées avec Pydantic
- Sanitizer les contenus d'articles (XSS)
- Limiter la taille des uploads

## 🧪 Tests

### Couverture Minimale
- **Services** : 90%
- **Repositories** : 80%
- **Routes** : 70%
- **Global** : 80%

## 📊 Performance

### Caching
- Articles populaires : Cache 5 minutes
- Liste d'articles : Cache 2 minutes
- Profils utilisateurs : Cache 10 minutes

### Optimisations
- Pagination obligatoire (max 50 items)
- Eager loading pour éviter N+1
- Index sur : article_id, user_id, created_at

## ❌ Ce qu'il faut ÉVITER

- ❌ Logique métier dans les routes
- ❌ Accès direct à la DB depuis les routes
- ❌ Exposer les modèles SQLAlchemy dans les réponses
- ❌ Secrets en dur dans le code
- ❌ print() pour le debug (utiliser logging)

## ✅ Checklist Avant Commit

- [ ] Code formaté avec Black
- [ ] Pas d'erreurs de linting (Ruff)
- [ ] Type hints vérifiés (mypy)
- [ ] Tests passent (pytest)
- [ ] Couverture >= 80%
- [ ] Documentation à jour