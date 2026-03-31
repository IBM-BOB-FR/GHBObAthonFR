# 🎯 Lab 0 : Prise en Main de Bob

> **Durée estimée** : 50-70 minutes  
> **Niveau** : Débutant ⭐  
> **Prérequis** : Aucun - C'est votre premier contact avec Bob !

---

## 📋 Objectifs du Lab

À la fin de ce lab, vous serez capable de :

- ✅ Communiquer efficacement avec Bob
- ✅ Utiliser les outils de base de Bob
- ✅ Comprendre le workflow étape par étape
- ✅ Résoudre des problèmes simples avec Bob
- ✅ Être autonome pour les labs suivants

---

## 🚀 Avant de Commencer

### Vérification de l'Installation

1. **Ouvrez IBM Bob**
2. **Vérifiez que Bob est accessible** (icône dans la barre latérale)
3. **Testez la connexion** : Envoyez "Hello Bob" et attendez une réponse

Si vous rencontrez des problèmes, levez la main ! 🙋

### Structure du Lab

Ce lab contient **6 exercices progressifs** + **1 exercice bonus** :

```
Lab 0 : Prise en Main
├── Exercice 1 : Premier Contact (5 min)
├── Exercice 2 : Lecture de Fichiers (10 min)
├── Exercice 3 : Modifications de Code (10 min)
├── Exercice 4 : Exécution de Commandes (10 min)
├── Exercice 5 : Projet Complet (15 min)
└── Bonus : Debugging (Optionnel)
```

> 💡 **Note sur les outils de Bob** : Dans ce lab, nous mentionnons parfois les outils que Bob utilise en arrière-plan (comme `read_file`, `apply_diff`, `execute_command`, etc.). Ces informations sont données à titre informatif pour vous aider à comprendre comment Bob fonctionne. Vous n'avez pas besoin de les mémoriser ou de les utiliser directement - Bob choisira automatiquement le bon outil selon votre demande. Concentrez-vous sur **ce que vous voulez accomplir**, pas sur **comment** Bob le fait !

---

## 📚 Exercice 1 : Premier Contact

**Durée** : 5 minutes

**Objectif** : Comprendre comment Bob communique et travaille

**Mode recommandé** : ❓ Ask

### Instructions

1. **Ouvrez Bob** dans IBM Bob
2. **Envoyez ce message** :

   ```
   Bonjour Bob ! Peux-tu te présenter et m'expliquer comment tu fonctionnes ?
   ```

3. **Observez** :
   - Comment Bob structure sa réponse
   - Quel outil il utilise (probablement `ask_followup_question` ou `attempt_completion`). **Note:** pour savoir quel outil Bob a utilisé à un moment donné, il suffit de le lui demander ;-)
   - Le format de sa réponse

### Questions de Réflexion

- Bob a-t-il utilisé un outil ?
- Sa réponse était-elle claire ?
- Avez-vous compris sa philosophie de travail ?

### ✅ Critères de Validation

Vous avez compris que Bob utilise **un outil par message** et attend votre **validation** après chaque action.

---

## 📖 Exercice 2 : Lecture de Fichiers

**Durée** : 10 minutes

**Objectif** : Apprendre à demander à Bob de lire et analyser des fichiers

**Mode recommandé** : 💻 Code

**Nouvelle tâche** : Oui (commencez une nouvelle tâche pour cet exercice)

### Préparation

Créez un fichier de test :

```bash
# macOS/Linux
mkdir -p exercices/ex2

# Windows (PowerShell)
New-Item -ItemType Directory -Force -Path exercices/ex2

# Windows (CMD)
mkdir exercices\ex2
```

Créez `exercices/ex2/example.py` avec ce contenu :

```python
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

def calculate_average(numbers):
    sum = calculate_sum(numbers)
    return sum / len(numbers)

# Test
data = [1, 2, 3, 4, 5]
print(f"Sum: {calculate_sum(data)}")
print(f"Average: {calculate_average(data)}")
```

