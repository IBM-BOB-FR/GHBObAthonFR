# 📖 Référence Rapide : Skills et Rules de Bob

## 🧠 Les 8 Skills de Bob

### 1. 🔍 Analyse
**Quand l'utiliser** : Pour comprendre du code existant, identifier des problèmes

**Exemples de commandes** :
```
"Analyse @fichier.py et identifie tous les code smells"
"Quels sont les problèmes de performance dans @app.py ?"
"Analyse l'architecture de ce projet"
```

**Ce que Bob fait** :
- Détecte les violations de conventions (PEP 8, etc.)
- Identifie les anti-patterns
- Repère les problèmes de sécurité
- Suggère des améliorations

---

### 2. ✨ Génération
**Quand l'utiliser** : Pour créer du nouveau code de qualité

**Exemples de commandes** :
```
"Crée une classe User avec validation et type hints"
"Génère une API REST pour gérer des produits"
"Crée des tests unitaires pour @calculator.py"
```

**Ce que Bob fait** :
- Génère du code propre et structuré
- Applique automatiquement les bonnes pratiques
- Ajoute type hints et docstrings
- Crée des tests pertinents

---

### 3. 🔧 Refactoring
**Quand l'utiliser** : Pour améliorer du code existant sans changer son comportement

**Exemples de commandes** :
```
"Refactorise @legacy.py en appliquant le Strategy Pattern"
"Améliore la lisibilité de @messy_code.py"
"Extrais les méthodes trop longues dans @service.py"
```

**Ce que Bob fait** :
- Applique des design patterns
- Extrait des méthodes/classes
- Élimine la duplication
- Améliore la structure

---

### 4. 🧪 Tests
**Quand l'utiliser** : Pour créer ou améliorer des tests

**Exemples de commandes** :
```
"Crée des tests unitaires pour @models.py"
"Ajoute des tests d'intégration pour l'API"
"Améliore la couverture de tests à 90%"
```

**Ce que Bob fait** :
- Crée des tests unitaires
- Génère des tests d'intégration
- Utilise pytest, unittest, etc.
- Vérifie la couverture

---

### 5. 📚 Documentation
**Quand l'utiliser** : Pour documenter du code ou des projets

**Exemples de commandes** :
```
"Ajoute des docstrings Google style à @utils.py"
"Crée un README.md pour ce projet"
"Documente l'API avec des exemples d'utilisation"
```

**Ce que Bob fait** :
- Ajoute des docstrings
- Crée des README
- Génère de la documentation API
- Ajoute des commentaires pertinents

---

### 6. 🐛 Débogage
**Quand l'utiliser** : Pour identifier et corriger des bugs

**Exemples de commandes** :
```
"Pourquoi cette fonction retourne None ?"
"Débogue l'erreur dans @app.py ligne 42"
"Trouve pourquoi les tests échouent"
```

**Ce que Bob fait** :
- Analyse les erreurs
- Identifie les causes
- Propose des corrections
- Ajoute des logs si nécessaire

---

### 7. ⚡ Optimisation
**Quand l'utiliser** : Pour améliorer les performances

**Exemples de commandes** :
```
"Optimise les performances de @slow_function.py"
"Réduis la complexité algorithmique de cette boucle"
"Ajoute du caching pour améliorer les performances"
```

**Ce que Bob fait** :
- Identifie les goulots d'étranglement
- Optimise les algorithmes
- Ajoute du caching
- Améliore l'utilisation mémoire

---

### 8. 🏗️ Architecture
**Quand l'utiliser** : Pour concevoir ou améliorer l'architecture

**Exemples de commandes** :
```
"Propose une architecture pour une application e-commerce"
"Comment structurer ce microservice ?"
"Applique le pattern Repository à ce projet"
```

**Ce que Bob fait** :
- Propose des architectures
- Applique des patterns
- Structure les projets
- Sépare les responsabilités

---

## 📏 Les 7 Rules de Bob

### Rule 1 : Un Outil par Message ⚙️

**Pourquoi** : Clarté, contrôle, traçabilité

**Ce que ça signifie** :
- Bob utilise exactement un outil par message
- Chaque action est isolée et claire
- Vous pouvez suivre facilement le processus

**Exemple** :
```
❌ Mauvais : Bob ne peut pas créer 3 fichiers en un message
✅ Bon : Bob crée un fichier, attend validation, puis le suivant
```

---

### Rule 2 : Validation Systématique ✅

**Pourquoi** : Sécurité, contrôle, confiance

**Ce que ça signifie** :
- Vous devez confirmer chaque action de Bob
- Bob attend votre validation avant de continuer
- Vous gardez le contrôle total

**Exemple** :
```
Bob : "Je vais créer le fichier app.py"
Vous : [Confirmez]
Bob : [Crée le fichier]
Bob : "Fichier créé. Que voulez-vous faire ensuite ?"
```

---

### Rule 3 : Lecture Groupée (Max 5 Fichiers) 📚

**Pourquoi** : Contexte complet, efficacité

**Ce que ça signifie** :
- Bob peut lire jusqu'à 5 fichiers simultanément
- Utilisez cette capacité pour donner du contexte
- Plus efficace que lire un par un

**Exemple** :
```
✅ Bon : "Lis @app.py, @models.py, @config.py, @utils.py et @routes.py"
❌ Moins efficace : Lire chaque fichier séparément
```

---

### Rule 4 : Modifications Ciblées 🎯

**Pourquoi** : Précision, sécurité, traçabilité

**Ce que ça signifie** :
- Bob préfère `apply_diff` à `write_to_file`
- Modifications précises = moins de risques
- Vous voyez exactement ce qui change

