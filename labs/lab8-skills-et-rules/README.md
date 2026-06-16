# 🎯 Lab 8 : Skills et Rules - Personnaliser Bob

> **Durée estimée** : 45-60 minutes
> **Difficulté** : ⭐⭐⭐ Avancé
> **Objectif** : Maîtriser la configuration avancée de Bob avec Skills et Rules

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

Les **Skills** sont des fichiers de configuration YAML situés dans `.bob/skills/` qui permettent de :

1. **Définir des comportements spécifiques** : Créer des compétences personnalisées pour Bob
2. **Configurer des outils** : Définir comment Bob utilise certains outils
3. **Créer des workflows** : Automatiser des séquences d'actions
4. **Partager des configurations** : Réutiliser des skills dans plusieurs projets

### Structure d'un Skill

```yaml
# .bob/skills/mon-skill.yaml
name: "Mon Skill Personnalisé"
description: "Description de ce que fait ce skill"
version: "1.0.0"

# Configuration du skill
config:
  # Paramètres spécifiques
```

**Documentation officielle** : https://internal.bob.ibm.com/docs/ide/features/skills

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

**Documentation officielle** : https://internal.bob.ibm.com/docs/ide/configuration/rules

---

## 🚀 Mise en Place

### Prérequis

- Avoir complété les Labs 0, 1 et 2
- Comprendre les bases de YAML
- Avoir un projet avec Bob configuré

### Structure du Lab

```
lab8-skills-et-rules/
├── README.md (ce fichier)
├── exercices/
│   ├── ex1-premier-skill/
│   ├── ex2-rules-personnalises/
│   ├── ex3-skill-avance/
│   └── ex4-workflow-complet/
├── exemples/
│   ├── skills/
│   └── rules/
└── solutions/
```

---

## 📝 Exercice 1 : Créer Votre Premier Skill (15 min)

### Objectif

Créer un skill simple qui définit des préférences de code pour Python.

### Instructions

1. **Créez la structure de base** :

```
Crée le répertoire .bob/skills/ dans exercices/ex1-premier-skill/
```

2. **Créez votre premier skill** :

```
Crée .bob/skills/python-style.yaml avec :

name: "Python Style Guide"
description: "Préférences de style pour le code Python"
version: "1.0.0"

preferences:
  language: python
  style_guide: "PEP 8"
  type_hints: required
  docstring_style: "Google"
  max_line_length: 88
  formatter: "black"
  linter: "ruff"
  
conventions:
  - "Utiliser des noms descriptifs pour les variables"
  - "Préférer les list comprehensions aux boucles simples"
  - "Toujours ajouter des type hints"
  - "Documenter toutes les fonctions publiques"
```

3. **Testez le skill** :

```
Crée un fichier test.py et demande à Bob de générer une fonction
qui respecte les conventions du skill python-style.yaml
```

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

---

## 🔨 Exercice 2 : Configurer des Rules Personnalisées (15 min)

### Objectif

Créer un fichier `.bob/rules.md` qui guide Bob dans votre projet.

### Instructions

1. **Créez le fichier Rules** :

```
Crée .bob/rules.md dans exercices/ex2-rules-personnalises/ avec :

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
```

2. **Testez les Rules** :

```
Demande à Bob de créer un service UserService qui :
- Récupère un utilisateur par ID
- Valide les données
- Gère les erreurs
- Respecte les rules du projet
```

3. **Observez le comportement** :

Bob devrait automatiquement :
- Suivre l'architecture en couches
- Utiliser les conventions de nommage
- Appliquer les bonnes pratiques
- Éviter les anti-patterns listés

### ✅ Critères de Validation

- [ ] Le fichier `.bob/rules.md` est créé
- [ ] Les rules couvrent architecture, conventions et bonnes pratiques
- [ ] Bob respecte les rules dans le code généré
- [ ] Vous comprenez comment les rules influencent Bob

### 💡 Points Clés

Les **Rules** permettent de :
- Communiquer le contexte du projet à Bob
- Définir des standards spécifiques
- Éviter les erreurs courantes
- Maintenir la cohérence architecturale

