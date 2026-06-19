# TDD Workflow

Workflow Test-Driven Development pour garantir la qualité du code.

## Étapes du Workflow

### 1. Écrire le test (Red)
Créer un test qui échoue pour la fonctionnalité à implémenter.

### 2. Implémenter (Green)
Écrire le code minimal pour faire passer le test.

### 3. Refactorer (Refactor)
Améliorer le code sans casser les tests.

### 4. Documenter
Ajouter la documentation nécessaire.

## Configuration

- **Framework de test** : pytest
- **Couverture minimale** : 80%

## Conventions

- Suivre le cycle Red-Green-Refactor
- Un test par comportement
- Tests lisibles et maintenables
- Utiliser des mocks pour les dépendances externes

## Exemple

```python
# 1. Test (Red)
def test_calculate_average():
    assert calculate_average([1, 2, 3]) == 2.0

# 2. Implémentation (Green)
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# 3. Refactoring + Documentation
def calculate_average(numbers: list[float]) -> float:
    """Calculate average of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)