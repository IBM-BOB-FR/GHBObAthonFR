# 🎯 Lab 8 : Skills et Rules - Personnaliser Bob

> **Durée estimée** : 45-60 minutes
> **Difficulté** : ⭐⭐⭐ Avancé
> **Objectif** : Maîtriser la configuration avancée de Bob avec Skills et Rules

## 🎥 Introduction Vidéo

Avant de commencer, regardez cette vidéo qui explique les concepts de Skills, Modes et Rules dans Bob :

[![Compétences vs modes vs règles – Laissez IBM Bob parler comme un pirate](https://img.youtube.com/vi/gbIXpgZHzMM/0.jpg)](https://www.youtube.com/watch?v=gbIXpgZHzMM)

**[▶️ Regarder la vidéo : Compétences vs modes vs règles](https://www.youtube.com/watch?v=gbIXpgZHzMM)**

> **Note** : La vidéo ne s'affiche pas directement dans le README sur GitHub, mais le lien cliquable vous permettra de l'ouvrir dans votre navigateur. Dans certains éditeurs Markdown (comme VS Code avec des extensions appropriées), la miniature peut s'afficher.

---

## 📋 Objectifs d'Apprentissage

À la fin de ce lab, vous serez capable de :

- ✅ Comprendre ce que sont les **Skills** dans Bob (fichiers de configuration `.bob/skills/`)
- ✅ Créer et configurer des **Skills** personnalisés
- ✅ Utiliser le fichier **Rules** (`.bob/rules.md`) pour personnaliser le comportement de Bob
- ✅ Combiner Skills et Rules pour des workflows optimisés
- ✅ Créer des configurations réutilisables pour votre équipe

---

## 🔧 Prérequis Techniques

- Python 3.8+ installé
- (Optionnel) PyYAML pour valider les fichiers : `pip install pyyaml`
- Éditeur de texte avec support YAML (VS Code recommandé)

---

## 🧠 Qu'est-ce que les "Skills" de Bob ?

> **Documentation officielle** : https://bob.ibm.com/docs/ide/features/skills

Les **Skills** sont des fichiers Markdown situés dans `.bob/skills/` qui permettent de :

1. **Définir des comportements spécifiques** : Créer des compétences personnalisées pour Bob
2. **Configurer des workflows** : Automatiser des séquences d'actions
3. **Créer des instructions spécialisées** : Définir des flux de travail pour des tâches spécifiques
4. **Partager des configurations** : Réutiliser des skills dans plusieurs projets

### Structure d'un Skill

```markdown
# .bob/skills/mon-skill.md

# Mon Skill Personnalisé

Description de ce que fait ce skill.

## Instructions

- Instruction 1
- Instruction 2
- Instruction 3

## Exemples

Exemples d'utilisation...
```

---

## 📏 Qu'est-ce que les "Rules" de Bob ?

Le fichier **Rules** (`.bob/rules.md`) contient des instructions personnalisées en langage naturel qui modifient le comportement de Bob :

1. **Instructions globales** : Comment Bob doit se comporter dans votre projet
2. **Préférences de code** : Conventions, styles, patterns à utiliser
3. **Contraintes** : Ce que Bob doit éviter ou toujours faire
4. **Contexte projet** : Informations spécifiques à votre projet

### Exemple de Rules

```markdown
# .bob/rules.md

## Conventions de Code

- Toujours utiliser TypeScript strict mode
- Préférer les functional components en React
- Utiliser Prettier avec la config du projet

## Architecture

- Suivre l'architecture hexagonale
- Séparer la logique métier des frameworks
- Utiliser des interfaces pour les dépendances

## Tests

- Minimum 80% de couverture de code
- Utiliser Jest pour les tests unitaires
- Créer des tests d'intégration pour les API
```

---

## 🚀 Mise en Place

### Prérequis

- Avoir complété les Labs 0, 1 et 2
- Comprendre les bases de YAML
- Avoir ce projet (GHBObAthonFR) ouvert dans VS Code avec Bob

### 📍 Emplacement du Répertoire `.bob`

**Important** : Selon la [documentation officielle de Bob](https://bob.ibm.com/docs/ide/configuration/rules), le répertoire `.bob` doit être placé :

1. **À la racine de votre projet courant** (recommandé pour ce lab) :
   ```
   GHBObAthonFR/.bob/
   ```
   - S'applique uniquement à ce projet
   - Idéal pour les configurations spécifiques au projet

2. **Dans votre répertoire home** (pour effet global) :
   ```
   ~/.bob/rules/
   ```
   - S'applique à tous vos projets
   - Utile pour les normes personnelles ou organisationnelles

**Pour ce lab, nous utiliserons la racine du projet** (`.bob/` à la racine de GHBObAthonFR).

### Structure du Lab

```
GHBObAthonFR/                      # Racine du projet
├── .bob/                          # ← Configuration Bob pour tout le projet
│   ├── skills/                    # ← Vos skills personnalisés
│   └── rules/                     # ← Vos règles personnalisées (répertoire)
│       ├── 01-architecture.md     # ← Règles d'architecture
│       ├── 02-conventions.md      # ← Conventions de code
│       └── 03-bonnes-pratiques.md # ← Bonnes pratiques
├── labs/
│   └── lab8-skills-et-rules/
│       ├── README.md (ce fichier)
│       ├── exercices/
│       │   ├── ex1-skills-analyse/
│       │   ├── ex2-rules-personnalises/
│       │   ├── ex3-rules-workflow/
│       │   └── ex4-optimisation/
│       ├── exemples/
│       │   ├── skills/
│       │   └── rules/
│       └── solutions/
```

---

## 📝 Exercice 1 : Créer Votre Premier Skill (15 min)

### Objectif

Créer un skill simple qui définit des préférences de code pour Python.

### Instructions

1. **Créez la structure de base à la racine du projet** :

```
Crée le répertoire .bob/skills/ à la racine du projet (GHBObAthonFR/.bob/skills/)
```

2. **Créez votre premier skill** :

```
Crée .bob/skills/python-style.md à la racine du projet avec :

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
```


3. **Testez le skill** :

Crée un fichier test.py et demande à Bob de générer une fonction calculate_average()
qui prend une liste de nombres en paramètre et retourne leur moyenne,
en respectant les conventions du skill python-style.md


### ✅ Critères de Validation

- [ ] Le fichier skill est créé dans `.bob/skills/`
- [ ] Le skill contient toutes les préférences
- [ ] Bob génère du code conforme au skill
- [ ] Vous comprenez comment les skills influencent Bob

### 💡 Points Clés

Les **Skills** permettent de :
- Définir des standards de code
- Automatiser l'application de conventions
- Partager des configurations dans l'équipe
- Maintenir la cohérence du code


4. **Refactoring**

Demandez à Bob de refactorer le code `labs/lab8-skills-et-rules/exercices/ex1-skills-analyse/messy_code.py` en utilisant le skill que vous venez de créer.

---

## 🔨 Exercice 2 : Configurer des Rules Personnalisées (15 min)

### Objectif

Créer des fichiers de règles organisés dans `.bob/rules/` qui guident Bob dans votre projet.

### Instructions

1. **Créez le répertoire et les fichiers de règles à la racine du projet** :

Crée la structure `.bob/rules/` à la racine du projet `(GHBObAthonFR/.bob/rules/)` avec :

1. `.bob/rules/01-architecture.md` :
```
# Architecture du Projet

Ce projet suit une architecture en couches :
- **Présentation** : API REST avec FastAPI
- **Métier** : Logique dans des services
- **Données** : Repository pattern avec SQLAlchemy

## Principes

- Séparation des responsabilités
- Dépendances vers l'intérieur
- Interfaces pour l'abstraction
```

2. `.bob/rules/02-conventions.md` :
```

# Conventions de Nommage

- Classes : PascalCase (ex: UserService)
- Fonctions : snake_case (ex: get_user_by_id)
- Constantes : UPPER_SNAKE_CASE (ex: MAX_RETRY_COUNT)
- Fichiers : snake_case (ex: user_service.py)

## Formatage

- Utiliser Black pour le formatage
- Ligne maximale : 88 caractères
- Imports organisés avec isort
```

3. `.bob/rules/03-bonnes-pratiques.md` :

```
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
```

2. **Testez les Rules** :

```
Demande à Bob de créer un service UserService en Python avec FastAPI qui :
- Implémente une méthode get_user_by_id(user_id: int) -> User
- Utilise un repository UserRepository pour accéder aux données
- Valide que l'ID utilisateur est positif
- Lève une exception UserNotFoundException si l'utilisateur n'existe pas
- Lève une exception ValidationError si l'ID est invalide
- Utilise le logging pour tracer les erreurs
- Respecte toutes les rules du projet (architecture en couches, conventions de nommage, bonnes pratiques)
- Inclut les type hints et docstrings Google style
```

3. **Observez le comportement** :

Bob devrait automatiquement :
- Suivre l'architecture en couches
- Utiliser les conventions de nommage
- Appliquer les bonnes pratiques
- Éviter les anti-patterns listés

### ✅ Critères de Validation

- [ ] Le répertoire `.bob/rules/` est créé avec les 3 fichiers
- [ ] Les rules couvrent architecture, conventions et bonnes pratiques
- [ ] Bob respecte les rules dans le code généré
- [ ] Vous comprenez comment les rules influencent Bob
- [ ] Vous comprenez l'avantage d'organiser les rules en plusieurs fichiers

### 💡 Points Clés

Les **Rules organisées en répertoire** permettent de :
- **Séparer les préoccupations** : Un fichier par thème (architecture, conventions, etc.)
- **Faciliter la maintenance** : Modifier une catégorie sans toucher aux autres
- **Améliorer la lisibilité** : Fichiers plus courts et ciblés
- **Collaborer efficacement** : Différentes personnes peuvent gérer différents fichiers
- **Réutiliser** : Copier uniquement les fichiers de règles pertinents dans d'autres projets

**Note** : Les fichiers sont chargés par ordre alphabétique (d'où les préfixes 01-, 02-, 03-)

---

## 📏 Exercice 3 : Skill Avancé avec Workflow (15 min)

### Objectif

Créer un skill qui définit un workflow complet pour le développement.

### Instructions

1. **Créez un skill de workflow à la racine du projet** :

```
Crée .bob/skills/tdd-workflow.md à la racine du projet (GHBObAthonFR/.bob/skills/tdd-workflow.md) avec :

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
```


2. **Utilisez le workflow** :

```
Demande à Bob de créer une fonctionnalité "calculer la moyenne d'une liste"
en suivant le workflow TDD défini dans tdd-workflow.md
```

3. **Observez le processus** :

Bob devrait :
- Créer d'abord les tests
- Implémenter le code minimal
- Refactorer si nécessaire
- Ajouter la documentation

### ✅ Critères de Validation

- [ ] Le skill workflow est créé
- [ ] Bob suit les étapes du workflow
- [ ] Les tests sont créés en premier
- [ ] Le code est refactoré et documenté
- [ ] La couverture atteint le minimum requis

### 💡 Points Clés

Les **Skills avancés** permettent de :
- Définir des workflows complexes
- Automatiser des processus de développement
- Garantir la qualité du code
- Former l'équipe aux bonnes pratiques

---

## 🎯 Exercice 4 : Workflow Complet avec Skills et Rules (15 min)

### Objectif

Combiner Skills et Rules pour créer un environnement de développement optimal.

### Instructions

1. **Enrichissez votre configuration à la racine du projet** :

```
À la racine du projet (GHBObAthonFR/.bob/), ajoutez :

1. .bob/skills/api-development.md :
   - Standards pour les API REST
   - Validation des données
   - Gestion d'erreurs
   - Documentation OpenAPI

2. .bob/skills/security.md :
   - Bonnes pratiques de sécurité
   - Validation des entrées
   - Authentification/Autorisation
   - Protection contre les vulnérabilités courantes

3. Ajoutez un nouveau fichier de règles .bob/rules/04-api-standards.md :
   - Standards spécifiques aux API REST
   - Stack technique (FastAPI, PostgreSQL, Redis)
   - Processus de review
   - Documentation requise
```

2. **Créez une API complète** :

```
Demande à Bob de refactorer le code dans labs/lab8-skills-et-rules/exercices/ex4-optimisation/legacy/
en créant une API REST moderne pour gérer des articles de blog avec :
- CRUD complet
- Authentification JWT
- Validation des données
- Tests unitaires et d'intégration
- Documentation OpenAPI
- Respect de tous les skills et rules configurés dans .bob/
```

3. **Analysez le résultat** :

Vérifiez que Bob a :
- Suivi l'architecture définie dans .bob/rules/01-architecture.md
- Respecté les conventions de .bob/rules/02-conventions.md
- Appliqué les bonnes pratiques de .bob/rules/03-bonnes-pratiques.md
- Suivi les standards API de .bob/rules/04-api-standards.md
- Appliqué les standards de .bob/skills/api-development.md
- Implémenté les pratiques de .bob/skills/security.md
- Créé un code cohérent et de qualité

### ✅ Critères de Validation

- [ ] Tous les skills et rules sont créés
- [ ] L'API est complète et fonctionnelle
- [ ] Les standards de sécurité sont appliqués
- [ ] Les tests passent avec succès
- [ ] La documentation est complète
- [ ] Vous comprenez la synergie Skills + Rules

### 💡 Points Clés

La **combinaison Skills + Rules** permet :
- **Cohérence** : Standards appliqués automatiquement
- **Qualité** : Bonnes pratiques intégrées
- **Productivité** : Moins de décisions à prendre
- **Collaboration** : Configuration partagée dans l'équipe

---

## 🎓 Exercice Bonus : Skills Réutilisables (Optionnel)

### Mission

Enrichir votre configuration `.bob/` à la racine du projet avec une bibliothèque de skills réutilisables.

### Instructions

```
Enrichissez votre configuration à la racine du projet (GHBObAthonFR/.bob/) :

1. .bob/skills/languages/
   - python.md
   - typescript.md
   - java.md

2. .bob/skills/frameworks/
   - fastapi.md
   - react.md
   - spring-boot.md

3. .bob/skills/practices/
   - tdd.md
   - clean-code.md
   - security.md

4. .bob/templates/
   - rules-template.md
   - skill-template.md

5. .bob/README.md :
   - Comment utiliser la bibliothèque de skills
   - Comment contribuer
   - Exemples d'utilisation
```

### Exemples de Skills

**Python Skill** :
```markdown
# Python Best Practices

## Configuration

- **Formateur** : Black
- **Linter** : Ruff
- **Type checker** : mypy
- **Framework de test** : pytest

## Conventions

- Conformité PEP 8
- Type hints obligatoires
- Docstrings style Google
```

**FastAPI Skill** :
```markdown
# FastAPI Development

## Patterns Recommandés

- Utiliser l'injection de dépendances
- Modèles Pydantic pour la validation
- Async/await pour les opérations I/O
- Documentation OpenAPI automatique

## Structure

```python
from fastapi import FastAPI, Depends

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
```

---

## 📊 Auto-Évaluation

Vérifiez que vous maîtrisez :

### Skills

- [ ] Je comprends ce qu'est un skill dans Bob
- [ ] Je sais créer un fichier skill YAML
- [ ] Je peux définir des préférences et conventions
- [ ] Je sais créer des workflows avec les skills
- [ ] Je comprends comment partager des skills

### Rules

- [ ] Je comprends ce qu'est le fichier rules.md
- [ ] Je sais écrire des rules claires et efficaces
- [ ] Je peux définir l'architecture dans les rules
- [ ] Je sais spécifier des conventions d'équipe
- [ ] Je comprends comment les rules influencent Bob

### Intégration

- [ ] Je peux combiner skills et rules efficacement
- [ ] Je sais créer une configuration de projet complète
- [ ] Je comprends les bénéfices pour l'équipe
- [ ] Je peux créer des configurations réutilisables

---

## 🎓 Ce que Vous Avez Appris

### Skills (.bob/skills/*.md)

**Définition** : Fichiers de configuration YAML qui définissent des comportements spécifiques

**Utilisations** :
- Standards de code par langage
- Workflows de développement
- Configurations d'outils
- Patterns et pratiques

**Avantages** :
- Réutilisables entre projets
- Partageables dans l'équipe
- Versionnables avec Git
- Faciles à maintenir

### Rules (.bob/rules.md)

**Définition** : Fichier Markdown avec des instructions en langage naturel

**Utilisations** :
- Architecture du projet
- Conventions d'équipe
- Contexte spécifique
- Contraintes et préférences

**Avantages** :
- Flexibles et expressifs
- Faciles à lire et écrire
- Adaptables au contexte
- Évolutifs avec le projet

### Synergie Skills + Rules

```
Skills (YAML)          Rules (Markdown)
     ↓                       ↓
Configuration          Instructions
structurée             en langage naturel
     ↓                       ↓
        ↘               ↙
          Bob Personnalisé
                ↓
        Code de Qualité
```

---

## 💡 Bonnes Pratiques

### Pour les Skills

1. **Soyez spécifique** : Un skill = un domaine précis
2. **Versionnez** : Utilisez semantic versioning
3. **Documentez** : Ajoutez description et exemples
4. **Testez** : Vérifiez que le skill fonctionne comme prévu
5. **Partagez** : Créez une bibliothèque d'équipe

### Pour les Rules

1. **Soyez clair** : Utilisez un langage simple et direct
2. **Soyez concis** : Évitez les règles trop longues
3. **Priorisez** : Mettez les règles importantes en premier
4. **Illustrez** : Donnez des exemples concrets
5. **Maintenez** : Mettez à jour avec l'évolution du projet

### Pour l'Intégration

1. **Commencez simple** : Un skill et quelques rules
2. **Itérez** : Ajoutez progressivement
3. **Mesurez** : Vérifiez l'impact sur la qualité
4. **Ajustez** : Adaptez selon les retours
5. **Partagez** : Documentez pour l'équipe
---

## ✅ Validation de Votre Travail

### Vérifier un Skill YAML

```bash
# Installer PyYAML si nécessaire
pip install pyyaml

# Vérifier qu'un skill existe et est lisible
cat .bob/skills/mon-skill.md | head -10
```

### Vérifier les Rules

```bash
# Vérifier qu'un fichier de rules existe et est lisible
cat .bob/rules/01-architecture.md | head -10
```

### Tester avec Bob

Une fois vos skills et rules créés, testez-les :

1. **Ouvrez votre projet dans VS Code avec Bob**
2. **Demandez à Bob** : "Crée une fonction calculate_average() en respectant nos standards Python"
3. **Observez** : Bob devrait respecter vos conventions (type hints, docstrings, formatage)
4. **Itérez** : Ajustez vos skills/rules selon les résultats

**Exemple de test** :
```
Prompt : "Crée une fonction calculate_average() en respectant nos standards"

Bob devrait générer du code avec :
- Type hints (List[float] -> float)
- Docstring Google style
- Formatage Black
- Noms descriptifs
- Gestion d'erreurs si spécifié dans vos rules
```


---

## 🚀 Prochaines Étapes

Vous maîtrisez maintenant Skills et Rules !

### Appliquez dans Vos Projets

1. **Créez vos skills** : Commencez par votre langage principal
2. **Définissez vos rules** : Documentez vos conventions
3. **Partagez avec l'équipe** : Créez une configuration commune
4. **Itérez** : Améliorez continuellement

### Explorez Plus Loin

- **Lab 6** : Custom MCP Modes (modes personnalisés avancés)
- **Lab 7** : DevOps Automation (automatisation CI/CD)
- **Documentation Bob** : https://internal.bob.ibm.com/docs

---

## 📚 Ressources

### Documentation Officielle

- **Skills** : https://internal.bob.ibm.com/docs/ide/features/skills
- **Rules** : https://internal.bob.ibm.com/docs/ide/configuration/rules
- **Configuration** : https://internal.bob.ibm.com/docs/ide/configuration

### Exemples

Consultez les fichiers dans `exemples/` :
- `skills/` : Exemples de skills pour différents langages
- `rules/` : Exemples de rules pour différents types de projets

### Vidéos

- [Compétences vs modes vs règles – Laissez IBM Bob parler comme un pirate](https://www.youtube.com/watch?v=example)

---

## 🎯 Challenge Final

Créez une configuration complète pour votre projet actuel :

1. **Identifiez vos besoins** : Quels standards ? Quelles conventions ?
2. **Créez vos skills** : Au moins 2-3 skills pertinents
3. **Écrivez vos rules** : Architecture, conventions, bonnes pratiques
4. **Testez** : Demandez à Bob de générer du code
5. **Partagez** : Documentez pour votre équipe

**Bravo ! Vous êtes maintenant un expert de la configuration Bob !** 🎉

---

_Lab créé pour le Bobathon 2026_