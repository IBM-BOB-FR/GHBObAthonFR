# API Development Standards

Standards et bonnes pratiques pour le développement d'API REST.

## Framework

- **Framework** : FastAPI
- **Version** : 0.109+
- **Documentation** : OpenAPI/Swagger automatique

## Architecture REST

### Principes

- Utiliser les verbes HTTP appropriés (GET, POST, PUT, DELETE)
- Codes de statut HTTP corrects
- URLs RESTful et cohérentes
- Versioning de l'API (v1, v2, etc.)

### Structure des URLs

```
GET    /api/v1/resources          # Liste
GET    /api/v1/resources/{id}     # Détail
POST   /api/v1/resources          # Création
PUT    /api/v1/resources/{id}     # Mise à jour complète
PATCH  /api/v1/resources/{id}     # Mise à jour partielle
DELETE /api/v1/resources/{id}     # Suppression
```

## Validation des Données

### Utiliser Pydantic

- Modèles Pydantic pour toutes les requêtes/réponses
- Validation automatique des types
- Documentation automatique des schémas
- Messages d'erreur clairs

### Exemple

```python
from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(..., ge=0, le=150)
```

## Gestion des Erreurs

### Codes de Statut

- `200 OK` : Succès
- `201 Created` : Ressource créée
- `204 No Content` : Succès sans contenu
- `400 Bad Request` : Erreur de validation
- `401 Unauthorized` : Non authentifié
- `403 Forbidden` : Non autorisé
- `404 Not Found` : Ressource non trouvée
- `500 Internal Server Error` : Erreur serveur

### Format des Erreurs

```python
{
    "detail": "Description de l'erreur",
    "error_code": "VALIDATION_ERROR",
    "field": "email"
}
```

## Documentation

### OpenAPI/Swagger

- Descriptions claires pour chaque endpoint
- Exemples de requêtes/réponses
- Tags pour organiser les endpoints
- Schémas de sécurité documentés

### Exemple

```python
@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    summary="Create a new user",
    description="Create a new user with the provided information",
)
async def create_user(user: UserCreate) -> UserResponse:
    """Create a new user."""
    pass
```

## Performance

### Async/Await

- Utiliser `async def` pour les opérations I/O
- Await pour les appels base de données
- Await pour les appels API externes

### Pagination

```python
@app.get("/items")
async def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    pass
```

## Tests

### Types de Tests

- Tests unitaires pour la logique métier
- Tests d'intégration pour les endpoints
- Tests de validation des schémas
- Tests de sécurité

### Exemple avec pytest

```python
def test_create_user(client):
    response = client.post(
        "/users",
        json={"name": "John", "email": "john@example.com", "age": 30}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "John"
```

## Bonnes Pratiques

1. **Injection de dépendances** : Utiliser FastAPI Depends
2. **Middleware** : Pour logging, CORS, authentification
3. **Configuration** : Variables d'environnement avec Pydantic Settings
4. **Logging** : Structuré avec contexte
5. **Rate Limiting** : Protection contre les abus
6. **CORS** : Configuration appropriée pour les clients web
7. **Compression** : Gzip pour les réponses volumineuses
8. **Caching** : Redis ou similaire pour les données fréquentes