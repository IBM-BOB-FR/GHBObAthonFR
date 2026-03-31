# 🎯 Lab 1 : Découverte et Premiers Pas avec Bob

> **Durée estimée** : 45-60 minutes  
> **Difficulté** : ⭐ Débutant  
> **Objectif** : Se familiariser avec Bob et ses outils de base

---

## 📋 Objectifs d'Apprentissage

À la fin de ce lab, vous serez capable de :

- ✅ Communiquer efficacement avec Bob
- ✅ Créer et modifier des fichiers simples
- ✅ Exécuter des commandes basiques
- ✅ Comprendre le workflow de validation

---

## 🚀 Mise en Place

### Prérequis

- IBM Bob installé et configuré
- Terminal accessible
- Utilitaire `curl` installé et fonctionnel

### Activation de l'environnement virtuel

```bash
# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat
```

### Structure du Lab

```
lab1-decouverte/
├── README.md (ce fichier)
├── exercices/
│   ├── ex1-hello/
│   ├── ex2-files/
│   ├── ex3-code/
│   └── ex4-commands/
└── solutions/ (à créer par Bob)
```

---

## 📝 Exercice 1 : Premier Contact (10 min)

### Objectif

Comprendre comment Bob communique et utilise ses outils.

### Instructions

1. **Ouvrez Bob** dans IBM Bob
2. **Demandez à Bob** :

   ```
   Bonjour Bob ! Peux-tu créer un fichier exercices/ex1-hello/hello.py
   qui affiche "Hello Bobathon 2026!" ?
   ```

3. **Observez** :
   - Comment structure-t-il sa réponse ?
   - Attend-il votre validation ?

4. **Validez** l'action de Bob

5. **Demandez à Bob d'exécuter** le fichier :
   ```
   Peux-tu exécuter ce fichier Python ?
   ```

### ✅ Critères de Validation

- [ ] Le fichier `hello.py` est créé
- [ ] Le fichier s'exécute correctement
- [ ] Vous avez compris le cycle : proposition → validation → exécution

### 💡 Points Clés

- Bob utilise **un outil par message**
- Vous devez **valider** chaque action
- Bob **explique** ce qu'il fait

---

## 📖 Exercice 2 : Exploration de Fichiers (15 min)

### Objectif

Apprendre à utiliser les outils de lecture et d'exploration.

### Instructions

1. **Créez une structure de test** :

   ```
   Peux-tu créer la structure suivante dans exercices/ex2-files/ :
   - config.json (avec des paramètres d'application)
   - utils.py (avec 2-3 fonctions utilitaires)
   - main.py (qui importe utils)
   ```

2. **Explorez avec Bob** :

   ```
   Peux-tu lister tous les fichiers dans @exercices/ex2-files/ ?
   ```

3. **Lisez plusieurs fichiers** :

   ```
   Peux-tu lire @config.json et @utils.py ensemble ?
   ```

4. **Analysez le code** :
   ```
   Peux-tu m'expliquer comment ces fichiers interagissent ?
   ```

### ✅ Critères de Validation

- [ ] La structure est créée correctement
- [ ] Bob peut lister les fichiers
- [ ] Bob peut lire plusieurs fichiers simultanément
- [ ] L'analyse des interactions est claire

### 💡 Astuce

Bob peut lire **jusqu'à 5 fichiers** en une seule fois. Utilisez cette capacité pour comprendre des projets complexes !

---

## ✏️ Exercice 3 : Modification de Code (15 min)

### Objectif

Apprendre à modifier du code existant.

### Instructions

1. **Créez un fichier de base** :

   ```
   Crée exercices/ex3-code/calculator.py avec ces fonctions :
   - add(a, b) : addition simple
   - subtract(a, b) : soustraction simple
   - multiply(a, b) : multiplication simple
   ```

2. **Améliorez le code** :

   ```
   Améliore @calculator.py en ajoutant :
   - Type hints pour toutes les fonctions
   - Docstrings au format Google
   - Une fonction divide(a, b) avec gestion de la division par zéro
   ```

3. **Ajoutez des tests** :

   ```
   Crée un fichier test_calculator.py avec des tests unitaires
   pour toutes les fonctions
   ```

4. **Exécutez les tests** :
   ```
   Peux-tu exécuter les tests avec pytest ?
   ```

### ✅ Critères de Validation

- [ ] Le code original est créé
- [ ] Les améliorations sont appliquées correctement
- [ ] Les tests sont créés et passent

### 💡 Points Clés

