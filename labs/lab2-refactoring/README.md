# 🔧 Lab 2 : Refactoring et Amélioration de Code

> **Durée estimée** : 60-75 minutes  
> **Difficulté** : ⭐⭐ Intermédiaire  
> **Objectif** : Maîtriser le refactoring avec Bob et améliorer la qualité du code

---

## 📋 Objectifs d'apprentissage

À la fin de ce lab, vous serez capable de :

- ✅ Identifier les code smells dans du code existant
- ✅ Appliquer des techniques de refactoring
- ✅ Utiliser des design patterns appropriés
- ✅ Améliorer la lisibilité et la maintenabilité
- ✅ Ajouter des tests pour sécuriser le refactoring

---

## 🚀 Mise en place

### Prérequis

- Avoir complété le Lab 1
- Connaissances de base en programmation
- Python 3.8+ installé
- Environnement virtuel Python activé (`.venv` à la racine du projet)

### Activation de l'environnement virtuel

```bash
# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat
```

---

## 📝 Exercice 1 : Analyse de Code Legacy (15 min)

### Objectif

Apprendre à identifier les problèmes dans du code existant.

### Préparation

Demandez à Bob de créer le fichier suivant :

```
Crée le fichier code-legacy/user_manager.py avec ce contenu :

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email, age, city, country):
        user = {
            'name': name,
            'email': email,
            'age': age,
            'city': city,
            'country': country,
            'created_at': None
        }
        self.users.append(user)
        return user

    def get_user(self, email):
        for user in self.users:
            if user['email'] == email:
                return user
        return None

    def update_user(self, email, name=None, age=None, city=None, country=None):
        user = self.get_user(email)
        if user:
            if name:
                user['name'] = name
            if age:
                user['age'] = age
            if city:
                user['city'] = city
            if country:
                user['country'] = country
            return user
        return None

    def delete_user(self, email):
        user = self.get_user(email)
        if user:
            self.users.remove(user)
            return True
        return False

    def get_all_users(self):
        return self.users

    def get_users_by_country(self, country):
        result = []
        for user in self.users:
            if user['country'] == country:
                result.append(user)
        return result

    def get_adult_users(self):
        result = []
        for user in self.users:
            if user['age'] >= 18:
                result.append(user)
        return result
```

### Instructions

1. **Demandez à Bob d'analyser** :

   ```
   Analyse le fichier @code-legacy/user_manager.py et identifie tous les
   code smells et problèmes de design. Liste-les avec des explications.
   ```

2. **Attendez l'analyse de Bob** qui devrait identifier :
   - Utilisation de dictionnaires au lieu de classes
   - Paramètres multiples (Long Parameter List)
   - Code dupliqué (boucles répétées)
   - Manque de validation
   - Pas de type hints
   - Pas de gestion d'erreurs
   - Violation du principe DRY

### ✅ Critères de Validation

- [ ] Bob a identifié au moins 5 problèmes
- [ ] Les explications sont claires
- [ ] Vous comprenez chaque problème identifié

---

## 🔨 Exercice 2 : Refactoring Basique (20 min)

### Objectif

Appliquer des améliorations fondamentales au code.

### Instructions

1. **Créez une classe User** :

   ```
   Refactorise user_manager.py en créant une classe User avec :
   - Attributs typés (type hints)
   - Validation dans __init__
   - Méthode __repr__ pour le debug
   - Utilise dataclass si approprié
   ```

2. **Améliorez UserManager** :

   ```
   Améliore @user_manager.py pour :
   - Utiliser la nouvelle classe User
   - Ajouter des type hints partout
   - Ajouter des docstrings
   - Gérer les erreurs avec des exceptions personnalisées
   ```

3. **Ajoutez des tests** :
   ```
   Crée test_user_manager.py avec des tests pour :
   - Création d'utilisateurs
   - Validation des données
   - Recherche d'utilisateurs
   - Mise à jour et suppression
   ```

### ✅ Critères de Validation

