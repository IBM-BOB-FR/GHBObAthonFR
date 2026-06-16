# 🎯 Exemples Pratiques : Skills et Rules en Action

Ce document présente des exemples concrets d'utilisation des Skills et Rules de Bob dans des situations réelles.

---

## 📚 Table des Matières

1. [Exemple 1 : Skill Python pour un Projet Data Science](#exemple-1--skill-python-pour-un-projet-data-science)
2. [Exemple 2 : Rules pour une API E-commerce](#exemple-2--rules-pour-une-api-e-commerce)
3. [Exemple 3 : Skill + Rules pour un Projet React](#exemple-3--skill--rules-pour-un-projet-react)
4. [Exemple 4 : Workflow TDD avec Skills](#exemple-4--workflow-tdd-avec-skills)
5. [Exemple 5 : Configuration Multi-Projets](#exemple-5--configuration-multi-projets)

---

## Exemple 1 : Skill Python pour un Projet Data Science

### Contexte

Vous travaillez sur un projet de machine learning et voulez standardiser le code Python de l'équipe.

### Skill : `.bob/skills/data-science-python.yaml`

```yaml
name: "Data Science Python Standards"
description: "Standards pour les projets de data science en Python"
version: "1.0.0"
author: "Data Science Team"
tags: ["python", "data-science", "ml"]

# Configuration Python
language: python
python_version: "3.11+"

# Outils
tools:
  formatter: black
  linter: ruff
  type_checker: mypy
  notebook_formatter: nbqa
  test_framework: pytest

# Style
style:
  max_line_length: 100
  docstring_style: "NumPy"
  
# Bibliothèques recommandées
libraries:
  data_manipulation:
    - pandas
    - numpy
    - polars
  visualization:
    - matplotlib
    - seaborn
    - plotly
  ml:
    - scikit-learn
    - xgboost
    - lightgbm
  deep_learning:
    - pytorch
    - tensorflow

# Conventions spécifiques
conventions:
  - "Utiliser pandas pour la manipulation de données"
  - "Préférer numpy pour les calculs numériques"
  - "Documenter les fonctions avec le style NumPy"
  - "Utiliser type hints même pour les notebooks"
  - "Versionner les datasets avec DVC"
  - "Tracker les expériences avec MLflow"

# Structure de projet
project_structure: |
  project/
  ├── data/
  │   ├── raw/           # Données brutes
  │   ├── processed/     # Données traitées
  │   └── external/      # Données externes
  ├── notebooks/         # Jupyter notebooks
  ├── src/
  │   ├── data/         # Scripts de traitement
  │   ├── features/     # Feature engineering
  │   ├── models/       # Modèles ML
  │   └── visualization/ # Visualisations
  ├── tests/            # Tests
  └── models/           # Modèles entraînés

# Bonnes pratiques ML
ml_best_practices:
  - "Séparer train/validation/test dès le début"
  - "Fixer les random seeds pour la reproductibilité"
  - "Valider les données avant l'entraînement"
  - "Logger les métriques et hyperparamètres"
  - "Versionner les modèles"
  - "Documenter les expériences"

# Ce qu'il faut éviter
avoid:
  - "Modifier les données raw directement"
  - "Entraîner sans validation set"
  - "Oublier de fixer les random seeds"
  - "Ne pas versionner les datasets"
  - "Hardcoder les chemins de fichiers"
```

### Utilisation

```python
# Demande à Bob
"Crée un script de preprocessing pour des données CSV en respectant 
nos standards data science"

# Bob génère automatiquement :
# - Code formaté avec Black
# - Type hints
# - Docstrings NumPy style
# - Gestion des chemins avec pathlib
# - Logging approprié
# - Tests unitaires
```

### Résultat Généré par Bob

```python
"""Module de preprocessing des données.

Ce module contient les fonctions pour nettoyer et transformer
les données brutes en données prêtes pour le ML.
"""

import logging
from pathlib import Path
from typing import Optional

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)


def load_raw_data(filepath: Path) -> pd.DataFrame:
    """Charge les données brutes depuis un fichier CSV.
    
    Parameters
    ----------
    filepath : Path
        Chemin vers le fichier CSV
        
    Returns
    -------
    pd.DataFrame
        DataFrame contenant les données brutes
        
    Raises
    ------
    FileNotFoundError
        Si le fichier n'existe pas
    ValueError
        Si le fichier est vide ou mal formaté
        
    Examples
    --------
    >>> data = load_raw_data(Path("data/raw/dataset.csv"))
    >>> print(data.shape)
    (1000, 10)
    """
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    logger.info(f"Loading data from {filepath}")
    df = pd.read_csv(filepath)
    
    if df.empty:
        raise ValueError("Loaded DataFrame is empty")
    
    logger.info(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    return df


def clean_data(
    df: pd.DataFrame,
    drop_duplicates: bool = True,
    handle_missing: str = "drop"
) -> pd.DataFrame:
    """Nettoie les données en gérant les duplicatas et valeurs manquantes.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame à nettoyer
    drop_duplicates : bool, default=True
        Si True, supprime les lignes dupliquées
    handle_missing : str, default="drop"
        Stratégie pour les valeurs manquantes: "drop", "mean", "median"
        
    Returns
    -------
    pd.DataFrame
        DataFrame nettoyé
        
    Examples
    --------
    >>> df_clean = clean_data(df, handle_missing="mean")
    """
    df_clean = df.copy()
    
    # Supprimer les duplicatas
    if drop_duplicates:
        initial_rows = len(df_clean)
        df_clean = df_clean.drop_duplicates()
        removed = initial_rows - len(df_clean)
        if removed > 0:
            logger.info(f"Removed {removed} duplicate rows")
    
    # Gérer les valeurs manquantes
    if handle_missing == "drop":
        df_clean = df_clean.dropna()
    elif handle_missing == "mean":
        df_clean = df_clean.fillna(df_clean.mean())
    elif handle_missing == "median":
        df_clean = df_clean.fillna(df_clean.median())
    
    logger.info(f"Cleaned data shape: {df_clean.shape}")
    return df_clean


def scale_features(
    df: pd.DataFrame,
    columns: Optional[list[str]] = None
) -> tuple[pd.DataFrame, StandardScaler]:
    """Normalise les features numériques.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les features
    columns : list[str], optional
        Colonnes à normaliser. Si None, normalise toutes les colonnes numériques
        
    Returns
    -------
    tuple[pd.DataFrame, StandardScaler]
        DataFrame avec features normalisées et le scaler utilisé
        
    Examples
    --------
    >>> df_scaled, scaler = scale_features(df, columns=["age", "income"])
    """
    df_scaled = df.copy()
    
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    scaler = StandardScaler()
    df_scaled[columns] = scaler.fit_transform(df[columns])
    
    logger.info(f"Scaled {len(columns)} features")
    return df_scaled, scaler
```

---

## Exemple 2 : Rules pour une API E-commerce

### Contexte

Vous développez une API e-commerce avec FastAPI et voulez documenter les règles du projet.

### Rules : `.bob/rules.md`

```markdown
# Règles du Projet - API E-commerce

## 📋 Contexte

API REST pour une plateforme e-commerce B2C avec :
- Gestion des produits et catégories
- Panier et commandes
- Paiements (Stripe)
- Authentification utilisateurs
- Système de reviews

## 🏗️ Architecture

### Stack Technique
- **Backend** : FastAPI + Python 3.11
- **Database** : PostgreSQL 15
- **Cache** : Redis
- **Queue** : Celery + RabbitMQ
- **Storage** : AWS S3 (images produits)
- **Payment** : Stripe API

### Architecture en Couches

```
Routes (API) → Services (Business Logic) → Repositories (Data Access) → Database
                    ↓
                 Celery Tasks (Async)
```

**Règles strictes** :
1. Les routes ne font QUE valider et appeler les services
2. Les services contiennent TOUTE la logique métier
3. Les repositories sont les SEULS à accéder à la DB
4. Les tâches Celery sont appelées depuis les services

## 💰 Gestion des Paiements

### Règles Critiques

- **JAMAIS** stocker les numéros de carte
- Utiliser Stripe Payment Intents
- Implémenter l'idempotence (idempotency keys)
- Logger TOUS les événements de paiement
- Gérer les webhooks Stripe de façon asynchrone
- Timeout de 30 secondes max pour les appels Stripe

### Workflow de Paiement

1. Client crée une commande → Status: PENDING
2. Service crée un Payment Intent Stripe
3. Client confirme le paiement côté frontend
4. Webhook Stripe notifie le succès/échec
5. Service met à jour la commande → Status: PAID ou FAILED
6. Si PAID, déclencher la préparation (Celery task)

## 🛒 Gestion du Panier

### Règles

- Un panier par utilisateur (session pour les anonymes)
- TTL de 7 jours pour les paniers inactifs
- Vérifier la disponibilité des produits avant checkout
- Recalculer les prix au moment du checkout (pas de confiance client)
- Gérer les codes promo avec validation stricte

### Calcul des Prix

```python
# TOUJOURS recalculer côté serveur
total = sum(item.product.price * item.quantity for item in cart.items)
if cart.promo_code:
    discount = calculate_discount(cart.promo_code, total)
    total -= discount
shipping = calculate_shipping(cart.items, user.address)
total += shipping
```

## 📦 Gestion des Stocks

### Règles Critiques

- Utiliser des transactions DB pour les modifications de stock
- Implémenter le pessimistic locking pour éviter les oversells
- Vérifier le stock AVANT de créer la commande
- Réserver le stock pendant 15 minutes après création commande
- Libérer le stock si paiement échoue ou timeout

### Code Pattern

```python
# TOUJOURS utiliser ce pattern
async with db.begin():  # Transaction
    product = await repo.get_with_lock(product_id)  # Lock
    if product.stock < quantity:
        raise InsufficientStockError()
    product.stock -= quantity
    await repo.save(product)
```

## 🔒 Sécurité

### Authentification

- JWT avec expiration 1 heure
- Refresh tokens (7 jours)
- Rate limiting : 100 req/min par IP
- 2FA optionnel pour les comptes

### Autorisation

Rôles :
- **CUSTOMER** : Acheter, voir ses commandes
- **SELLER** : Gérer ses produits
- **ADMIN** : Accès complet

### Validation

- Valider TOUTES les entrées avec Pydantic
- Sanitizer les descriptions de produits (XSS)
- Limiter la taille des uploads (5MB max)
- Vérifier les types MIME des images

## 📊 Performance

### Caching Strategy

- **Products** : Cache 1 heure (invalidation sur update)
- **Categories** : Cache 24 heures
- **User Cart** : Cache 5 minutes
- **Search Results** : Cache 15 minutes

### Optimisations Requises

- Pagination obligatoire (max 50 items)
- Eager loading pour éviter N+1
- Index sur : product_id, user_id, order_id, created_at
- Compression des réponses API (gzip)

## 🧪 Tests

### Couverture Minimale

- **Services** : 90% (logique critique)
- **Repositories** : 80%
- **Routes** : 70%
- **Global** : 80%

### Tests Obligatoires

- Tous les cas de paiement (succès, échec, timeout)
- Gestion des stocks (race conditions)
- Validation des données
- Authentification et autorisation
- Webhooks Stripe

## 📝 Logging

### Ce qu'il faut logger

- Toutes les transactions financières
- Modifications de stock
- Erreurs de paiement
- Tentatives d'accès non autorisé
- Performances anormales (> 1s)

### Format

```python
logger.info(
    "Order created",
    extra={
        "order_id": order.id,
        "user_id": user.id,
        "total": order.total,
        "items_count": len(order.items)
    }
)
```

## ❌ Ce qu'il faut ABSOLUMENT éviter

- ❌ Stocker des données de carte bancaire
- ❌ Faire confiance aux prix envoyés par le client
- ❌ Modifier le stock sans transaction
- ❌ Exposer les erreurs internes au client
- ❌ Oublier de valider les webhooks Stripe
- ❌ Utiliser des IDs séquentiels (utiliser UUID)
- ❌ Logger les données sensibles (tokens, passwords)

## ✅ Checklist Avant Déploiement

- [ ] Tous les tests passent
- [ ] Couverture >= 80%
- [ ] Pas de secrets en dur
- [ ] Rate limiting configuré
- [ ] Webhooks Stripe testés
- [ ] Monitoring configuré (Sentry)
- [ ] Logs structurés
- [ ] Backup DB configuré
- [ ] SSL/TLS activé
- [ ] CORS configuré correctement
```

### Utilisation

```python
# Demande à Bob
"Crée le service OrderService qui gère la création de commandes 
en respectant nos rules"

# Bob génère automatiquement :
# - Vérification du stock avec transaction
# - Recalcul des prix côté serveur
# - Intégration Stripe Payment Intent
# - Gestion des erreurs appropriée
# - Logging des événements
# - Tests complets
```

---

## Exemple 3 : Skill + Rules pour un Projet React

### Skill : `.bob/skills/react-typescript.yaml`

```yaml
name: "React TypeScript Standards"
version: "1.0.0"
framework: react
language: typescript

# Configuration TypeScript
typescript:
  strict: true
  no_any: true
  no_implicit_any: true

# Composants
components:
  style: "functional"
  export_style: "named"
  props_destructuring: true

# State Management
state_management: zustand

# Styling
styling:
  primary: tailwind
  secondary: css_modules

# Forms
forms:
  library: react-hook-form
  validation: zod

# API
api:
  client: axios
  data_fetching: react-query

# Tests
testing:
  unit: vitest
  component: react-testing-library
  e2e: playwright

conventions:
  - "Functional components uniquement"
  - "Named exports pour les composants"
  - "Props typées avec TypeScript"
  - "Custom hooks préfixés avec 'use'"
  - "Un composant par fichier"
```

### Rules : `.bob/rules.md`

```markdown
# Règles du Projet - Dashboard Analytics

## Architecture

Application SPA React pour visualiser des données analytics en temps réel.

### Structure

```
src/
├── components/
│   ├── ui/          # Composants réutilisables (Button, Input)
│   ├── charts/      # Composants de graphiques
│   └── dashboard/   # Composants métier
├── hooks/           # Custom hooks
├── stores/          # Zustand stores
├── services/        # API services
└── pages/           # Pages
```

## Conventions Spécifiques

### Composants de Graphiques

- Utiliser Recharts pour tous les graphiques
- Wrapper dans des composants réutilisables
- Gérer le responsive
- Ajouter des tooltips informatifs

### Performance

- Virtualiser les longues listes (react-window)
- Lazy load les pages
- Memoizer les calculs coûteux
- Debounce les recherches (300ms)

### Temps Réel

- WebSocket pour les updates en temps réel
- Reconnexion automatique
- Afficher le statut de connexion
- Buffer les messages pendant la déconnexion
```

### Utilisation Combinée

```typescript
// Demande à Bob
"Crée un composant RevenueChart qui affiche les revenus en temps réel
en respectant nos skills et rules"

// Bob génère :
// - Composant fonctionnel TypeScript
// - Props typées
// - Utilisation de Recharts
// - WebSocket pour le temps réel
// - Responsive design avec Tailwind
// - Tests avec Vitest
```

---

## Exemple 4 : Workflow TDD avec Skills

### Skill : `.bob/skills/tdd-workflow.yaml`

```yaml
name: "TDD Workflow"
description: "Test-Driven Development workflow"
version: "1.0.0"

workflow:
  methodology: "Red-Green-Refactor"
  
  steps:
    - name: "Red"
      description: "Écrire un test qui échoue"
      action: "create_failing_test"
      
    - name: "Green"
      description: "Écrire le code minimal pour passer le test"
      action: "implement_minimal_code"
      
    - name: "Refactor"
      description: "Améliorer le code sans casser les tests"
      action: "refactor_code"
      
    - name: "Repeat"
      description: "Répéter pour la prochaine fonctionnalité"
      action: "next_feature"

test_framework: pytest
coverage_minimum: 90

test_conventions:
  - "Un test par comportement"
  - "Noms descriptifs : test_should_X_when_Y"
  - "Arrange-Act-Assert pattern"
  - "Utiliser des fixtures pour le setup"
  - "Mocker les dépendances externes"

refactoring_rules:
  - "Ne jamais refactorer sans tests verts"
  - "Faire des petits refactorings incrémentaux"
  - "Relancer les tests après chaque refactoring"
  - "Commiter après chaque cycle Red-Green-Refactor"
```

### Utilisation

```python
# Demande à Bob
"Implémente une fonction calculate_discount() en suivant le workflow TDD"

# Bob suit automatiquement le cycle :

# 1. RED - Crée le test qui échoue
def test_should_apply_10_percent_discount_when_amount_over_100():
    result = calculate_discount(amount=150, customer_type="regular")
    assert result == 135.0  # 150 - 15

# 2. GREEN - Implémente le minimum
def calculate_discount(amount: float, customer_type: str) -> float:
    if amount > 100:
        return amount * 0.9
    return amount

# 3. REFACTOR - Améliore le code
def calculate_discount(amount: float, customer_type: str) -> float:
    """Calcule le montant après réduction.
    
    Args:
        amount: Montant initial
        customer_type: Type de client
        
    Returns:
        Montant après réduction
    """
    DISCOUNT_RATES = {
        "regular": 0.10,
        "premium": 0.20,
        "vip": 0.30
    }
    
    if amount <= 100:
        return amount
        
    discount_rate = DISCOUNT_RATES.get(customer_type, 0)
    return amount * (1 - discount_rate)

# 4. REPEAT - Ajoute le test suivant
def test_should_apply_20_percent_discount_when_premium_customer():
    result = calculate_discount(amount=150, customer_type="premium")
    assert result == 120.0
```

---

## Exemple 5 : Configuration Multi-Projets

### Contexte

Vous gérez plusieurs projets avec des standards communs mais des spécificités.

### Structure

```
team-skills/  (repo Git partagé)
├── skills/
│   ├── common/
│   │   ├── python-base.yaml
│   │   ├── typescript-base.yaml
│   │   └── git-workflow.yaml
│   ├── backend/
│   │   ├── fastapi.yaml
│   │   └── django.yaml
│   └── frontend/
│       ├── react.yaml
│       └── vue.yaml
└── templates/
    ├── rules-api.md
    └── rules-frontend.md
```

### Projet 1 : API Backend

```bash
# .bob/skills/ (symlinks vers team-skills)
ln -s ../../team-skills/skills/common/python-base.yaml
ln -s ../../team-skills/skills/backend/fastapi.yaml

# .bob/rules.md (spécifique au projet)
# Règles du Projet API Users
[Hérite des skills communs + spécificités du projet]
```

### Projet 2 : Frontend Dashboard

```bash
# .bob/skills/
ln -s ../../team-skills/skills/common/typescript-base.yaml
ln -s ../../team-skills/skills/frontend/react.yaml

# .bob/rules.md
# Règles du Projet Dashboard
[Hérite des skills communs + spécificités du projet]
```

### Avantages

✅ Standards communs partagés  
✅ Facile à maintenir (un seul endroit)  
✅ Flexibilité par projet (rules spécifiques)  
✅ Versionné avec Git  
✅ Évolution collaborative

---

## 💡 Conseils Pratiques

### Démarrer Simple

1. **Commencez avec un skill de base** pour votre langage principal
2. **Ajoutez quelques rules** essentielles
3. **Testez avec Bob** sur des tâches simples
4. **Itérez** en ajoutant progressivement

### Mesurer l'Impact

- **Avant** : Temps pour créer une feature
- **Après** : Temps avec skills/rules
- **Qualité** : Nombre de bugs, couverture de tests
- **Cohérence** : Respect des standards

### Partager avec l'Équipe

1. **Créer un repo** de skills partagés
2. **Documenter** l'utilisation
3. **Former** l'équipe
4. **Itérer** selon les retours

---

_Exemples créés pour le Bobathon 2026_