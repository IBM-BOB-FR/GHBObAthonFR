# Règles du Projet - API de Gestion de Bibliothèque

## 📋 Vue d'Ensemble du Projet

Ce projet est une API REST pour gérer une bibliothèque en ligne. Il permet de gérer des livres, des auteurs, des utilisateurs et des emprunts.

## 🏗️ Architecture

### Stack Technique

- **Backend** : FastAPI (Python 3.11+)
- **Base de données** : PostgreSQL 15
- **Cache** : Redis
- **ORM** : SQLAlchemy 2.0
- **Migration** : Alembic
- **Tests** : pytest
- **Documentation** : OpenAPI/Swagger

### Architecture en Couches

Le projet suit une architecture en couches stricte :

```
Présentation (Routes) → Services (Logique Métier) → Repositories (Données) → Database
```

**Règles strictes** :
- Les routes ne contiennent QUE la validation et l'appel aux services
- Les services contiennent TOUTE la logique métier
- Les repositories sont les SEULS à accéder à la base de données
- Aucune couche ne peut sauter une autre couche

### Structure des Dossiers

```
app/
├── main.py                 # Point d'entrée
├── config.py              # Configuration centralisée
├── dependencies.py        # Dépendances FastAPI
├── models/                # Modèles Pydantic (Request/Response)
├── routes/                # Endpoints API
├── services/              # Logique métier
├── repositories/          # Accès aux données
├── database/              # Configuration DB et modèles SQLAlchemy
├── utils/                 # Utilitaires (security, logging, etc.)
└── tests/                 # Tests
```

## 📝 Conventions de Code

### Nommage

- **Fichiers** : `snake_case.py` (ex: `book_service.py`)
- **Classes** : `PascalCase` (ex: `BookService`, `UserRepository`)
- **Fonctions/Méthodes** : `snake_case` (ex: `get_book_by_id`, `create_user`)
- **Constantes** : `UPPER_SNAKE_CASE` (ex: `MAX_BOOKS_PER_USER`)
- **Variables privées** : `_leading_underscore` (ex: `_internal_cache`)

### Modèles Pydantic

- **Request models** : Suffixe `Create`, `Update` (ex: `BookCreate`, `BookUpdate`)
- **Response models** : Suffixe `Response` ou `Out` (ex: `BookResponse`, `BookOut`)
- **Base models** : Suffixe `Base` pour les champs communs (ex: `BookBase`)

Exemple :
```python
class BookBase(BaseModel):
    title: str
    isbn: str

class BookCreate(BookBase):
    author_id: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    isbn: Optional[str] = None

class BookResponse(BookBase):
    id: int
    author: AuthorResponse
    created_at: datetime
```

### Type Hints

- **OBLIGATOIRE** sur toutes les fonctions et méthodes
- Utiliser `Optional[T]` pour les valeurs nullables
- Utiliser `List[T]`, `Dict[K, V]` pour les collections
- Utiliser `Union[T1, T2]` pour les types multiples

### Documentation

- **Docstrings Google style** pour toutes les fonctions publiques
- Documenter les paramètres, retours et exceptions
- Ajouter des exemples pour les cas complexes

Exemple :
```python
def get_book_by_id(book_id: int) -> Optional[Book]:
    """Récupère un livre par son ID.
    
    Args:
        book_id: L'identifiant unique du livre
        
    Returns:
        Le livre trouvé ou None si non trouvé
        
    Raises:
        DatabaseError: Si une erreur de base de données survient
        
    Example:
        >>> book = get_book_by_id(123)
        >>> print(book.title)
        "Le Petit Prince"
    """
```

## 🔒 Sécurité

### Authentification

- Utiliser JWT (JSON Web Tokens)
- Tokens valides pendant 24 heures
- Refresh tokens valides pendant 7 jours
- Hasher les mots de passe avec bcrypt (12 rounds minimum)

### Autorisation

Trois rôles :
- **USER** : Peut emprunter des livres, voir son profil
- **LIBRARIAN** : Peut gérer les livres et les emprunts
- **ADMIN** : Accès complet

### Validation

- **TOUJOURS** valider les entrées utilisateur
- Utiliser Pydantic pour la validation automatique
- Ajouter des validations métier dans les services
- Ne JAMAIS faire confiance aux données externes

### Secrets

- **JAMAIS** de secrets en dur dans le code
- Utiliser des variables d'environnement
- Utiliser `.env` pour le développement (dans .gitignore)
- Utiliser des secrets managers en production

