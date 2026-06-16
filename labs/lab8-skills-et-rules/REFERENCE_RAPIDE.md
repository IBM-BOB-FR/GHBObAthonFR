# 📖 Référence Rapide : Skills et Rules de Bob

## 🧠 Qu'est-ce qu'un Skill ?

Un **Skill** est un fichier de configuration YAML (`.bob/skills/*.yaml`) qui définit des comportements, standards et préférences pour Bob.

### Structure d'un Skill

```yaml
name: "Nom du Skill"
description: "Description de ce que fait ce skill"
version: "1.0.0"

# Configuration spécifique
config:
  # Vos paramètres ici
```

### Exemples de Skills

#### 1. Skill de Style Python

```yaml
name: "Python Style Guide"
version: "1.0.0"
language: python
formatter: black
linter: ruff
type_hints: required
docstring_style: "Google"
max_line_length: 88
```

#### 2. Skill de Framework

```yaml
name: "FastAPI Development"
version: "1.0.0"
framework: fastapi
architecture: "Layered"
async_by_default: true
validation: pydantic
documentation: openapi
```

#### 3. Skill de Workflow TDD

```yaml
name: "TDD Workflow"
version: "1.0.0"
workflow:
  steps:
    - name: "Write Test"
      action: "create_test"
    - name: "Implement"
      action: "implement_feature"
    - name: "Refactor"
      action: "refactor_code"
test_framework: pytest
coverage_minimum: 80
```

---

## 📏 Qu'est-ce qu'un fichier Rules ?

Le fichier **Rules** (`.bob/rules.md`) contient des instructions en langage naturel qui guident Bob dans votre projet.

### Structure d'un fichier Rules

```markdown
# Règles du Projet

## Architecture
[Description de l'architecture]

## Conventions de Code
[Vos conventions]

## Bonnes Pratiques
[Ce qu'il faut faire]

## Ce qu'il faut éviter
[Ce qu'il ne faut pas faire]
```

### Exemple de Rules

```markdown
# Règles du Projet

## Architecture

Ce projet suit une architecture en couches :
- Routes : Endpoints API uniquement
- Services : Toute la logique métier
- Repositories : Accès aux données uniquement

## Conventions de Nommage

- Classes : PascalCase
- Fonctions : snake_case
- Constantes : UPPER_SNAKE_CASE

## Bonnes Pratiques

- Toujours valider les entrées utilisateur
- Utiliser des type hints partout
- Logger les erreurs avec le contexte
- Écrire des tests pour chaque fonctionnalité

## Ce qu'il faut éviter

- Pas de logique métier dans les routes
- Pas de secrets en dur dans le code
- Pas de print() pour le debug
```

---

## 🎯 Quand Utiliser Skills vs Rules ?

### Utilisez un **Skill** pour :

✅ Définir des standards techniques (formatage, linting)  
✅ Configurer des outils et frameworks  
✅ Créer des workflows réutilisables  
✅ Partager des configurations entre projets  
✅ Automatiser des patterns de code

**Exemple** : "Utilise toujours Black avec une ligne max de 88 caractères"

### Utilisez des **Rules** pour :

✅ Décrire l'architecture du projet  
✅ Définir des conventions d'équipe  
✅ Expliquer le contexte métier  
✅ Spécifier des contraintes spécifiques  
✅ Documenter les décisions techniques

**Exemple** : "Dans ce projet, les services ne doivent jamais accéder directement à la base de données, ils doivent passer par les repositories"

---

## 🔄 Combiner Skills et Rules

### Approche Recommandée

```
Skills (YAML)                Rules (Markdown)
     ↓                             ↓
Configuration                Instructions
technique                    contextuelles
     ↓                             ↓
        ↘                     ↙
          Bob Personnalisé
                ↓
        Code de Qualité
```

### Exemple Complet

**Skill** : `.bob/skills/python-api.yaml`
```yaml
name: "Python API Development"
language: python
framework: fastapi
formatter: black
linter: ruff
type_hints: required
async_by_default: true
```