---

## 📏 Exercice 3 : Skill Avancé avec Workflow (15 min)

### Objectif

Créer un skill qui définit un workflow complet pour le développement.

### Instructions

1. **Créez un skill de workflow** :

```
Crée .bob/skills/tdd-workflow.yaml dans exercices/ex3-skill-avance/ avec :

name: "TDD Workflow"
description: "Workflow Test-Driven Development"
version: "1.0.0"

workflow:
  steps:
    - name: "Écrire le test"
      description: "Créer un test qui échoue"
      action: "create_test"
      
    - name: "Implémenter"
      description: "Écrire le code minimal pour passer le test"
      action: "implement_feature"
      
    - name: "Refactorer"
      description: "Améliorer le code sans casser les tests"
      action: "refactor_code"
      
    - name: "Documenter"
      description: "Ajouter la documentation"
      action: "add_documentation"

test_framework: "pytest"
coverage_minimum: 80

conventions:
  - "Red-Green-Refactor cycle"
  - "Un test par comportement"
  - "Tests lisibles et maintenables"
  - "Mocks pour les dépendances externes"
```

2. **Utilisez le workflow** :

```
Demande à Bob de créer une fonctionnalité "calculer la moyenne d'une liste"
en suivant le workflow TDD défini dans tdd-workflow.yaml
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

1. **Créez une configuration complète** :

```
Dans exercices/ex4-workflow-complet/, crée :

1. .bob/skills/api-development.yaml :
   - Standards pour les API REST
   - Validation des données
   - Gestion d'erreurs
   - Documentation OpenAPI

2. .bob/skills/security.yaml :
   - Bonnes pratiques de sécurité
   - Validation des entrées
   - Authentification/Autorisation
   - Protection contre les vulnérabilités courantes

3. .bob/rules.md :
   - Architecture du projet
   - Stack technique (FastAPI, PostgreSQL, Redis)
   - Conventions de l'équipe
   - Processus de review
```

2. **Créez une API complète** :

```
Demande à Bob de créer une API REST pour gérer des articles de blog avec :
- CRUD complet
- Authentification JWT
- Validation des données
- Tests unitaires et d'intégration
- Documentation OpenAPI
- Respect de tous les skills et rules
```

3. **Analysez le résultat** :

Vérifiez que Bob a :
- Suivi l'architecture définie dans rules.md
- Appliqué les standards de api-development.yaml
- Implémenté les pratiques de security.yaml
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

Créer une bibliothèque de skills réutilisables pour votre équipe.

### Instructions

```
Crée exercices/bonus/skill-library/ avec :

1. skills/languages/
   - python.yaml
   - typescript.yaml
   - java.yaml

2. skills/frameworks/
   - fastapi.yaml
   - react.yaml
   - spring-boot.yaml

3. skills/practices/
   - tdd.yaml
   - clean-code.yaml
   - security.yaml

4. templates/
   - rules-template.md
   - skill-template.yaml

5. README.md :
   - Comment utiliser la bibliothèque
   - Comment contribuer
   - Exemples d'utilisation
```

### Exemples de Skills

**Python Skill** :
```yaml
name: "Python Best Practices"
version: "1.0.0"
language: python
formatter: black
linter: ruff
type_checker: mypy
test_framework: pytest
conventions:
  - "PEP 8 compliance"
  - "Type hints required"
  - "Google-style docstrings"
```

**FastAPI Skill** :
```yaml
name: "FastAPI Development"
version: "1.0.0"
framework: fastapi
patterns:
  - "Dependency injection"
  - "Pydantic models for validation"
  - "Async/await for I/O operations"
  - "OpenAPI documentation"
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

### Skills (.bob/skills/*.yaml)

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

# Valider un fichier YAML
python3 -c "import yaml; print('✅ YAML valide' if yaml.safe_load(open('.bob/skills/mon-skill.yaml')) else '❌ YAML invalide')"
```

### Vérifier les Rules Markdown

```bash
# Vérifier que le fichier existe et est lisible
cat .bob/rules.md | head -10
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