- Bob est capable d'appliquer des modifications **ciblées** (plus sûr).
- Il peut également créer ou **réécrire complètement** des fichiers
- Toujours **vérifier** les changements avant de valider

---

## 🔧 Exercice 4 : Commandes et Automatisation (10 min)

### Objectif

Utiliser Bob pour exécuter des commandes et automatiser des tâches.

### Instructions

1. **Créez une API REST** :

   ```
   Crée une API REST simple dans exercices/ex4-commands/ avec :
   - Un serveur web (Flask/Python OU Express/Node.js, au choix)
   - Un endpoint GET /hello qui retourne "Hello Bobathon!"
   - Un endpoint GET /health pour vérifier le statut du service
   - Le serveur doit écouter sur le port 3000
   ```

2. **Installez les dépendances** :

   ```
   Installe les dépendances nécessaires
   ```

   → Bob identifie et exécute les commandes
   - Pour Flask : `pip install flask`
   - Pour Express : `npm install express`

3. **Testez le serveur** :

   ```
   Peux-tu démarrer le serveur et tester l'endpoint avec curl ?
   ```

4. **Créez la documentation** :
   ```
   Crée un README.md qui explique comment démarrer et tester l'API
   ```

### ✅ Critères de Validation

- [ ] L'API REST est créée (Flask ou Express)
- [ ] Les dépendances sont installées
- [ ] Le serveur démarre correctement sur le port 3000
- [ ] Les endpoints /hello et /health répondent comme attendu
- [ ] La documentation est claire

### 💡 Astuces

- Bob peut exécuter des commandes complexes :
  ```bash
  cd backend && npm install && npm test
  ```
- Utilisez le framework que vous connaissez le mieux
- Flask est déjà installé dans le .venv du projet

---

## 🎯 Exercice Bonus : Mini-Projet (Optionnel, 15 min)

### Objectif

Mettre en pratique tout ce que vous avez appris.

### Mission

Créer une application de gestion de contacts en Python.

### Instructions

Demandez à Bob :

```
Je veux créer une application de gestion de contacts dans exercices/bonus/.

Fonctionnalités :
- Ajouter un contact (nom, email, téléphone)
- Lister tous les contacts
- Rechercher un contact par nom
- Supprimer un contact
- Sauvegarder dans un fichier JSON

Peux-tu créer cette application avec :
- Le code principal
- Des tests unitaires
- Un README expliquant l'utilisation
```

### ✅ Critères de Validation

- [ ] L'application fonctionne
- [ ] Les tests passent
- [ ] Le README est clair
- [ ] Vous avez utilisé le workflow complet avec Bob

---

## 📊 Auto-Évaluation

Avant de passer au Lab 2, vérifiez que vous pouvez répondre OUI à ces questions :

- [ ] Je sais demander à Bob de créer des fichiers
- [ ] Je comprends comment Bob lit et explore les fichiers
- [ ] Je peux demander à Bob de modifier du code existant
- [ ] Je sais faire exécuter des commandes par Bob
- [ ] Je comprends le cycle de validation
- [ ] Je me sens à l'aise pour continuer

Si vous avez répondu NON à une question, **revenez sur l'exercice correspondant** !

---

## 🎓 Ce que Vous Avez Appris

### Outils Maîtrisés

- ✅ Créer des fichiers
- ✅ Lire des fichiers (jusqu'à 5 simultanément)
- ✅ Explorer la structure des fichiers
- ✅ Modifier du code de manière ciblée
- ✅ Exécuter des commandes
- ✅ Clarifier les besoins

### Concepts Clés

- **Un outil par message** : Bob travaille méthodiquement
- **Validation systématique** : Vous gardez le contrôle
- **Itération progressive** : Construire étape par étape
- **Clarté = Efficacité** : Plus vous êtes précis, meilleur est le résultat

---

## 🚀 Prochaines Étapes

Vous êtes maintenant prêt pour le **Lab 2 : Refactoring et Amélioration** !

Dans le Lab 2, vous apprendrez à :

- Analyser du code legacy
- Identifier les code smells
- Appliquer des design patterns
- Améliorer la qualité du code

**Bon courage !** 🎉

---

## 💡 Conseils pour la Suite

1. **Soyez spécifique** : Plus votre demande est claire, meilleur sera le résultat
2. **Itérez** : N'hésitez pas à demander des ajustements
3. **Expérimentez** : Essayez différentes approches
4. **Posez des questions** : Bob est là pour vous aider

---

_Lab créé pour le Bobathon 2026_
