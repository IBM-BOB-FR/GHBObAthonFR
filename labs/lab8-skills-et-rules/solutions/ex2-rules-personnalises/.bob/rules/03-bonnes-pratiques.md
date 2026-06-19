# Bonnes Pratiques

## Validation et Sécurité

- Toujours valider les entrées utilisateur
- Utiliser des exceptions personnalisées
- Logger les erreurs avec le contexte

## Tests et Qualité

- Écrire des tests pour chaque nouvelle fonctionnalité
- Minimum 80% de couverture de code
- Tests unitaires + tests d'intégration

## Ce qu'il faut éviter

- Pas de logique métier dans les routes
- Pas de requêtes SQL directes (utiliser les repositories)
- Pas de secrets en dur dans le code
- Pas de print() pour le debug (utiliser logging)