- [ ] La classe User est créée avec validation
- [ ] UserManager utilise la classe User
- [ ] Type hints présents partout
- [ ] Tests créés et passent
- [ ] Le code est plus lisible

### 💡 Points Clés

- **Dataclass** : Simplifie la création de classes de données
- **Type hints** : Améliore la lisibilité et détecte les erreurs
- **Validation** : Prévient les données invalides dès la création

---

## 🎨 Exercice 3 : Design Patterns (25 min)

### Objectif

Appliquer des design patterns pour améliorer l'architecture.

### Préparation

Demandez à Bob de créer ce fichier :

```
Crée code-legacy/data_processor.py avec ce contenu :

class DataProcessor:
    def process_data(self, data, format_type):
        if format_type == 'json':
            import json
            return json.dumps(data)
        elif format_type == 'xml':
            result = '<data>'
            for key, value in data.items():
                result += f'<{key}>{value}</{key}>'
            result += '</data>'
            return result
        elif format_type == 'csv':
            result = ','.join(data.keys()) + '\n'
            result += ','.join(str(v) for v in data.values())
            return result
        else:
            return str(data)

    def validate_data(self, data, validation_type):
        if validation_type == 'email':
            return '@' in data and '.' in data
        elif validation_type == 'phone':
            return len(data) >= 10 and data.isdigit()
        elif validation_type == 'age':
            return data.isdigit() and 0 <= int(data) <= 150
        else:
            return True
```

### Instructions

1. **Identifiez le pattern approprié** :

   ```
   Analyse @data_processor.py et suggère quel design pattern
   serait approprié pour remplacer les if/elif.
   ```

   → Bob devrait suggérer le **Strategy Pattern**

2. **Implémentez le Strategy Pattern** :

   ```
   Refactorise @data_processor.py en utilisant le Strategy Pattern :
   - Crée une interface/classe abstraite pour les formatters
   - Implémente JsonFormatter, XmlFormatter, CsvFormatter
   - Modifie DataProcessor pour utiliser ces strategies
   ```

3. **Appliquez le même pattern pour la validation** :

   ```
   Applique aussi le Strategy Pattern pour les validateurs :
   - EmailValidator
   - PhoneValidator
   - AgeValidator
   ```

4. **Ajoutez des tests** :
   ```
   Crée des tests pour vérifier que tous les formatters
   et validateurs fonctionnent correctement.
   ```

### ✅ Critères de Validation

