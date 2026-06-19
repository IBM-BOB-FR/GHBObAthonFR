# 📚 Solutions des Exercices - Lab 8

Ce dossier contient les solutions complètes des 4 exercices du Lab 8 sur les Skills et Rules.

---

## 📁 Structure

```
solutions/
├── README.md (ce fichier)
│
├── ex1-premier-skill/                    # Exercice 1 : Premier Skill
│   ├── .bob/
│   │   └── skills/
│   │       └── python-style.md          # ✅ Skill Python
│   ├── test.py                          # ✅ Code : calculate_average()
│   └── messy_code_refactored.py         # ✅ Code refactoré
│
├── ex2-rules-personnalises/              # Exercice 2 : Rules Personnalisées
│   ├── .bob/
│   │   └── rules/
│   │       ├── 01-architecture.md       # ✅ Rules architecture
│   │       ├── 02-conventions.md        # ✅ Rules conventions
│   │       └── 03-bonnes-pratiques.md   # ✅ Rules bonnes pratiques
│   ├── models.py                        # ✅ Modèles de domaine
│   ├── exceptions.py                    # ✅ Exceptions personnalisées
│   ├── user_repository.py               # ✅ Repository pattern
│   ├── user_service.py                  # ✅ Service avec logique métier
│   ├── main.py                          # ✅ API FastAPI complète
│   └── requirements.txt                 # ✅ Dépendances
│
├── ex3-skill-avance/                     # Exercice 3 : TDD Workflow
│   ├── .bob/
│   │   └── skills/
│   │       └── tdd-workflow.md          # ✅ Skill TDD
│   ├── test_average.py                  # ✅ Tests (Red phase)
│   ├── average.py                       # ✅ Implémentation (Green + Refactor)
│   └── requirements.txt                 # ✅ Dépendances
│
└── ex4-workflow-complet/                 # Exercice 4 : API REST Complète
    ├── .bob/
    │   ├── skills/
    │   │   ├── api-development.md       # ✅ Skill API REST
    │   │   └── security.md              # ✅ Skill sécurité
    │   └── rules/
    │       └── 04-api-standards.md      # ✅ Rules standards API
    ├── app/
    │   ├── __init__.py                  # ✅ Package Python
    │   └── config.py                    # ✅ Configuration
    ├── blog_api.py                      # ✅ API complète (704 lignes)
    ├── test_blog_api.py                 # ✅ Tests complets (349 lignes)
    ├── requirements.txt                 # ✅ Dépendances
    ├── .env.example                     # ✅ Configuration exemple
    └── README.md                        # ✅ Documentation
```

---

## 🎯 Exercice 1 : Premier Skill

**Fichiers créés** :
- `ex1-premier-skill/.bob/skills/python-style.md` - Skill Python
- `ex1-premier-skill/test.py` - Fonction calculate_average()
- `ex1-premier-skill/messy_code_refactored.py` - Code refactoré

**Ce que démontre cette solution** :
- ✅ Structure de base d'un skill Markdown
- ✅ Sections : Standards, Conventions, Exemples
- ✅ Préférences de style Python (PEP 8, Black, Ruff)
- ✅ Type hints et docstrings Google style
- ✅ **Code Python généré** suivant le skill
- ✅ **Refactoring** du code legacy

**Points clés** :
- Format Markdown clair et lisible
- Standards de code Python bien définis
- Exemples concrets de code
- **Application pratique** : test.py et messy_code_refactored.py

---

## 📏 Exercice 2 : Rules Personnalisées

**Fichiers créés** :
- `ex2-rules-personnalises/.bob/rules/01-architecture.md` - Rules architecture
- `ex2-rules-personnalises/.bob/rules/02-conventions.md` - Rules conventions
- `ex2-rules-personnalises/.bob/rules/03-bonnes-pratiques.md` - Rules bonnes pratiques
- `ex2-rules-personnalises/models.py` - Modèles de domaine
- `ex2-rules-personnalises/exceptions.py` - Exceptions personnalisées
- `ex2-rules-personnalises/user_repository.py` - Repository pattern
- `ex2-rules-personnalises/user_service.py` - Service avec logique métier
- `ex2-rules-personnalises/main.py` - API FastAPI complète
- `ex2-rules-personnalises/requirements.txt` - Dépendances