## 🧪 Tests

### Couverture

- **Minimum 80%** de couverture de code
- **100%** pour les services critiques (authentification, paiement)

### Organisation

```
tests/
├── unit/              # Tests unitaires (services, utils)
├── integration/       # Tests d'intégration (repositories)
└── e2e/              # Tests end-to-end (API complète)
```

### Conventions

- Un fichier de test par module : `test_book_service.py`
- Une classe de test par classe testée : `TestBookService`
- Noms descriptifs : `test_should_return_book_when_id_exists`
- Utiliser des fixtures pour le setup
- Mocker les dépendances externes (DB, API tierces)

### Fixtures

Créer des fixtures réutilisables :
```python
@pytest.fixture
def sample_book():
    return Book(
        id=1,
        title="Test Book",
        isbn="978-0-123456-78-9"
    )
```

## 📊 Base de Données

### Migrations

- **TOUJOURS** créer une migration pour les changements de schéma
- Tester les migrations up ET down
- Nommer les migrations de façon descriptive : `add_book_rating_column`

### Requêtes

- Utiliser SQLAlchemy ORM (pas de SQL brut)
- Optimiser les requêtes N+1 avec `joinedload()` ou `selectinload()`
- Utiliser des index pour les colonnes fréquemment recherchées
- Paginer les résultats (max 100 items par page)

### Transactions

- Utiliser des transactions pour les opérations multiples
- Rollback en cas d'erreur
- Utiliser des context managers pour la gestion automatique

## 🚀 Performance

### Caching

- Cacher les données fréquemment lues et rarement modifiées
- Utiliser Redis pour le cache
- TTL approprié selon les données (ex: 5 min pour les livres populaires)
- Invalider le cache lors des modifications

### Async/Await

- Utiliser `async/await` pour toutes les opérations I/O
- Ne PAS bloquer l'event loop
- Utiliser `asyncio.gather()` pour les opérations parallèles

### Pagination

- Toujours paginer les listes
- Paramètres : `skip` (offset) et `limit` (max 100)
- Retourner le total dans les métadonnées

## 📝 Logging

### Niveaux

- **DEBUG** : Informations de développement
- **INFO** : Événements normaux (création, modification)
- **WARNING** : Situations anormales mais gérées
- **ERROR** : Erreurs nécessitant attention
- **CRITICAL** : Erreurs critiques (système down)

### Format

```python
logger.info(
    "Book borrowed",
    extra={
        "user_id": user.id,
        "book_id": book.id,
        "action": "borrow"
    }
)
```

### Ce qu'il faut logger

- Toutes les erreurs avec le contexte complet
- Les actions importantes (création, modification, suppression)
- Les tentatives d'accès non autorisé
- Les performances anormales

## ❌ Ce qu'il faut ÉVITER

### Anti-Patterns

- ❌ Logique métier dans les routes
- ❌ Accès direct à la DB depuis les routes
- ❌ Modèles SQLAlchemy exposés dans les réponses API
- ❌ Exceptions non gérées
- ❌ Secrets en dur
- ❌ SQL brut (sauf cas très spécifiques)
- ❌ Opérations synchrones bloquantes
- ❌ Code dupliqué

### Mauvaises Pratiques

- ❌ `except:` sans spécifier l'exception
- ❌ `print()` pour le debug (utiliser logging)
- ❌ Variables globales mutables
- ❌ Imports circulaires
- ❌ Fonctions de plus de 50 lignes
- ❌ Classes avec plus de 10 méthodes publiques

## ✅ Checklist Avant Commit

- [ ] Code formaté avec Black
- [ ] Pas d'erreurs de linting (Ruff)
- [ ] Type hints vérifiés (mypy)
- [ ] Tests passent (pytest)
- [ ] Couverture >= 80%
- [ ] Documentation à jour
- [ ] Pas de secrets en dur
- [ ] Migrations créées si nécessaire

## 🔄 Workflow de Développement

1. **Créer une branche** : `feature/nom-de-la-feature`
2. **Écrire les tests** (TDD)
3. **Implémenter la fonctionnalité**
4. **Vérifier la checklist**
5. **Créer une Pull Request**
6. **Code review** par au moins 1 personne
7. **Merge** après approbation

## 📚 Ressources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [pytest Documentation](https://docs.pytest.org/)

---

**Note** : Ces règles sont vivantes et peuvent évoluer. Proposez des améliorations via des Pull Requests sur ce fichier.