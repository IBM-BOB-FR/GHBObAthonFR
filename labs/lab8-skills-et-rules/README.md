# 🎯 Lab 8 : Skills et Rules - Les Super-Pouvoirs de Bob

> **Durée estimée** : 45-60 minutes  
> **Difficulté** : ⭐⭐ Intermédiaire  
> **Objectif** : Maîtriser les fonctionnalités avancées "skills" et "rules" de Bob

---

## 📋 Objectifs d'Apprentissage

À la fin de ce lab, vous serez capable de :

- ✅ Comprendre comment Bob utilise ses "skills" (compétences)
- ✅ Exploiter les "rules" (règles) pour guider Bob
- ✅ Optimiser vos interactions avec Bob
- ✅ Créer des workflows efficaces
- ✅ Utiliser les capacités avancées de Bob

---

## 🧠 Qu'est-ce que les "Skills" de Bob ?

Les **skills** sont les compétences intégrées de Bob qui lui permettent de :

1. **Analyser du code** : Comprendre la structure, identifier les problèmes
2. **Générer du code** : Créer du code de qualité dans plusieurs langages
3. **Refactorer** : Améliorer le code existant sans changer son comportement
4. **Tester** : Créer et exécuter des tests
5. **Documenter** : Générer de la documentation claire
6. **Déboguer** : Identifier et corriger les bugs
7. **Optimiser** : Améliorer les performances
8. **Architecturer** : Concevoir des solutions robustes

---

## 📏 Qu'est-ce que les "Rules" de Bob ?

Les **rules** sont les règles de fonctionnement de Bob :

1. **Un outil par message** : Bob utilise exactement un outil à la fois
2. **Validation systématique** : Vous devez confirmer chaque action
3. **Lecture groupée** : Bob peut lire jusqu'à 5 fichiers simultanément
4. **Modifications ciblées** : Préférence pour `apply_diff` sur `write_to_file`
5. **Clarté avant action** : Bob pose des questions si besoin
6. **Pas de suppositions** : Bob attend la confirmation avant de continuer
7. **Contexte complet** : Bob lit tous les fichiers nécessaires avant de modifier

---

## 🚀 Mise en Place

### Prérequis

- Avoir complété les Labs 1 et 2
- Comprendre les bases de Python
- Environnement virtuel activé

### Structure du Lab

```
lab8-skills-et-rules/
├── README.md (ce fichier)
├── exercices/
│   ├── ex1-skills-analyse/
│   ├── ex2-skills-generation/
│   ├── ex3-rules-workflow/
│   └── ex4-optimisation/
└── solutions/ (à créer par Bob)
```

---

## 📝 Exercice 1 : Skills - Analyse de Code (15 min)

### Objectif

Découvrir comment Bob analyse et comprend le code.

### Instructions

1. **Créez un fichier avec du code problématique** :

```
Crée exercices/ex1-skills-analyse/messy_code.py avec ce contenu :

def calc(a,b,c):
    x=a+b
    y=x*c
    z=y/2
    return z

def process(data):
    result=[]
    for i in range(len(data)):
        if data[i]>0:
            result.append(data[i]*2)
    return result

class User:
    def __init__(self,n,e,a):
        self.n=n
        self.e=e
        self.a=a
    def get_info(self):
        return self.n+' '+self.e+' '+str(self.a)
```

2. **Demandez une analyse complète** :

```
Analyse @messy_code.py et identifie TOUS les problèmes :
- Nommage
- Style (PEP 8)
- Lisibilité
- Performance
- Bonnes pratiques
- Documentation manquante

Pour chaque problème, explique pourquoi c'est un problème et comment le corriger.
```

3. **Observez les skills de Bob** :
   - Analyse syntaxique
   - Détection de code smells
   - Suggestions d'amélioration
   - Explications pédagogiques

### ✅ Critères de Validation

- [ ] Bob identifie au moins 10 problèmes différents
- [ ] Les explications sont claires et détaillées
- [ ] Bob propose des solutions concrètes
- [ ] Vous comprenez chaque problème identifié

### 💡 Points Clés

Bob utilise ses **skills d'analyse** pour :
- Détecter les violations de conventions
- Identifier les anti-patterns
- Suggérer des améliorations
- Expliquer le "pourquoi" derrière chaque recommandation