**Rules** : `.bob/rules.md`
```markdown
# Règles du Projet API E-commerce

## Architecture
- Layered architecture (Routes → Services → Repositories)
- Pas de logique métier dans les routes

## Sécurité
- JWT pour l'authentification
- Bcrypt pour les mots de passe
- Validation stricte des entrées

## Performance
- Caching Redis pour les données fréquentes
- Pagination obligatoire (max 100 items)
```

**Résultat** : Bob appliquera automatiquement le formatage Black, utilisera FastAPI avec async/await, ET respectera votre architecture en couches et vos règles de sécurité.

---

## 💡 Commandes Utiles

### Créer un Skill

```bash
# Créer le répertoire
mkdir -p .bob/skills

# Créer un skill
cat > .bob/skills/mon-skill.yaml << EOF
name: "Mon Skill"
version: "1.0.0"
# Configuration...
EOF
```

### Créer des Rules

```bash
# Créer le fichier rules
cat > .bob/rules.md << EOF
# Règles du Projet

## Architecture
...

## Conventions
...
EOF
```

### Demander à Bob d'utiliser vos Skills/Rules

```
"Crée une API REST en respectant les skills et rules du projet"

"Génère un service UserService qui suit nos conventions"

"Refactorise ce code selon nos standards définis dans les skills"
```

---

## 📚 Exemples de Skills par Domaine

### Langages

- `python-best-practices.yaml` : Standards Python
- `typescript-strict.yaml` : TypeScript en mode strict
- `java-spring.yaml` : Conventions Spring Boot

### Frameworks

- `fastapi-development.yaml` : API REST avec FastAPI
- `react-typescript.yaml` : React avec TypeScript
- `django-rest.yaml` : Django REST Framework

### Pratiques

- `tdd-workflow.yaml` : Test-Driven Development
- `clean-code.yaml` : Principes Clean Code
- `security-first.yaml` : Sécurité en priorité

### Outils

- `git-workflow.yaml` : Workflow Git
- `ci-cd-pipeline.yaml` : Pipeline CI/CD
- `docker-compose.yaml` : Configuration Docker

---

## 📝 Templates

### Template Skill Minimal

```yaml
name: "Nom du Skill"
description: "Description courte"
version: "1.0.0"

# Ajoutez votre configuration ici
```

### Template Skill Complet

```yaml
name: "Nom du Skill"
description: "Description détaillée"
version: "1.0.0"
author: "Votre Nom"
tags: ["python", "api", "fastapi"]

# Configuration
language: python
framework: fastapi

# Outils
tools:
  formatter: black
  linter: ruff
  test_framework: pytest

# Conventions
conventions:
  - "Convention 1"
  - "Convention 2"

# Patterns
patterns:
  - name: "Pattern Name"
    description: "Description"

# Ce qu'il faut éviter
avoid:
  - "Anti-pattern 1"
  - "Anti-pattern 2"
```

### Template Rules Minimal

```markdown
# Règles du Projet

## Architecture
[Description]

## Conventions
[Liste des conventions]

## Bonnes Pratiques
[Ce qu'il faut faire]
```

### Template Rules Complet

```markdown
# Règles du Projet [Nom]

## 📋 Vue d'Ensemble
[Description du projet]

## 🏗️ Architecture
[Architecture technique]

## 📝 Conventions de Code
### Nommage
[Conventions de nommage]

### Style
[Style de code]

## 🔒 Sécurité
[Règles de sécurité]

## 🧪 Tests
[Stratégie de tests]

## 📊 Base de Données
[Conventions DB]

## ⚡ Performance
[Optimisations]

## ❌ Ce qu'il faut ÉVITER
[Anti-patterns]

## ✅ Checklist
[Checklist avant commit]
```

---

## 🎓 Bonnes Pratiques

### Pour les Skills

1. **Un skill = un domaine** : Ne mélangez pas Python et React dans le même skill
2. **Versionnez** : Utilisez semantic versioning (1.0.0, 1.1.0, 2.0.0)
3. **Documentez** : Ajoutez une description claire
4. **Testez** : Vérifiez que Bob applique bien le skill
5. **Partagez** : Créez une bibliothèque d'équipe

### Pour les Rules