**Exemple** :
```
✅ Bon : apply_diff pour ajouter une méthode
❌ Risqué : write_to_file pour tout réécrire
```

---

### Rule 5 : Clarté Avant Action 💬

**Pourquoi** : Éviter les erreurs, comprendre les besoins

**Ce que ça signifie** :
- Bob pose des questions si besoin
- Il clarifie avant d'agir
- Pas d'action basée sur des suppositions

**Exemple** :
```
Vous : "Améliore l'API"
Bob : "Quels aspects voulez-vous améliorer ? Performance, sécurité, documentation ?"
```

---

### Rule 6 : Pas de Suppositions 🚫

**Pourquoi** : Précision, éviter les erreurs

**Ce que ça signifie** :
- Bob ne suppose pas ce que vous voulez
- Il demande des précisions si nécessaire
- Il attend la confirmation des résultats

**Exemple** :
```
❌ Bob ne suppose pas : "Je pense que tu veux Flask"
✅ Bob demande : "Quel framework préfères-tu : Flask ou FastAPI ?"
```

---

### Rule 7 : Contexte Complet 📖

**Pourquoi** : Modifications cohérentes et correctes

**Ce que ça signifie** :
- Bob lit les fichiers nécessaires avant de modifier
- Il comprend le contexte global
- Modifications cohérentes avec l'existant

**Exemple** :
```
✅ Bon workflow :
1. "Lis @app.py et @models.py"
2. [Bob lit et comprend]
3. "Ajoute une route pour créer un utilisateur"
4. [Bob modifie en cohérence avec l'existant]
```

---

## 🎯 Combiner Skills et Rules : Workflows Optimaux

### Workflow 1 : Analyse et Refactoring

```
1. "Lis @legacy.py, @utils.py et @config.py" (Rule 3: Lecture groupée)
2. [Bob lit les 3 fichiers]
3. "Analyse ces fichiers et identifie les problèmes" (Skill: Analyse)
4. [Bob analyse et liste les problèmes]
5. "Refactorise @legacy.py en appliquant le Strategy Pattern" (Skill: Refactoring)
6. [Bob utilise apply_diff pour modifier] (Rule 4: Modifications ciblées)
7. [Vous validez] (Rule 2: Validation)
8. "Crée des tests pour vérifier le refactoring" (Skill: Tests)
```

### Workflow 2 : Création d'Application

```
1. "Crée une API REST pour gérer des tâches" (Skill: Génération)
2. [Bob crée app.py] (Rule 1: Un outil par message)
3. [Vous validez] (Rule 2: Validation)
4. [Bob crée models.py]
5. [Vous validez]
6. "Ajoute des tests unitaires" (Skill: Tests)
7. "Documente l'API dans README.md" (Skill: Documentation)
```

### Workflow 3 : Optimisation

```
1. "Lis tous les fichiers du module performance/" (Rule 3: Lecture groupée)
2. "Analyse les performances et identifie les goulots" (Skill: Analyse + Optimisation)
3. "Optimise la fonction la plus lente" (Skill: Optimisation)
4. [Bob utilise apply_diff] (Rule 4: Modifications ciblées)
5. "Ajoute des tests de performance" (Skill: Tests)
```

---

## 💡 Astuces Pro

### Pour Maximiser les Skills

1. **Soyez spécifique** : "Analyse les performances" > "Analyse le code"
2. **Combinez les skills** : "Analyse, puis refactorise, puis teste"
3. **Demandez des explications** : "Pourquoi ce pattern ?"
4. **Itérez** : Affinez progressivement

### Pour Respecter les Rules

1. **Anticipez** : Listez les fichiers à lire ensemble
2. **Validez rapidement** : Ne bloquez pas le workflow
3. **Préférez apply_diff** : Plus sûr et traçable
4. **Donnez du contexte** : Expliquez l'objectif global

### Commandes Magiques

```bash
# Lecture optimale (Rule 3)
"Lis @app.py, @models.py, @routes.py, @config.py et @utils.py ensemble"

# Analyse complète (Skill: Analyse)
"Analyse @fichier.py en détail : code smells, performance, sécurité, lisibilité"

# Refactoring sûr (Skill: Refactoring + Rule 4)
"Refactorise @code.py en utilisant apply_diff pour chaque modification"

# Génération de qualité (Skill: Génération)
"Crée une classe User avec type hints, validation, docstrings et tests"

# Workflow complet
"Lis le projet, analyse-le, propose un plan, puis applique les améliorations une par une"
```

---

## 🎓 Checklist de Maîtrise

### Skills
- [ ] Je sais quand utiliser chaque skill
- [ ] Je peux combiner plusieurs skills
- [ ] Je demande des explications quand nécessaire
- [ ] J'itère pour affiner les résultats

### Rules
- [ ] Je comprends pourquoi chaque rule existe
- [ ] Je respecte le workflow de validation
- [ ] J'utilise la lecture groupée efficacement
- [ ] Je préfère les modifications ciblées

### Workflow
- [ ] Je planifie mes interactions avec Bob
- [ ] Je donne le contexte nécessaire
- [ ] Je valide systématiquement
- [ ] J'optimise mes demandes

---

## 🚀 Aller Plus Loin

### Ressources
- Lab 1 : Découverte des outils de base
- Lab 2 : Refactoring et design patterns
- Lab 6 : Custom MCP Modes
- Lab 7 : DevOps Automation

### Pratique
- Appliquez ces concepts à vos projets réels
- Expérimentez avec différents workflows
- Partagez vos découvertes

---

_Référence créée pour le Bobathon 2026_