### Instructions

### 💡 Commandes Slash

Bob supporte des **commandes slash** pour automatiser des tâches et accéder rapidement à des fonctionnalités. Tapez **/** dans le chat pour voir toutes les commandes disponibles.

**Commandes intégrées principales :**

- **`/init`** - Initialise un nouveau projet ou workspace avec Bob
  - Configure la structure nécessaire pour travailler avec Bob
  - Crée les fichiers de configuration de base

- **`/review`** - Analyse et révise votre code
  - `/review` - Révise les changements non commités dans votre répertoire de travail
  - `/review <branche>` - Compare une branche avec votre branche actuelle
  - `/review #<numéro-issue>` - Valide les changements locaux par rapport à une issue GitHub
  - Effectue une analyse complète : détection de bugs, vérifications de sécurité, problèmes de performance

- **`/create-pr`** - Crée une pull request avec une description générée par IA
  - Analyse vos changements
  - Génère une description complète de PR basée sur le diff

**💡 Astuce :** Les commandes slash vous permettent de standardiser vos workflows et de gagner du temps sur les tâches récurrentes. Vous pouvez même créer vos propres commandes personnalisées en ajoutant des fichiers markdown dans `.bob/commands/` !

Entre autres, Bob permet de mentionner des fichiers en contexte en utilisant le symbole **@**. Il suffit de taper **@** dans la fenêtre de chat de Bob pour voir une liste des mentions possibles.

1. **Demandez à Bob** :

   ```
   Peux-tu lire le fichier @exercices/ex2/example.py et me dire ce qu'il fait ?
   ```

2. **Observez** :
   - Bob utilise l'outil `read_file`
   - Il analyse le contenu
   - Il vous explique le code

3. **Demandez une analyse plus poussée** :
   ```
   Quelles améliorations pourrais-tu suggérer pour ce code ?
   ```

### ✅ Critères de Validation

- Bob a lu le fichier correctement
- Il a identifié les fonctions
- Il a proposé des améliorations pertinentes

### 💡 Astuce

Bob peut lire **jusqu'à 5 fichiers simultanément**. Essayez de créer plusieurs fichiers et demandez-lui de les lire ensemble !

---

## ✏️ Exercice 3 : Modifications de Code

**Durée** : 10 minutes

**Objectif** : Découvrir comment demander à Bob de modifier du code existant

**Mode recommandé** : 💻 Code

**Nouvelle tâche** : Optionnel (vous pouvez continuer dans la même tâche que l'Exercice 2)

### Instructions

1. **Demandez à Bob d'améliorer le code** :

   ```
   Peux-tu améliorer le fichier @exercices/ex2/example.py en :
   1. Ajoutant des type hints
   2. Ajoutant des docstrings
   3. Utilisant des fonctions Python plus idiomatiques
   ```

2. **Observez** :
   - Bob est capable d'appliquer des modifications ciblées
   - Il montre exactement ce qu'il va changer
   - Il attend votre confirmation

3. **Validez ou demandez des ajustements** :
   - Si vous êtes d'accord : "Oui, applique ces changements"
   - Si vous voulez modifier : "Peux-tu aussi ajouter X ?"
   - Une fois appliqué, Bob vous montrera un résumé des modifications

### ✅ Critères de Validation

- Le code a été amélioré
- Les type hints sont présents
- Les docstrings sont claires
- Le code est plus pythonique

### 💡 Points Clés

- Bob peut appliquer des modifications ciblées à un fichier
- Il peut également réécrire complètement un fichier
- Toujours **valider** avant que Bob n'applique

---

## 🔧 Exercice 4 : Exécution de Commandes

**Durée** : 10 minutes

**Objectif** : Découvrir comment demander à Bob d'exécuter des commandes

**Mode recommandé** : 💻 Code

**Nouvelle tâche** : Oui (commencez une nouvelle tâche pour cet exercice)

### Instructions

1. **Créez un environnement de test** :

   ```
   Peux-tu créer un environnement virtuel Python dans exercices/ex4
   et installer pytest ?
   ```

2. **Observez** :
   - Bob explique ce que fait chaque commande
   - Il attend la confirmation du résultat

3. **Créez un fichier de test** :

   ```
   Crée un fichier exercices/ex4/test_math.py avec des tests
   pour les fonctions calculate_sum et calculate_average
   ```

4. **Exécutez les tests** :
   ```
   Peux-tu exécuter les tests avec pytest ?
   ```

### ✅ Critères de Validation

- L'environnement virtuel est créé
- pytest est installé
- Les tests sont créés et passent

### 💡 Astuce

Bob peut exécuter des commandes complexes :

```bash
# macOS/Linux
cd backend && source .venv/bin/activate && python -m pytest -v

# Windows (PowerShell)
cd backend; .venv\Scripts\Activate.ps1; python -m pytest -v

# Windows (CMD)
cd backend && .venv\Scripts\activate.bat && python -m pytest -v
```

---

## 🎯 Exercice 5 : Projet Complet

**Durée** : 15 minutes

**Objectif** : Mettre en pratique tout ce que vous avez appris dans un mini-projet

**Mode recommandé** : 💻 Code

**Nouvelle tâche** : Oui (commencez une nouvelle tâche pour ce projet complet)

### Mission

Créer une petite application de gestion de tâches (TODO list) en Python.

### Instructions

1. **Décrivez le projet à Bob** :

   ```
   Je veux créer une application TODO list en Python dans exercices/ex5/.

   Fonctionnalités :
   - Ajouter une tâche
   - Lister les tâches
   - Marquer une tâche comme complétée
   - Supprimer une tâche
   - Sauvegarder dans un fichier JSON

   Peux-tu créer la structure du projet et implémenter ces fonctionnalités ?
   ```

2. **Laissez Bob travailler** :
   - Il va créer une TODO list pour organiser le travail
   - Il va procéder étape par étape

3. **Validez chaque étape**

4. **Demandez des tests** :

   ```
   Peux-tu ajouter des tests unitaires pour cette application ?
   ```

5. **Demandez de la documentation** :

   ```
   Peux-tu créer un README.md expliquant comment utiliser l'application ?
   ```

6. **Testez l'application** :
   ```
   Peux-tu exécuter l'application pour vérifier qu'elle fonctionne ?
   ```

### ✅ Critères de Validation

- L'application fonctionne
- Les tests passent
- La documentation est claire
- Vous avez compris le workflow complet

### 💡 Ce que vous avez appris

- Décomposer un projet en étapes
- Travailler itérativement avec Bob
- Valider à chaque étape
- Obtenir un résultat professionnel

---

## 🎓 Exercice Bonus : Debugging (Optionnel)

**Objectif** : Apprendre à utiliser Bob pour débugger du code

**Mode recommandé** : 💻 Code

**Nouvelle tâche** : Oui (commencez une nouvelle tâche pour cet exercice bonus)

### Instructions

1. **Créez le fichier buggy** :

   Créez un fichier `exercices/bonus/buggy.py` avec du code qui a des bugs :

```python
def divide_numbers(a, b):
    return a / b

def process_list(items):
    result = []
    for i in range(len(items)):
        result.append(items[i] * 2)
    return result

def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max == num
    return max

# Tests
print(divide_numbers(10, 0))  # Bug 1
print(process_list([1, 2, 3]))  # Pas optimal
print(find_max([1, 5, 3, 2]))  # Bug 2
```

2. **Exécutez le code pour observer les bugs** :

   ```
   Peux-tu exécuter le fichier @exercices/bonus/buggy.py et me montrer les erreurs ?
   ```

   Observez les erreurs qui s'affichent - cela vous aidera à comprendre les problèmes.

3. **Analysez les erreurs avec Bob** :

   ```
   Maintenant que nous avons vu les erreurs, peux-tu identifier tous les bugs
   et problèmes dans ce code ?
   ```

4. **Demandez les corrections** :
   ```
   Peux-tu corriger ces bugs et optimiser le code ?
   ```

### ✅ Critères de Validation

- Bug 1 : Division par zéro (ajouter gestion d'erreur)
- Bug 2 : `==` au lieu de `=` dans find_max
- Optimisation : Utiliser list comprehension dans process_list

---

## 📊 Auto-Évaluation

Avant de passer aux labs suivants, vérifiez que vous pouvez répondre OUI à ces questions :

- [ ] Je sais comment demander à Bob de lire des fichiers
- [ ] Je comprends comment Bob modifie le code (changements ciblés ou réécriture complète)
- [ ] Je sais demander à Bob d'exécuter des commandes
- [ ] Je peux utiliser Bob pour chercher dans des fichiers
- [ ] Je comprends le workflow étape par étape
- [ ] Je sais valider ou demander des ajustements
- [ ] Je peux décomposer un projet en tâches avec Bob
- [ ] Je me sens à l'aise pour commencer les labs suivants

Si vous avez répondu NON à une question, **revenez sur l'exercice correspondant** ou **demandez de l'aide** ! 🙋

---

## 💡 Bonnes Pratiques pour Travailler avec Bob

### DO ✅

1. **Soyez spécifique**
   - ❌ "Améliore ce code"
   - ✅ "Refactorise cette fonction pour utiliser le pattern Strategy"

2. **Donnez du contexte**
   - Expliquez ce que vous voulez accomplir
   - Mentionnez les contraintes
   - Précisez les technologies

3. **Validez chaque étape**
   - Lisez ce que Bob propose
   - Vérifiez que c'est correct
   - Demandez des ajustements si nécessaire

4. **Itérez**
   - Commencez simple
   - Ajoutez de la complexité progressivement
   - Affinez au fur et à mesure

### DON'T ❌

1. **Ne soyez pas vague**
   - Bob a besoin de clarté pour être efficace

2. **N'assumez pas**
   - Attendez toujours la confirmation
   - Vérifiez les résultats

3. **Ne sautez pas d'étapes**
   - Le workflow étape par étape est important
   - Chaque validation compte

4. **N'hésitez pas à poser des questions**
   - Bob est là pour vous aider
   - Il n'y a pas de question bête

---

## 🎨 Personnaliser Bob avec des Règles Personnalisées

Bob peut être personnalisé pour suivre vos préférences et standards d'équipe en utilisant des **règles personnalisées** (custom rules).

### Qu'est-ce qu'une règle personnalisée ?

Les règles personnalisées sont des instructions qui influencent comment Bob répond à vos demandes :

- 📝 Définissent des préférences de style de code
- 📋 Établissent des conventions de documentation
- 🔧 Spécifient des workflows et processus
- 🌍 Peuvent être globales (tous vos projets) ou spécifiques à un projet

### Créer des règles simples

Créez un fichier `.bobrules` à la racine de votre projet :

```bash
# macOS/Linux
cat > .bobrules << 'EOF'
# Règles de style
- Utilise 4 espaces pour l'indentation
- Utilise camelCase pour les noms de variables
- Utilise PascalCase pour les noms de classes

# Règles de documentation
- Ajoute des docstrings pour toutes les fonctions publiques
- Inclus des exemples d'utilisation dans les docstrings

# Règles de tests
- Écris des tests unitaires pour toutes les nouvelles fonctions
- Utilise pytest comme framework de test
EOF

# Windows (PowerShell)
@"
# Règles de style
- Utilise 4 espaces pour l'indentation
- Utilise camelCase pour les noms de variables
- Utilise PascalCase pour les noms de classes

# Règles de documentation
- Ajoute des docstrings pour toutes les fonctions publiques
- Inclus des exemples d'utilisation dans les docstrings

# Règles de tests
- Écris des tests unitaires pour toutes les nouvelles fonctions
- Utilise pytest comme framework de test
"@ | Out-File -FilePath .bobrules -Encoding UTF8
```

### Exemples de règles efficaces

**Bonnes règles** (spécifiques et actionnables) :

- ✅ "Utilise 4 espaces pour l'indentation dans les fichiers Python"
- ✅ "Ajoute des type hints pour tous les paramètres de fonction"
- ✅ "Explique ton raisonnement avant de fournir du code"
- ✅ "Lors de l'ajout de fonctionnalités web, assure-toi qu'elles sont responsives et accessibles"

**Règles à éviter** (trop vagues) :

- ❌ "Formate le code correctement"
- ❌ "Fais du bon code"

### Règles globales vs. règles de projet

**Règles de projet** (`.bobrules` dans votre projet) :

- S'appliquent uniquement au projet actuel
- Parfaites pour les standards spécifiques au projet
- Peuvent être versionnées avec Git

**Règles globales** (`~/.bob/rules/`) :

- S'appliquent à tous vos projets
- Idéales pour vos préférences personnelles
- Partagées entre tous vos workspaces

### Configuration avancée

Pour une organisation plus complexe, utilisez des répertoires :

```bash
# Structure de projet
.bob/
  rules/                    # Règles générales
    coding-style.md
    documentation.md
  rules-code/              # Règles spécifiques au mode Code
    python-standards.md
```

### 💡 Astuce

Les règles personnalisées sont particulièrement utiles pour :

- Standardiser le code dans une équipe
- Appliquer les conventions de votre entreprise
- Adapter Bob à vos préférences personnelles
- Assurer la cohérence entre les projets

Pour en savoir plus sur les règles personnalisées, consultez la [documentation officielle](https://bob.ibm.com/docs/ide/configuration/rules).

---

## 🚀 Prochaines Étapes

Félicitations ! Vous avez terminé le Lab 0. Vous êtes maintenant prêt(e) pour les labs suivants.

### Choisissez votre prochain lab selon votre profil :

- **Lab 1 - Découverte** (45-60 min) ⭐  
  Parfait si vous voulez approfondir les bases

- **Lab 2 - Refactoring** (60-75 min) ⭐⭐  
  Pour apprendre à améliorer du code existant

- **Lab 3 - API et Tests** (75-90 min) ⭐⭐⭐  
  Pour créer des APIs REST avec tests

- **Lab 4 - Data Science** (75-90 min) ⭐⭐⭐  
  Pour analyser des données avec pandas

- **Lab 5 - Architecture** (90-120 min) ⭐⭐⭐⭐  
  Pour concevoir des architectures robustes

---

## 🎉 Félicitations !

Vous maîtrisez maintenant les bases de Bob !

### Ce que vous avez appris

✅ Communiquer efficacement avec Bob  
✅ Utiliser les outils de base (lecture de fichiers, application de changements, exécution de commandes, etc.)  
✅ Comprendre le workflow étape par étape  
✅ Résoudre des problèmes de manière autonome  
✅ Créer des projets complets avec Bob

### Pour aller plus loin

- **Expérimentez** : Essayez différentes approches
- **Partagez** : Discutez de vos découvertes avec les autres
- **Documentez** : Notez vos astuces et bonnes pratiques
- **Amusez-vous** : C'est un hackathon, profitez-en !

---

## 📞 Besoin d'Aide ?

Si vous rencontrez des difficultés :

1. **Relisez** la section concernée de ce lab
2. **Demandez à Bob** de clarifier ou d'expliquer
3. **Consultez** vos collègues
4. **Appelez** un organisateur

---

## 🚀 Bon Bobathon !

Vous avez maintenant toutes les clés en main pour réussir. Les labs suivants vous attendent !

**Rappelez-vous** : Bob est là pour vous aider, pas pour vous remplacer. Utilisez-le comme un partenaire de développement expérimenté qui amplifie vos capacités.

**Bonne chance et amusez-vous bien !** 🎉

---

_Lab créé pour le Bobathon 2026_