---

## 🔨 Exercice 2 : Skills - Génération de Code (15 min)

### Objectif

Explorer comment Bob génère du code de qualité.

### Instructions

1. **Demandez à Bob de créer une application complète** :

```
Crée une application de gestion de tâches dans exercices/ex2-skills-generation/ avec :

1. Un modèle Task avec :
   - id (UUID)
   - title (str)
   - description (str)
   - status (enum: TODO, IN_PROGRESS, DONE)
   - priority (enum: LOW, MEDIUM, HIGH)
   - created_at (datetime)
   - updated_at (datetime)

2. Un TaskManager avec :
   - Ajouter une tâche
   - Modifier une tâche
   - Supprimer une tâche
   - Lister les tâches (avec filtres par status et priority)
   - Marquer comme terminée
   - Statistiques (nombre par status, par priority)

3. Exigences de qualité :
   - Type hints partout
   - Docstrings Google style
   - Validation des données
   - Gestion d'erreurs avec exceptions personnalisées
   - Tests unitaires complets (pytest)
   - Logging approprié

4. Fichiers à créer :
   - models.py (modèles de données)
   - manager.py (logique métier)
   - exceptions.py (exceptions personnalisées)
   - test_manager.py (tests)
   - README.md (documentation)
```

2. **Observez les skills de génération** :
   - Structure du code
   - Qualité du code généré
   - Respect des bonnes pratiques
   - Documentation intégrée

3. **Testez l'application** :

```
Exécute les tests et montre-moi les résultats
```

### ✅ Critères de Validation

- [ ] Code généré de haute qualité
- [ ] Type hints et docstrings présents
- [ ] Tests passent avec succès
- [ ] Architecture claire et maintenable
- [ ] Documentation complète

### 💡 Points Clés

Bob utilise ses **skills de génération** pour :
- Créer du code structuré et propre
- Appliquer automatiquement les bonnes pratiques
- Générer des tests pertinents
- Produire de la documentation claire

---

## 📏 Exercice 3 : Rules - Workflow Optimal (15 min)

### Objectif

Comprendre et appliquer les règles de Bob pour un workflow efficace.

### Instructions

1. **Créez un scénario complexe** :

```
Crée exercices/ex3-rules-workflow/ avec une API REST Flask :

Structure :
- app.py (application Flask)
- models.py (modèles SQLAlchemy)
- routes.py (endpoints)
- config.py (configuration)
- requirements.txt

L'API doit gérer des articles de blog avec :
- CRUD complet
- Authentification JWT
- Validation des données
- Tests d'API
```

2. **Observez comment Bob applique ses rules** :

   **Rule 1 : Un outil par message**
   - Bob crée un fichier à la fois
   - Vous validez chaque étape

   **Rule 2 : Lecture groupée**
   - Demandez : "Lis tous les fichiers de l'API ensemble"
   - Bob lit jusqu'à 5 fichiers en une fois

   **Rule 3 : Modifications ciblées**
   - Demandez une modification : "Ajoute un endpoint de recherche"
   - Bob utilise `apply_diff` pour des changements précis

3. **Testez le workflow optimal** :

```
Maintenant, améliore l'API en ajoutant :
- Pagination sur la liste des articles
- Filtrage par catégorie
- Tri par date ou popularité

Utilise le workflow le plus efficace possible.
```

4. **Analysez le processus** :
   - Combien d'étapes Bob a-t-il utilisées ?
   - A-t-il lu les fichiers nécessaires avant de modifier ?
   - A-t-il utilisé les bons outils ?

### ✅ Critères de Validation

- [ ] Bob respecte la règle "un outil par message"
- [ ] Bob lit les fichiers nécessaires avant de modifier
- [ ] Bob utilise `apply_diff` pour les modifications ciblées
- [ ] Le workflow est efficace et logique
- [ ] Vous comprenez pourquoi chaque rule existe

### 💡 Points Clés

Les **rules de Bob** garantissent :
- **Sécurité** : Validation avant chaque action
- **Efficacité** : Lecture groupée pour le contexte
- **Précision** : Modifications ciblées pour éviter les erreurs
- **Clarté** : Un outil = une action = facile à suivre

