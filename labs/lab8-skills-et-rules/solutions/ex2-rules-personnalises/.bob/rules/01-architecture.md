# Architecture du Projet

Ce projet suit une architecture en couches :
- **Présentation** : API REST avec FastAPI
- **Métier** : Logique dans des services
- **Données** : Repository pattern avec SQLAlchemy

## Principes

- Séparation des responsabilités
- Dépendances vers l'intérieur
- Interfaces pour l'abstraction