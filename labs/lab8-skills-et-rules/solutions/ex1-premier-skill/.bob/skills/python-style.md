# Python Style Guide

Préférences de style pour le code Python.

## Standards

- **Langage** : Python
- **Guide de style** : PEP 8
- **Type hints** : Obligatoires
- **Style de docstring** : Google
- **Longueur de ligne max** : 88 caractères
- **Formateur** : Black
- **Linter** : Ruff

## Conventions

- Utiliser des noms descriptifs pour les variables
- Préférer les list comprehensions aux boucles simples
- Toujours ajouter des type hints
- Documenter toutes les fonctions publiques

## Exemples

```python
def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average.
        
    Returns:
        The average value.
    """
    return sum(numbers) / len(numbers)