---

## 🎯 Exercice 4 : Optimisation - Combiner Skills et Rules (15 min)

### Objectif

Maîtriser l'utilisation combinée des skills et rules pour un résultat optimal.

### Instructions

1. **Créez un projet legacy** :

```
Crée exercices/ex4-optimisation/legacy/ avec :

1. Un fichier data_processor.py mal écrit :
   - Pas de type hints
   - Fonctions trop longues
   - Code dupliqué
   - Pas de tests
   - Pas de documentation

2. Un fichier api.py avec :
   - Endpoints non sécurisés
   - Pas de validation
   - Gestion d'erreurs basique
   - Performance non optimisée
```

2. **Demandez une refonte complète** :

```
Je veux refactorer complètement ce projet en utilisant tes meilleurs skills.

Étape 1 : Analyse
- Lis tous les fichiers ensemble
- Identifie tous les problèmes
- Propose un plan de refactoring détaillé

Étape 2 : Refactoring
- Applique les améliorations par ordre de priorité
- Utilise les design patterns appropriés
- Ajoute tests et documentation

Étape 3 : Optimisation
- Améliore les performances
- Ajoute du caching si pertinent
- Optimise les requêtes

Étape 4 : Documentation
- Crée un BEFORE_AFTER.md comparant l'ancien et le nouveau code
- Documente les choix d'architecture
- Explique les améliorations de performance
```

3. **Observez la synergie skills + rules** :
   - Bob lit tous les fichiers (rule : lecture groupée)
   - Bob analyse en profondeur (skill : analyse)
   - Bob propose un plan (skill : architecture)
   - Bob applique les changements un par un (rule : un outil par message)
   - Bob valide à chaque étape (rule : validation)

### ✅ Critères de Validation

- [ ] Analyse complète et pertinente
- [ ] Plan de refactoring logique
- [ ] Refactoring appliqué avec succès
- [ ] Tests passent
- [ ] Documentation claire des améliorations
- [ ] Vous comprenez comment skills et rules travaillent ensemble

### 💡 Points Clés

La **combinaison skills + rules** permet :
- **Qualité** : Skills assurent l'excellence technique
- **Sécurité** : Rules assurent le contrôle et la validation
- **Efficacité** : Workflow optimisé
- **Confiance** : Vous gardez le contrôle à chaque étape

---

## 🎓 Exercice Bonus : Créer Votre Propre Workflow (Optionnel)

### Mission

Créez un workflow personnalisé qui exploite au maximum les skills et rules de Bob.

### Instructions

```
Crée un projet de ton choix dans exercices/bonus/ qui :

1. Utilise au moins 5 skills différents de Bob :
   - Analyse
   - Génération
   - Refactoring
   - Tests
   - Documentation
   - Optimisation
   - Architecture
   - Débogage

2. Respecte toutes les rules de Bob :
   - Un outil par message
   - Validation systématique
   - Lecture groupée
   - Modifications ciblées
   - Clarté avant action

3. Documente ton workflow dans WORKFLOW.md :
   - Étapes suivies
   - Skills utilisés à chaque étape
   - Rules appliquées
   - Résultats obtenus
   - Leçons apprises
```

### Exemples de Projets

- **API de recommandation** : ML + API + Tests
- **Système de monitoring** : Logging + Métriques + Dashboard
- **CLI avancé** : Parsing + Validation + Help
- **Microservice** : Docker + K8s + CI/CD

---

## 📊 Auto-Évaluation

Vérifiez que vous maîtrisez :

### Skills de Bob

- [ ] Je comprends comment Bob analyse le code
- [ ] Je sais exploiter ses capacités de génération
- [ ] Je peux lui demander de refactorer efficacement
- [ ] Je comprends ses skills de test et documentation
- [ ] Je sais quand utiliser quel skill

### Rules de Bob

- [ ] Je comprends pourquoi "un outil par message"
- [ ] Je sais utiliser la lecture groupée (5 fichiers max)
- [ ] Je préfère apply_diff pour les modifications
- [ ] Je valide systématiquement les actions
- [ ] Je fournis le contexte nécessaire

