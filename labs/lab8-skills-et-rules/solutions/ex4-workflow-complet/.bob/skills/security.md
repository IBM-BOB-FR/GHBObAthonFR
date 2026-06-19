# Security Best Practices

Bonnes pratiques de sécurité pour les applications web et API.

## Authentification

### JWT (JSON Web Tokens)

- Utiliser des tokens JWT pour l'authentification stateless
- Durée de vie limitée (15-30 minutes pour access token)
- Refresh tokens pour renouveler les sessions
- Stocker les secrets de manière sécurisée

### Exemple

```python
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "your-secret-key"  # À stocker dans les variables d'environnement
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

## Validation des Entrées

### Principes

- **Toujours valider** les entrées utilisateur
- **Whitelist** plutôt que blacklist
- **Sanitize** les données avant utilisation
- **Limiter** la taille des entrées

### Protection contre les Injections

```python
from pydantic import BaseModel, Field, validator

class ArticleCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1, max_length=10000)
    
    @validator('title', 'content')
    def sanitize_html(cls, v):
        # Supprimer les balises HTML dangereuses
        import bleach
        return bleach.clean(v)
```

## Protection des Données Sensibles

### Mots de Passe

- **Jamais en clair** : Toujours hasher
- **Utiliser bcrypt** ou argon2
- **Salt automatique** avec bcrypt
- **Politique de complexité** : longueur minimale, caractères variés

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
```

### Données Personnelles

- **Chiffrement** des données sensibles au repos
- **HTTPS** obligatoire pour les communications
- **Pas de logs** des données sensibles
- **Conformité RGPD** : droit à l'oubli, portabilité

## Autorisation

### Contrôle d'Accès

- **Principe du moindre privilège**
- **Vérifier les permissions** à chaque requête
- **Séparer** authentification et autorisation
- **RBAC** (Role-Based Access Control) ou **ABAC** (Attribute-Based)

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

async def require_admin(current_user: str = Depends(get_current_user)):
    if not is_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
```

## Protection contre les Vulnérabilités Courantes

### OWASP Top 10

1. **Injection** : Utiliser des requêtes paramétrées (ORM)
2. **Broken Authentication** : JWT avec expiration, MFA
3. **Sensitive Data Exposure** : Chiffrement, HTTPS
4. **XML External Entities (XXE)** : Désactiver les entités externes
5. **Broken Access Control** : Vérifier les permissions
6. **Security Misconfiguration** : Configuration sécurisée par défaut
7. **XSS** : Sanitize les entrées, CSP headers
8. **Insecure Deserialization** : Valider avant désérialisation
9. **Using Components with Known Vulnerabilities** : Mises à jour régulières
10. **Insufficient Logging & Monitoring** : Logs de sécurité

### CSRF Protection

```python
from fastapi.middleware.csrf import CSRFMiddleware

app.add_middleware(CSRFMiddleware, secret="your-csrf-secret")
```

### CORS Configuration

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Pas de wildcard en production
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

### Rate Limiting

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/api/resource")
@limiter.limit("5/minute")
async def get_resource(request: Request):
    pass
```

## Gestion des Secrets

### Variables d'Environnement

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    jwt_secret: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```

### Bonnes Pratiques

- **Jamais dans le code** : Utiliser des variables d'environnement
- **Fichier .env** : Ajouter au .gitignore
- **Rotation** : Changer régulièrement les secrets
- **Vault** : Utiliser un gestionnaire de secrets (HashiCorp Vault, AWS Secrets Manager)

## Logging et Monitoring

### Logs de Sécurité

```python
import logging

security_logger = logging.getLogger("security")

def log_security_event(event_type: str, user: str, details: dict):
    security_logger.warning(
        f"Security event: {event_type}",
        extra={
            "user": user,
            "event": event_type,
            "details": details,
            "timestamp": datetime.utcnow().isoformat()
        }
    )
```

### Événements à Logger

- Tentatives de connexion échouées
- Accès non autorisés
- Modifications de données sensibles
- Changements de permissions
- Erreurs d'authentification

## Headers de Sécurité

```python
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# Force HTTPS
app.add_middleware(HTTPSRedirectMiddleware)

# Trusted hosts
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["yourdomain.com", "*.yourdomain.com"]
)

# Security headers
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response
```

## Checklist de Sécurité

- [ ] Authentification JWT implémentée
- [ ] Mots de passe hashés avec bcrypt
- [ ] Validation des entrées avec Pydantic
- [ ] HTTPS activé
- [ ] CORS configuré correctement
- [ ] Rate limiting en place
- [ ] Headers de sécurité configurés
- [ ] Logs de sécurité actifs
- [ ] Secrets dans variables d'environnement
- [ ] Tests de sécurité automatisés
- [ ] Dépendances à jour
- [ ] Protection CSRF activée
- [ ] Principe du moindre privilège appliqué