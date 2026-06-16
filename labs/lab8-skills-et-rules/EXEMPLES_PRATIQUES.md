# 🎯 Exemples Pratiques : Skills et Rules en Action

Ce document présente des exemples concrets d'utilisation des skills et rules de Bob dans des situations réelles.

---

## 📚 Table des Matières

1. [Skill : Analyse](#skill--analyse)
2. [Skill : Génération](#skill--génération)
3. [Skill : Refactoring](#skill--refactoring)
4. [Skill : Tests](#skill--tests)
5. [Rule : Lecture Groupée](#rule--lecture-groupée)
6. [Rule : Modifications Ciblées](#rule--modifications-ciblées)
7. [Workflows Complets](#workflows-complets)

---

## Skill : Analyse

### Exemple 1 : Analyse de Code Legacy

**Situation** : Vous héritez d'un code mal écrit

**Commande** :
```
Analyse @messy_code.py et identifie tous les problèmes :
- Nommage
- Style (PEP 8)
- Lisibilité
- Performance
- Bonnes pratiques
- Documentation manquante
```

**Résultat attendu de Bob** :
```
J'ai identifié 12 problèmes dans ce code :

1. NOMMAGE
   - Ligne 1 : Fonction 'calc' → nom trop vague, devrait être 'calculate_average'
   - Ligne 3-5 : Variables 'x', 'y', 'z' → noms non descriptifs
   - Ligne 14 : Attributs 'n', 'e', 'a' → noms cryptiques

2. STYLE (PEP 8)
   - Ligne 1 : Manque d'espaces autour des paramètres
   - Ligne 3-5 : Manque d'espaces autour des opérateurs
   - Ligne 8 : Manque de ligne vide avant la définition de fonction

3. LISIBILITÉ
   - Ligne 1-6 : Pas de docstring
   - Ligne 3-5 : Calculs intermédiaires non expliqués
   - Ligne 10 : Boucle avec range(len()) au lieu d'itération directe

4. PERFORMANCE
   - Ligne 10 : range(len(data)) inefficace, utiliser enumerate()
   - Ligne 11-12 : Append dans une boucle, utiliser list comprehension

5. BONNES PRATIQUES
   - Ligne 1 : Pas de type hints
   - Ligne 6 : Division par 2 pourrait causer une erreur si résultat attendu est int
   - Ligne 14 : Classe sans validation des données

6. DOCUMENTATION
   - Aucune docstring dans tout le fichier
   - Pas de commentaires pour expliquer la logique
```

### Exemple 2 : Analyse de Performance

**Commande** :
```
Analyse les performances de @data_processor.py et identifie les goulots d'étranglement
```

**Résultat attendu** :
```
Analyse de performance :

GOULOTS IDENTIFIÉS :

1. Fonction calculate_stats() (lignes 45-63)
   - Complexité : O(n) × 3 = O(3n)
   - Problème : 3 boucles séparées sur les mêmes données
   - Impact : Performance × 3 plus lente que nécessaire
   - Solution : Une seule boucle pour calculer tout

2. Fonction process_data() (lignes 3-21)
   - Problème : Concaténation de strings dans une boucle (XML/CSV)
   - Impact : O(n²) en mémoire
   - Solution : Utiliser une liste et join()

3. Validation (lignes 23-43)
   - Problème : Pas de cache pour les validations répétées
   - Solution : Ajouter un décorateur @lru_cache

RECOMMANDATIONS :
- Réduire calculate_stats de O(3n) à O(n)
- Utiliser join() au lieu de concaténation
- Ajouter du caching pour les validations
```

---

## Skill : Génération

### Exemple 1 : Génération d'une Classe Complète

**Commande** :
```
Crée une classe Product dans exercices/ex2-skills-generation/models.py avec :
- Attributs : id (UUID), name (str), price (Decimal), stock (int), category (str)
- Validation : price > 0, stock >= 0, name non vide
- Type hints partout
- Docstrings Google style
- Méthode __repr__ pour le debug
- Méthode to_dict() pour la sérialisation
- Utilise dataclass si approprié
```

**Code généré par Bob** :
```python
from dataclasses import dataclass, field
from decimal import Decimal
from uuid import UUID, uuid4
from typing import Dict, Any

@dataclass
class Product:
    """Représente un produit dans le système.
    
    Attributes:
        id: Identifiant unique du produit (UUID)
        name: Nom du produit (non vide)
        price: Prix du produit (doit être positif)
        stock: Quantité en stock (doit être >= 0)
        category: Catégorie du produit
        
    Raises:
        ValueError: Si les validations échouent
        
    Example:
        >>> product = Product(
        ...     name="Laptop",
        ...     price=Decimal("999.99"),
        ...     stock=10,
        ...     category="Electronics"
        ... )
    """
    
    name: str
    price: Decimal
    stock: int
    category: str
    id: UUID = field(default_factory=uuid4)
    
    def __post_init__(self) -> None:
        """Valide les données après initialisation."""
        if not self.name or not self.name.strip():
            raise ValueError("Le nom du produit ne peut pas être vide")
        
        if self.price <= 0:
            raise ValueError(f"Le prix doit être positif, reçu: {self.price}")
        
        if self.stock < 0:
            raise ValueError(f"Le stock ne peut pas être négatif, reçu: {self.stock}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertit le produit en dictionnaire.
        
        Returns:
            Dictionnaire contenant toutes les données du produit
        """
        return {
            'id': str(self.id),
            'name': self.name,
            'price': str(self.price),
            'stock': self.stock,
            'category': self.category
        }
    
    def __repr__(self) -> str:
        """Représentation pour le debug."""
        return (
            f"Product(id={self.id}, name='{self.name}', "
            f"price={self.price}, stock={self.stock}, category='{self.category}')"
        )
```

### Exemple 2 : Génération de Tests

**Commande** :
```
Crée des tests unitaires complets pour @models.py dans test_models.py
```

**Tests générés** :
```python
import pytest
from decimal import Decimal
from uuid import UUID
from models import Product

class TestProduct:
    """Tests pour la classe Product."""
    
    def test_product_creation_valid(self):
        """Test création d'un produit valide."""
        product = Product(
            name="Laptop",
            price=Decimal("999.99"),
            stock=10,
            category="Electronics"
        )
        
        assert product.name == "Laptop"
        assert product.price == Decimal("999.99")
        assert product.stock == 10
        assert product.category == "Electronics"
        assert isinstance(product.id, UUID)
    
    def test_product_validation_empty_name(self):
        """Test validation : nom vide."""
        with pytest.raises(ValueError, match="ne peut pas être vide"):
            Product(
                name="",
                price=Decimal("10.00"),
                stock=5,
                category="Test"
            )
    
    def test_product_validation_negative_price(self):
        """Test validation : prix négatif."""
        with pytest.raises(ValueError, match="doit être positif"):
            Product(
                name="Test",
                price=Decimal("-10.00"),
                stock=5,
                category="Test"
            )
    
    def test_product_validation_negative_stock(self):
        """Test validation : stock négatif."""
        with pytest.raises(ValueError, match="ne peut pas être négatif"):
            Product(
                name="Test",
                price=Decimal("10.00"),
                stock=-5,
                category="Test"
            )
    
    def test_product_to_dict(self):
        """Test conversion en dictionnaire."""
        product = Product(
            name="Mouse",
            price=Decimal("29.99"),
            stock=50,
            category="Accessories"
        )
        
        result = product.to_dict()
        
        assert result['name'] == "Mouse"
        assert result['price'] == "29.99"
        assert result['stock'] == 50
        assert result['category'] == "Accessories"
        assert 'id' in result
    
    def test_product_repr(self):
        """Test représentation string."""
        product = Product(
            name="Keyboard",
            price=Decimal("79.99"),
            stock=25,
            category="Accessories"
        )
        
        repr_str = repr(product)
        
        assert "Product(" in repr_str
        assert "name='Keyboard'" in repr_str
        assert "price=79.99" in repr_str
```

---

## Skill : Refactoring

### Exemple 1 : Appliquer le Strategy Pattern

**Avant** :
```python
def process_data(data, format):
    if format == 'json':
        return json.dumps(data)
    elif format == 'xml':
        # ... code XML
    elif format == 'csv':
        # ... code CSV
```

**Commande** :
```
Refactorise @data_processor.py en appliquant le Strategy Pattern pour les formatters
```

**Après (généré par Bob)** :
```python
from abc import ABC, abstractmethod
from typing import Dict, Any
import json

class DataFormatter(ABC):
    """Interface pour les formatters de données."""
    
    @abstractmethod
    def format(self, data: Dict[str, Any]) -> str:
        """Formate les données."""
        pass

class JsonFormatter(DataFormatter):
    """Formatter JSON."""
    
    def format(self, data: Dict[str, Any]) -> str:
        """Formate en JSON."""
        return json.dumps(data, indent=2)

class XmlFormatter(DataFormatter):
    """Formatter XML."""
    
    def format(self, data: Dict[str, Any]) -> str:
        """Formate en XML."""
        elements = [f"<{key}>{value}</{key}>" for key, value in data.items()]
        return f"<data>{''.join(elements)}</data>"

class CsvFormatter(DataFormatter):
    """Formatter CSV."""
    
    def format(self, data: Dict[str, Any]) -> str:
        """Formate en CSV."""
        headers = ','.join(data.keys())
        values = ','.join(str(v) for v in data.values())
        return f"{headers}\n{values}"

class DataProcessor:
    """Processeur de données avec formatters interchangeables."""
    
    def __init__(self, formatter: DataFormatter):
        self.formatter = formatter
    
    def process(self, data: Dict[str, Any]) -> str:
        """Traite les données avec le formatter configuré."""
        return self.formatter.format(data)
```

---

## Rule : Lecture Groupée

### Exemple : Comprendre un Module Complet

**Situation** : Vous voulez comprendre comment fonctionne un module d'authentification

**Commande optimale** :
```
Lis ensemble ces fichiers du module auth :
@auth/models.py
@auth/services.py
@auth/routes.py
@auth/middleware.py
@auth/utils.py

Puis explique-moi comment l'authentification fonctionne dans ce système.
```

**Avantages** :
- Bob lit les 5 fichiers en une seule fois (Rule 3)
- Il comprend le contexte complet
- Il peut expliquer les interactions entre fichiers
- Plus efficace que lire un par un

**Résultat de Bob** :
```
Après lecture des 5 fichiers, voici comment fonctionne l'authentification :

ARCHITECTURE :
1. models.py : Définit User et Token
2. services.py : Logique métier (login, register, verify)
3. routes.py : Endpoints API
4. middleware.py : Vérification des tokens
5. utils.py : Fonctions helper (hash, JWT)

FLUX D'AUTHENTIFICATION :
1. User POST /login → routes.py
2. routes.py appelle services.authenticate()
3. services.py vérifie avec models.User
4. services.py génère un JWT avec utils.create_token()
5. Token retourné au client
6. Requêtes suivantes → middleware.py vérifie le token
7. middleware.py utilise utils.verify_token()

POINTS CLÉS :
- JWT avec expiration de 24h
- Passwords hashés avec bcrypt
- Refresh tokens supportés
- Rate limiting sur /login
```

---

## Rule : Modifications Ciblées

### Exemple : Ajouter une Fonctionnalité

**Situation** : Ajouter une méthode à une classe existante

**❌ Mauvaise approche** :
```
Réécris @models.py en ajoutant une méthode update()
```
→ Risque : Bob réécrit tout le fichier, peut introduire des erreurs

**✅ Bonne approche** :
```
Ajoute une méthode update() à la classe User dans @models.py
en utilisant apply_diff
```

**Résultat de Bob** :
```
Je vais ajouter la méthode update() à la classe User.
```

```python
<<<<<<< SEARCH
    def to_dict(self) -> Dict[str, Any]:
        """Convertit l'utilisateur en dictionnaire."""
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email
        }
=======
    def to_dict(self) -> Dict[str, Any]:
        """Convertit l'utilisateur en dictionnaire."""
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email
        }
    
    def update(self, **kwargs) -> None:
        """Met à jour les attributs de l'utilisateur.
        
        Args:
            **kwargs: Attributs à mettre à jour
            
        Raises:
            ValueError: Si un attribut est invalide
        """
        for key, value in kwargs.items():
            if not hasattr(self, key):
                raise ValueError(f"Attribut invalide : {key}")
            setattr(self, key, value)
        
        # Revalider après mise à jour
        self.__post_init__()
>>>>>>> REPLACE
```

**Avantages** :
- Modification précise et ciblée
- Vous voyez exactement ce qui change
- Moins de risques d'erreurs
- Facile à valider

---

## Workflows Complets

### Workflow 1 : Créer une API REST Complète

```
Étape 1 : Génération
"Crée une API REST Flask pour gérer des livres dans exercices/api-books/"

Étape 2 : Validation
[Vous validez la structure créée]

Étape 3 : Lecture groupée
"Lis @app.py, @models.py et @routes.py ensemble"

Étape 4 : Analyse
"Analyse cette API et suggère des améliorations"

Étape 5 : Amélioration ciblée
"Ajoute la validation des données avec marshmallow dans @routes.py"

Étape 6 : Tests
"Crée des tests d'API complets dans test_api.py"

Étape 7 : Documentation
"Crée un README.md avec des exemples d'utilisation de l'API"
```

### Workflow 2 : Refactoring d'un Projet Legacy

```
Étape 1 : Lecture complète
"Lis tous les fichiers Python dans legacy/ (jusqu'à 5 fichiers)"

Étape 2 : Analyse approfondie
"Analyse ce code et identifie tous les problèmes par ordre de priorité"

Étape 3 : Plan de refactoring
"Propose un plan de refactoring détaillé avec les étapes à suivre"

Étape 4 : Refactoring progressif
"Commence par le problème prioritaire : refactorise @data_processor.py"

Étape 5 : Tests de non-régression
"Crée des tests pour vérifier que le comportement n'a pas changé"

Étape 6 : Validation
[Vous exécutez les tests et validez]

Étape 7 : Itération
"Continue avec le problème suivant : @api.py"

Étape 8 : Documentation
"Crée un REFACTORING.md qui documente tous les changements"
```

### Workflow 3 : Optimisation de Performance

```
Étape 1 : Profilage
"Analyse les performances de @slow_module.py"

Étape 2 : Identification
"Identifie les 3 fonctions les plus lentes"

Étape 3 : Optimisation ciblée
"Optimise la fonction calculate_stats() en réduisant la complexité"

Étape 4 : Benchmarking
"Crée un script de benchmark pour comparer avant/après"

Étape 5 : Tests
"Vérifie que les tests passent toujours après optimisation"

Étape 6 : Documentation
"Documente les améliorations de performance dans PERFORMANCE.md"
```

---

## 💡 Conseils Pratiques

### Maximiser l'Efficacité

1. **Planifiez vos demandes**
   - Réfléchissez à ce dont Bob a besoin
   - Groupez les lectures de fichiers
   - Soyez spécifique dans vos demandes

2. **Utilisez les bons skills**
   - Analyse → Comprendre
   - Génération → Créer
   - Refactoring → Améliorer
   - Tests → Sécuriser

3. **Respectez les rules**
   - Un outil par message → Clarté
   - Validation → Contrôle
   - Lecture groupée → Efficacité
   - Modifications ciblées → Sécurité

### Éviter les Pièges

❌ **À éviter** :
```
"Fais tout en une fois"
"Suppose ce que je veux"
"Réécris tout le fichier"
"Ne me demande pas de confirmation"
```

✅ **À faire** :
```
"Étape par étape, en commençant par..."
"Clarifie d'abord ce que je veux"
"Modifie uniquement la fonction X"
"Attends ma validation avant de continuer"
```

---

## 🎯 Exercices Pratiques

Testez ces workflows dans le Lab 8 :

1. **Exercice 1** : Utilisez le skill d'analyse sur du code legacy
2. **Exercice 2** : Générez une application complète
3. **Exercice 3** : Appliquez les rules dans un workflow complexe
4. **Exercice 4** : Combinez skills et rules pour un refactoring complet

---

_Exemples créés pour le Bobathon 2026_