### Workflow

- [ ] Je peux créer un workflow efficace
- [ ] Je combine skills et rules intelligemment
- [ ] Je garde le contrôle du processus
- [ ] Je sais optimiser mes interactions avec Bob

---

## 🎓 Ce que Vous Avez Appris

### Les 8 Skills Principaux de Bob

1. **Analyse** 🔍
   - Détection de code smells
   - Identification de problèmes
   - Suggestions d'amélioration

2. **Génération** ✨
   - Code de qualité
   - Respect des conventions
   - Documentation intégrée

3. **Refactoring** 🔧
   - Amélioration sans casser
   - Design patterns
   - Optimisation

4. **Tests** 🧪
   - Tests unitaires
   - Tests d'intégration
   - Couverture de code

5. **Documentation** 📚
   - Docstrings
   - README
   - Architecture

6. **Débogage** 🐛
   - Identification de bugs
   - Correction
   - Prévention

7. **Optimisation** ⚡
   - Performance
   - Mémoire
   - Scalabilité

8. **Architecture** 🏗️
   - Design de solutions
   - Patterns
   - Best practices

### Les 7 Rules Essentielles

1. **Un outil par message** : Clarté et contrôle
2. **Validation systématique** : Sécurité
3. **Lecture groupée** : Contexte complet
4. **Modifications ciblées** : Précision
5. **Clarté avant action** : Pas de suppositions
6. **Pas de suppositions** : Questions si besoin
7. **Contexte complet** : Lecture avant modification

---

## 💡 Conseils pour Maximiser Bob

### Pour les Skills

1. **Soyez spécifique** : "Analyse les performances" vs "Analyse le code"
2. **Demandez des explications** : "Pourquoi ce pattern ?"
3. **Itérez** : Affinez progressivement
4. **Combinez** : Utilisez plusieurs skills ensemble

### Pour les Rules

1. **Anticipez** : Listez les fichiers à lire ensemble
2. **Validez rapidement** : Ne bloquez pas le workflow
3. **Utilisez apply_diff** : Plus sûr que write_to_file
4. **Donnez du contexte** : Expliquez l'objectif global

### Workflow Optimal

```
1. Analyse (skill) → Lecture groupée (rule)
2. Plan (skill) → Validation (rule)
3. Implémentation (skill) → Un outil par message (rule)
4. Tests (skill) → Validation (rule)
5. Documentation (skill) → Modifications ciblées (rule)
```

---

## 🚀 Prochaines Étapes

Vous maîtrisez maintenant les skills et rules de Bob !

### Continuez à Pratiquer

- Appliquez ces concepts dans vos projets réels
- Expérimentez avec différents workflows
- Partagez vos découvertes avec l'équipe

### Explorez Plus Loin

- **Lab 6** : Custom MCP Modes (modes personnalisés)
- **Lab 7** : DevOps Automation (automatisation)
- **Projets réels** : Appliquez Bob à votre travail quotidien

---

## 📚 Récapitulatif des Commandes Utiles

### Exploiter les Skills

```
# Analyse approfondie
"Analyse @fichier.py en détail et identifie tous les problèmes"

# Génération de qualité
"Crée une classe User avec validation, type hints et tests"

# Refactoring intelligent
"Refactorise @code.py en appliquant le Strategy Pattern"

# Tests complets
"Crée des tests unitaires avec au moins 90% de couverture"

# Documentation claire
"Documente cette API avec des exemples d'utilisation"
```

### Respecter les Rules

```
# Lecture groupée
"Lis @app.py, @models.py et @config.py ensemble"

# Modifications ciblées
"Ajoute une méthode validate() à la classe User dans @models.py"

# Validation explicite
Toujours confirmer après chaque action de Bob

# Contexte complet
"Avant de modifier, lis tous les fichiers du module auth/"
```

---

## 🎯 Challenge Final

Créez un projet complet qui démontre votre maîtrise :

1. **Utilisez tous les skills** de Bob
2. **Respectez toutes les rules**
3. **Documentez votre workflow**
4. **Partagez vos résultats**

**Bravo ! Vous êtes maintenant un expert Bob !** 🎉

---

_Lab créé pour le Bobathon 2026_