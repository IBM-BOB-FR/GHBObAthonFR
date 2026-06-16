# Règles du Projet

## Architecture

Ce projet suit une architecture en couches :
- **Présentation** : API REST avec FastAPI
- **Métier** : Logique dans des services
- **Données** : Repository pattern avec SQLAlchemy

## Conventions de Nommage

- Classes : PascalCase (ex: UserService)
- Fonctions : snake_case (ex: get_user_by_id)
- Constantes : UPPER_SNAKE_CASE (ex: MAX_RETRY_COUNT)
- Fichiers : snake_case (ex: user_service.py)

## Bonnes Pratiques

- Toujours valider les entrées utilisateur
- Utiliser des exceptions personnalisées
- Logger les erreurs avec le contexte
- Écrire des tests pour chaque nouvelle fonctionnalité

## Ce qu'il faut éviter

- Pas de logique métier dans les routes
- Pas de requêtes SQL directes (utiliser les repositories)
- Pas de secrets en dur dans le code
- Pas de print() pour le debug (utiliser logging)