1. **Soyez spécifique** : "Utiliser FastAPI" > "Utiliser un framework"
2. **Soyez concis** : Évitez les pavés de texte
3. **Priorisez** : Mettez les règles importantes en premier
4. **Illustrez** : Donnez des exemples concrets
5. **Maintenez** : Mettez à jour avec le projet

### Pour l'Intégration

1. **Commencez simple** : Un skill + quelques rules
2. **Itérez** : Ajoutez progressivement
3. **Mesurez** : Vérifiez l'impact sur la qualité
4. **Documentez** : Expliquez à l'équipe
5. **Évoluez** : Adaptez selon les besoins

---

## 🚀 Workflow Recommandé

### 1. Nouveau Projet

```bash
# Créer la structure
mkdir -p .bob/skills
touch .bob/rules.md

# Créer un skill de base
# Écrire les rules initiales
# Tester avec Bob
```

### 2. Projet Existant

```bash
# Analyser le code existant
# Identifier les patterns
# Créer des skills correspondants
# Documenter dans rules.md
```

### 3. Équipe

```bash
# Créer un repo de skills partagés
# Définir des rules communes
# Documenter l'utilisation
# Former l'équipe
```

---

## 🔍 Debugging

### Bob n'applique pas mon skill

✅ Vérifiez que le fichier est dans `.bob/skills/`  
✅ Vérifiez la syntaxe YAML  
✅ Vérifiez que le skill est pertinent pour la tâche  
✅ Demandez explicitement : "en utilisant le skill X"

### Bob ignore mes rules

✅ Vérifiez que le fichier est `.bob/rules.md`  
✅ Vérifiez que les rules sont claires  
✅ Soyez plus spécifique dans vos demandes  
✅ Rappelez les rules : "selon nos rules"

### Conflit entre skill et rules

✅ Les rules sont plus spécifiques et prioritaires  
✅ Clarifiez dans les rules en cas de conflit  
✅ Mettez à jour le skill si nécessaire

---

## 📚 Ressources

### Documentation Officielle

- **Skills** : https://internal.bob.ibm.com/docs/ide/features/skills
- **Rules** : https://internal.bob.ibm.com/docs/ide/configuration/rules
- **Configuration** : https://internal.bob.ibm.com/docs/ide/configuration

### Exemples

Consultez le dossier `exemples/` du lab :
- `exemples/skills/` : Skills pour Python, FastAPI, etc.
- `exemples/rules/` : Rules pour différents types de projets

### Vidéos

- [Compétences vs modes vs règles](https://www.youtube.com/watch?v=example)

---

## 🎯 Checklist de Maîtrise

### Skills
- [ ] Je comprends ce qu'est un skill
- [ ] Je sais créer un fichier skill YAML
- [ ] Je peux définir des configurations techniques
- [ ] Je sais créer des workflows
- [ ] Je comprends comment partager des skills

### Rules
- [ ] Je comprends ce qu'est le fichier rules.md
- [ ] Je sais écrire des rules claires
- [ ] Je peux définir l'architecture
- [ ] Je sais spécifier des conventions
- [ ] Je comprends comment les rules influencent Bob

### Intégration
- [ ] Je peux combiner skills et rules
- [ ] Je sais créer une configuration complète
- [ ] Je comprends les bénéfices
- [ ] Je peux créer des configurations réutilisables

---

## 💬 FAQ

**Q: Quelle est la différence entre skills et rules ?**  
R: Skills = configuration technique (YAML), Rules = instructions contextuelles (Markdown)

**Q: Puis-je avoir plusieurs skills ?**  
R: Oui ! Créez un skill par domaine (langage, framework, pratique)

**Q: Les rules remplacent-elles les skills ?**  
R: Non, ils sont complémentaires. Skills = "comment", Rules = "pourquoi et quoi"

**Q: Comment partager mes skills avec l'équipe ?**  
R: Créez un repo Git avec vos skills et clonez-le dans `.bob/skills/`

**Q: Bob utilise-t-il toujours mes skills/rules ?**  
R: Oui, automatiquement. Vous pouvez aussi les mentionner explicitement.

---

_Référence créée pour le Bobathon 2026_