**Ce que démontre cette solution** :
- ✅ Organisation des rules en plusieurs fichiers thématiques
- ✅ Architecture en couches clairement définie
- ✅ Conventions de nommage explicites
- ✅ Bonnes pratiques et anti-patterns listés
- ✅ **Code Python complet** : UserService avec FastAPI
- ✅ **Architecture en couches** : Models, Repository, Service, Routes

**Points clés** :
- **Séparation des préoccupations** : Un fichier par thème
- **Ordre alphabétique** : Préfixes 01-, 02-, 03- pour le chargement
- **Application pratique** : API FastAPI fonctionnelle avec 6 fichiers Python
- **Respect des rules** : Architecture, conventions et bonnes pratiques appliquées

---

## 🔧 Exercice 3 : Skill Avancé avec Workflow

**Fichiers créés** :
- `ex3-skill-avance/.bob/skills/tdd-workflow.md` - Skill TDD
- `ex3-skill-avance/test_average.py` - Tests (Red phase)
- `ex3-skill-avance/average.py` - Implémentation (Green + Refactor)
- `ex3-skill-avance/requirements.txt` - Dépendances

**Ce que démontre cette solution** :
- ✅ Skill avec workflow TDD défini
- ✅ Étapes séquentielles (Red-Green-Refactor-Document)
- ✅ Configuration de test (pytest, coverage 80%)
- ✅ **Tests écrits en premier** : test_average.py
- ✅ **Implémentation** : average.py avec docstrings
- ✅ **Cycle TDD complet** démontré

**Points clés** :
- **Workflow structuré** : 4 étapes claires
- **Red phase** : 8 tests dans test_average.py
- **Green phase** : Implémentation minimale
- **Refactor phase** : Code propre avec documentation

---

## 🎯 Exercice 4 : Workflow Complet

**Fichiers créés** :
- `ex4-workflow-complet/.bob/skills/api-development.md` - Skill API REST (138 lignes)
- `ex4-workflow-complet/.bob/skills/security.md` - Skill sécurité (244 lignes)
- `ex4-workflow-complet/.bob/rules/04-api-standards.md` - Rules standards API (268 lignes)
- `ex4-workflow-complet/app/__init__.py` - Package Python
- `ex4-workflow-complet/app/config.py` - Configuration Pydantic
- `ex4-workflow-complet/blog_api.py` - **API complète (704 lignes)**
- `ex4-workflow-complet/test_blog_api.py` - **Tests complets (349 lignes)**
- `ex4-workflow-complet/requirements.txt` - Dépendances
- `ex4-workflow-complet/.env.example` - Configuration exemple
- `ex4-workflow-complet/README.md` - Documentation complète (301 lignes)

**Ce que démontre cette solution** :
- ✅ **API REST complète** pour gestion d'articles de blog
- ✅ **Authentification JWT** avec bcrypt
- ✅ **CRUD complet** : Create, Read, Update, Delete
- ✅ **Architecture en couches** : Models, Repositories, Services, Routes
- ✅ **Validation Pydantic** stricte
- ✅ **Autorisation** : seul l'auteur peut modifier/supprimer
- ✅ **Tests complets** : 15 tests unitaires et d'intégration
- ✅ **Documentation OpenAPI** automatique
- ✅ **Sécurité** : mots de passe hashés, JWT, CORS, validation
- ✅ **Logging** structuré avec contexte
- ✅ **Pagination** des articles
- ✅ **Gestion d'erreurs** complète

**Points clés** :
- **704 lignes de code** dans blog_api.py
- **349 lignes de tests** dans test_blog_api.py
- **Tous les skills et rules appliqués** :
  - python-style.md (Exercice 1)
  - 01-architecture.md, 02-conventions.md, 03-bonnes-pratiques.md (Exercice 2)
  - tdd-workflow.md (Exercice 3)
  - api-development.md, security.md, 04-api-standards.md (Exercice 4)
- **Production-ready** : peut servir de template pour vos projets