- [ ] Strategy Pattern correctement implémenté
- [ ] Code plus extensible (facile d'ajouter de nouveaux formats)
- [ ] Principe Open/Closed respecté
- [ ] Tests passent
- [ ] Vous comprenez les avantages du pattern

### 💡 Avantages du Strategy Pattern

- **Extensibilité** : Ajouter de nouveaux formats sans modifier le code existant
- **Testabilité** : Chaque strategy peut être testée indépendamment
- **Lisibilité** : Plus de longues chaînes if/elif

---

## 🏗️ Exercice 4 : Refactoring Avancé (15 min)

### Objectif

Appliquer plusieurs techniques de refactoring simultanément.

### Préparation

```
Crée code-legacy/report_generator.py avec ce contenu :

class ReportGenerator:
    def generate_report(self, users, report_type):
        if report_type == 'summary':
            total = len(users)
            adults = 0
            for user in users:
                if user['age'] >= 18:
                    adults += 1
            avg_age = sum(u['age'] for u in users) / len(users) if users else 0

            report = f"Total Users: {total}\n"
            report += f"Adults: {adults}\n"
            report += f"Average Age: {avg_age:.2f}\n"
            return report

        elif report_type == 'detailed':
            report = "DETAILED USER REPORT\n"
            report += "=" * 50 + "\n"
            for user in users:
                report += f"Name: {user['name']}\n"
                report += f"Email: {user['email']}\n"
                report += f"Age: {user['age']}\n"
                report += f"Location: {user['city']}, {user['country']}\n"
                report += "-" * 50 + "\n"
            return report

        elif report_type == 'by_country':
            countries = {}
            for user in users:
                country = user['country']
                if country not in countries:
                    countries[country] = []
                countries[country].append(user)

            report = "USERS BY COUNTRY\n"
            report += "=" * 50 + "\n"
            for country, country_users in countries.items():
                report += f"\n{country}: {len(country_users)} users\n"
                for user in country_users:
                    report += f"  - {user['name']} ({user['email']})\n"
            return report
```

### Instructions

1. **Analyse complète** :

   ```
   Analyse @report_generator.py et propose un plan de refactoring complet
   incluant :
   - Extraction de méthodes
   - Utilisation de design patterns
   - Amélioration de la structure
   - Ajout de type hints et docstrings
   ```

2. **Implémentez le refactoring** :

   ```
   Applique le plan de refactoring en créant :
   - Des méthodes privées pour chaque type de calcul
   - Des classes de rapport (SummaryReport, DetailedReport, etc.)
   - Une interface commune pour les rapports
   - Des tests unitaires
   ```

3. **Comparez** :
   ```
   Crée un fichier COMPARISON.md qui compare l'ancien et le nouveau code
   en termes de :
   - Lisibilité
   - Maintenabilité
   - Testabilité
   - Extensibilité
   ```

### ✅ Critères de Validation

- [ ] Code refactoré avec méthodes extraites
- [ ] Design pattern approprié appliqué
- [ ] Tests complets
- [ ] Documentation de comparaison claire
- [ ] Amélioration mesurable de la qualité

---

## 🎯 Exercice Bonus : Refactoring Complet (Optionnel)

### Mission

Combinez tous les fichiers refactorés en une application cohérente.

### Instructions

```
Crée une application complète dans refactored/ qui :
1. Utilise toutes les classes refactorées
2. Ajoute une interface CLI simple
3. Inclut des tests d'intégration
4. Génère un rapport de couverture de tests
5. Documente l'architecture dans ARCHITECTURE.md
```

### ✅ Critères de Validation

- [ ] Application fonctionnelle
- [ ] Tests d'intégration passent
- [ ] Couverture de tests > 80%
- [ ] Documentation architecture claire

---

## 📊 Auto-Évaluation

Avant de passer au Lab 3, vérifiez :

- [ ] Je sais identifier les code smells
- [ ] Je connais au moins 3 design patterns
- [ ] Je peux refactorer du code de manière sécurisée avec des tests
- [ ] Je me sens à l'aise pour continuer

---

## 🎓 Ce que Vous Avez Appris

### Techniques de Refactoring

- ✅ **Extract Method** : Extraire des méthodes pour réduire la complexité
- ✅ **Replace Conditional with Polymorphism** : Strategy Pattern
- ✅ **Introduce Parameter Object** : Regrouper les paramètres
- ✅ **Replace Magic Numbers** : Utiliser des constantes

### Design Patterns

- ✅ **Strategy Pattern** : Pour les algorithmes interchangeables
- ✅ **Template Method** : Pour les rapports
- ✅ **Factory Pattern** : Pour créer des objets

### Principes

- ✅ **DRY** : Don't Repeat Yourself
- ✅ **SOLID** : Single Responsibility, Open/Closed, etc.
- ✅ **KISS** : Keep It Simple, Stupid
- ✅ **YAGNI** : You Aren't Gonna Need It

---

## 🚀 Prochaines Étapes

Vous êtes maintenant prêt pour le **Lab 3 : Création d'API et Tests** !

Dans le Lab 3, vous apprendrez à :

- Créer des APIs REST avec Flask/FastAPI
- Implémenter des tests d'API
- Gérer l'authentification
- Documenter les APIs

**Excellent travail !** 🎉

---

## 💡 Ressources Complémentaires

- **Livre** : "Refactoring" de Martin Fowler
- **Livre** : "Clean Code" de Robert C. Martin
- **Site** : refactoring.guru (patterns et refactoring)

---

_Lab créé pour le Bobathon 2026_