**Fonctionnalités** :
- 🔐 Inscription et connexion utilisateur
- 📝 CRUD articles avec autorisation
- 📄 Pagination des résultats
- 🔒 Sécurité : JWT, bcrypt, validation
- 📚 Documentation Swagger/ReDoc
- ✅ Tests avec couverture > 80%
- 🚀 Prêt pour la production
- `ex4-workflow-complet/.bob/skills/security.md`
- `ex4-workflow-complet/.bob/rules/04-api-standards.md`

**Ce que démontre cette solution** :
- ✅ Configuration complète avec plusieurs skills et rules
- ✅ Skill API : architecture, validation, gestion d'erreurs, documentation
- ✅ Skill Security : authentification, autorisation, protection contre vulnérabilités
- ✅ Rules API : stack technique, conventions, processus de review
- ✅ Synergie entre skills (techniques) et rules (contexte projet)

**Points clés** :
- **Séparation des préoccupations** : Un skill par domaine (API, Security)
- **Complémentarité** : Skills réutilisables + Rules spécifiques au projet
- **Exhaustivité** : Couvre tous les aspects d'une API moderne
- **Exemples concrets** : Code FastAPI complet avec bonnes pratiques

---

## 💡 Comment Utiliser Ces Solutions

### 1. Comparer avec Votre Travail

```bash
# Voir la différence entre votre solution et la solution officielle
diff -r .bob/ solutions/ex1-premier-skill/.bob/
```

### 2. Copier pour Tester

```bash
# Copier une solution complète dans votre projet
cp -r solutions/ex1-premier-skill/.bob .

# Ou copier un fichier spécifique
cp solutions/ex1-premier-skill/.bob/skills/python-style.md .bob/skills/
```

### 3. Adapter à Vos Besoins

Les solutions sont des **exemples de référence**, pas des réponses uniques :
- Modifiez les conventions selon votre équipe
- Ajoutez des sections spécifiques à votre projet
- Combinez plusieurs skills selon vos besoins
- Adaptez les rules à votre contexte

---

## 🎓 Points d'Apprentissage

### Skills (Markdown)

**Format** :
```markdown
# Titre du Skill

Description du skill.

## Section 1

Contenu...

## Section 2

Contenu...

## Exemples

```code
exemple
```
```

**Bonnes pratiques** :
- Un skill = un domaine précis (Python, API, Security, TDD)
- Structure claire avec sections logiques
- Exemples de code concrets
- Instructions actionnables

### Rules (Markdown organisé en répertoire)

**Format** :
```markdown
# Titre de la Rule

## Section 1
Contenu...

## Section 2
Contenu...
```

**Bonnes pratiques** :
- Organiser en plusieurs fichiers thématiques
- Utiliser des préfixes numériques (01-, 02-, 03-)
- Soyez spécifique et concis
- Listez ce qu'il faut faire ET éviter

### Combinaison Skills + Rules

**Principe** :
- **Skills** = Configuration technique réutilisable (comment faire)
- **Rules** = Contexte et décisions spécifiques au projet (pourquoi et quand)
- **Ensemble** = Bob personnalisé pour votre projet

**Exemple de synergie** :
```
Skill (api-development.md)          Rules (04-api-standards.md)
         ↓                                    ↓
   "Utiliser FastAPI"              "Stack: FastAPI 0.100+"
   "Valider avec Pydantic"         "Projet: API de blog"
   "Documentation OpenAPI"         "Versioning: /api/v1/"
         ↓                                    ↓
              ↘                          ↙
                Bob comprend tout :
            - Framework : FastAPI 0.100+
            - Validation : Pydantic v2
            - Contexte : Blog API
            - Structure : /api/v1/articles
```

---

## 🔍 Vérification

### Checklist de Validation

Pour chaque solution, vérifiez :

**Skills** :
- [ ] Format Markdown valide
- [ ] Structure claire avec sections logiques
- [ ] Conventions claires et actionnables
- [ ] Exemples de code fournis

**Rules** :
- [ ] Format Markdown valide
- [ ] Sections organisées logiquement
- [ ] Instructions claires et spécifiques
- [ ] Exemples concrets fournis
- [ ] Organisation en fichiers thématiques (pour ex2 et ex4)

**Intégration** :
- [ ] Skills et rules sont complémentaires
- [ ] Pas de contradiction entre eux
- [ ] Couvrent les aspects importants du projet
- [ ] Peuvent être utilisés ensemble par Bob

---

## 🚀 Aller Plus Loin

### Exercices Supplémentaires

1. **Créez vos propres skills** pour :
   - Votre langage préféré (TypeScript, Java, Go)
   - Votre framework favori (React, Spring Boot, Django)
   - Vos pratiques d'équipe (code review, CI/CD)

2. **Écrivez des rules** pour :
   - Un projet personnel
   - Un projet d'équipe
   - Un projet open source

3. **Combinez** :
   - Plusieurs skills dans un projet
   - Skills génériques + rules spécifiques
   - Créez une bibliothèque de skills réutilisables

### Ressources

- **Documentation Skills** : https://bob.ibm.com/docs/ide/features/skills
- **Documentation Rules** : https://bob.ibm.com/docs/ide/configuration/rules
- **Exemples** : Consultez le dossier `exemples/` du lab
- **README principal** : `labs/lab8-skills-et-rules/README.md`

---

## 💬 Questions Fréquentes

**Q: Mes solutions sont différentes, est-ce grave ?**  
R: Non ! Il n'y a pas UNE seule bonne réponse. L'important est que vos skills/rules soient valides, clairs et utiles pour votre projet.

**Q: Dois-je utiliser Markdown ou YAML pour les skills ?**  
R: Les deux fonctionnent ! Markdown est plus flexible et lisible. YAML est plus structuré. Choisissez selon vos préférences.

**Q: Combien de skills dois-je avoir ?**  
R: Commencez avec 1-2 skills de base, puis ajoutez selon vos besoins. Qualité > Quantité.

**Q: Les rules doivent-elles être longues ?**  
R: Non ! Des rules courtes et percutantes (10-20 lignes) peuvent être très efficaces. Voir `exemples/rules/ai-rag-hygiene.md` (10 lignes).

**Q: Puis-je combiner plusieurs fichiers de rules ?**  
R: Oui ! C'est même recommandé. Organisez vos rules en plusieurs fichiers thématiques (architecture, conventions, sécurité, etc.) comme dans l'exercice 2.

**Q: Comment Bob charge-t-il les fichiers de rules ?**  
R: Bob charge tous les fichiers `.md` dans `.bob/rules/` par ordre alphabétique. C'est pourquoi on utilise des préfixes numériques (01-, 02-, 03-).

---

## 📊 Comparaison des Exercices

| Exercice | Complexité | Skills | Rules | Cas d'usage |
|----------|------------|--------|-------|-------------|
| Ex 1 | ⭐ Simple | 1 skill basique | - | Apprendre la structure d'un skill |
| Ex 2 | ⭐⭐ Moyen | - | 3 rules organisées | Apprendre l'organisation des rules |
| Ex 3 | ⭐⭐ Moyen | 1 skill avec workflow | - | Définir un processus de développement |
| Ex 4 | ⭐⭐⭐ Avancé | 2 skills + 1 rule | Combinaison complète | Projet réel avec API |

---

## ✅ Auto-Évaluation

Après avoir étudié les solutions, vérifiez que vous maîtrisez :

### Compréhension
- [ ] Je comprends la différence entre skills et rules
- [ ] Je sais quand utiliser un skill vs une rule
- [ ] Je comprends l'organisation en fichiers multiples
- [ ] Je comprends la synergie skills + rules

### Pratique
- [ ] Je peux créer un skill Markdown valide
- [ ] Je peux créer des rules organisées en fichiers
- [ ] Je peux combiner skills et rules efficacement
- [ ] Je peux adapter les solutions à mon projet

### Application
- [ ] J'ai testé les solutions avec Bob
- [ ] J'ai adapté au moins une solution à mes besoins
- [ ] Je peux créer mes propres skills/rules
- [ ] Je peux partager mes configurations avec l'équipe

---

**Bravo d'avoir complété le Lab 8 ! Vous maîtrisez maintenant Skills et Rules ! 🎉**

---

_Solutions créées pour le Bobathon 2026_