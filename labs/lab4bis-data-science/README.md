# 📊 Lab 4 : Data Science et Analyse de Données

> **Durée estimée** : 75-90 minutes (+ 15-20 min bonus optionnel)  
> **Difficulté** : ⭐⭐⭐ Avancé  
> **Objectif** : Maîtriser l'analyse de données et le machine learning avec Bob

---

## 📋 Objectifs d'Apprentissage

À la fin de ce lab, vous serez capable de :

✅ Charger et explorer des datasets avec pandas  
✅ Nettoyer et préparer les données  
✅ Créer des visualisations informatives  
✅ Effectuer des analyses statistiques  
✅ Construire des modèles de machine learning  
✅ Évaluer et optimiser les modèles  

---

## 🚀 Mise en Place

### Prérequis

- Avoir complété les Labs 0, 1 et 1 bis
- Python 3.8+ installé
- Connaissances de base en statistiques (utile mais pas obligatoire)
- Environnement virtuel Python (`.venv` à la racine du projet)

### Installation des Dépendances

Activer l'environnement virtuel (à la racine du projet)

```bash
# macOS/Linux
source .venv/bin/activate
```

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

```bash
# Windows (CMD)
.venv\Scripts\activate.bat
```

Installer les bibliothèques
```bash
pip install -r labs/lab4-data-science/requirements.txt
```

**Contenu de requirements.txt** :

```txt
# Data manipulation
pandas==2.2.3
numpy==2.2.1

# Visualization
matplotlib==3.10.0
seaborn==0.13.2

# Machine Learning
scikit-learn==1.6.1

# Notebooks
jupyter==1.1.1

# Utilities
tabulate==0.9.0  # Requis pour DataFrame.to_markdown()
```

### Préparation de la Structure

Crée la structure de répertoires nécessaire :

```bash
# macOS/Linux
mkdir -p lab4-data-science/data/{raw,processed,results}
mkdir -p lab4-data-science/{src,tests,notebooks}
```

```bash
# Windows (PowerShell)
New-Item -ItemType Directory -Force -Path lab4-data-science/data/raw
New-Item -ItemType Directory -Force -Path lab4-data-science/data/processed
New-Item -ItemType Directory -Force -Path lab4-data-science/data/results
New-Item -ItemType Directory -Force -Path lab4-data-science/src
New-Item -ItemType Directory -Force -Path lab4-data-science/tests
New-Item -ItemType Directory -Force -Path lab4-data-science/notebooks
```

```bash
# Windows (CMD)
mkdir lab4-data-science\data\raw lab4-data-science\data\processed lab4-data-science\data\results
mkdir lab4-data-science\src lab4-data-science\tests lab4-data-science\notebooks
```

---

## 📝 Exercice 1 : Exploration des Données (15 min)

### Objectif

Charger et explorer un dataset réaliste pour comprendre sa structure.

### Dataset Fourni

Un **dataset de ventes réaliste** est fourni dans `labs/lab4bis-data-science/data/sales_data.csv`.

**Caractéristiques** :

- 📊 **1000 transactions** de ventes sur l'année 2023
- 📋 **11 colonnes** : date, product, category, quantity, price, customer_age, customer_gender, region, discount, shipping_cost, revenue
- ⚠️ **Valeurs manquantes** : ~5% (à nettoyer dans l'Exercice 2)
- 🔍 **Outliers** : ~2% (à détecter)
- 🔗 **Corrélations réalistes** : quantity (+0.60), price (+0.19) avec revenue

**📚 Documentation complète** : Voir `labs/lab4bis-data-science/data/README.md`

### Instructions

1. **Copiez le dataset** :

   ```bash
   # macOS/Linux
   mkdir -p data/raw
   cp labs/lab4bis-data-science/data/sales_data.csv data/raw/
   ```

    ```bash
   # Windows (PowerShell)
   New-Item -ItemType Directory -Force -Path data/raw
   Copy-Item labs/lab4bis-data-science/data/sales_data.csv -Destination data/raw/
   ```
    
    ```bash
   # Windows (CMD)
   mkdir data\raw
   copy labs\lab4bis-data-science\data\sales_data.csv data\raw\
   ```

La suite est à saisir dans Bob

2. **Créez un script d'exploration** :

   ```
   Crée src/data_loader.py avec une classe DataLoader qui :
   - Charge le CSV avec pandas
   - Affiche les informations de base (shape, dtypes, head)
   - Calcule les statistiques descriptives
   - Identifie les valeurs manquantes
   - Détecte les valeurs aberrantes
   ```

3. **Analysez les données** :

   ```
   Utilise le DataLoader pour :
   - Afficher les 10 premières lignes
   - Montrer les statistiques pour chaque colonne numérique
   - Lister les valeurs uniques pour les colonnes catégorielles
   - Identifier les problèmes potentiels (valeurs manquantes, doublons)
   ```

4. **Créez un rapport d'exploration** :
   ```
   Génère un fichier data/results/exploration_report.md avec :
   - Résumé du dataset
   - Statistiques clés
   - Problèmes identifiés
   - Recommandations pour le nettoyage
   ```

### ✅ Critères de Validation

- [ ] Dataset créé avec 1000 lignes
- [ ] DataLoader fonctionnel
- [ ] Statistiques calculées correctement
- [ ] Rapport d'exploration généré
- [ ] Problèmes identifiés

### 💡 Exemple de Code

```python
import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def get_info(self):
        """Retourne les informations de base"""
        return {
            'shape': self.df.shape,
            'columns': self.df.columns.tolist(),
            'dtypes': self.df.dtypes.to_dict(),
            'missing': self.df.isnull().sum().to_dict()
        }

    def detect_outliers(self, column, method='iqr'):
        """Détecte les valeurs aberrantes"""
        if method == 'iqr':
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            return (self.df[column] < lower) | (self.df[column] > upper)
        return None
```


## 🧹 Exercice 2 : Nettoyage des Données (20 min)

### Objectif

Nettoyer et préparer les données pour l'analyse.

### Instructions

1. **Créez un preprocessor** :

   ```
   Crée src/preprocessor.py avec une classe DataPreprocessor qui :
   - Gère les valeurs manquantes (imputation ou suppression)
   - Supprime les doublons
   - Corrige les types de données
   - Normalise les valeurs (ex: dates, noms de catégories)
   - Détecte et traite les outliers
   ```

2. **Ajoutez des transformations** :

   ```
   Ajoute des méthodes pour :
   - Extraire des informations temporelles (mois, jour de la semaine, is_weekend)
   - Encoder les variables catégorielles (one-hot encoding)
   - Normaliser/standardiser les variables numériques
   - Créer des features dérivées APPROPRIÉES (voir section Data Leakage ci-dessous)
   ```

   ### ⚠️ ATTENTION : Data Leakage !

   **Data leakage** = utiliser des informations qui contiennent déjà la réponse.

   **❌ À NE PAS FAIRE** :

   ```python
   # Si revenue = quantity × price, NE PAS créer :
   df['quantity_x_price'] = df['quantity'] * df['price']  # = revenue !
   df['subtotal'] = df['quantity'] * df['price'] * (1 - df['discount'])  # ≈ revenue
   ```

   **Pourquoi ?** Ces features donnent un R² = 1.0 artificiel qui n'apprend rien d'utile.

   **✅ FEATURES APPROPRIÉES** :

   ```python
   # Features qui ajoutent réellement de l'information
   df['avg_price_category'] = df.groupby('category')['price'].transform('mean')
   df['quantity_category_ratio'] = df['quantity'] / df.groupby('category')['quantity'].transform('mean')
   df['is_high_value'] = (df['price'] > df['price'].quantile(0.75)).astype(int)
   df['is_weekend'] = df['date'].dt.dayofweek >= 5
   df['month'] = df['date'].dt.month
   df['day_of_week'] = df['date'].dt.dayofweek
   ```

   **Règle d'or** : Si une feature est une combinaison mathématique exacte de la target, c'est du data leakage !

3. **Créez une pipeline de nettoyage** :

   ```
   Crée une méthode clean_pipeline() qui :
   - Applique toutes les transformations dans le bon ordre
   - Log chaque étape
   - Sauvegarde les données nettoyées dans data/processed/
   - Génère un rapport de nettoyage
   ```

   **Exemple de pipeline** :

   ```python
   def clean_pipeline(self, save_path=None):
       """Pipeline de nettoyage complet"""
       # 1. Convertir les types
       self.convert_dtypes({'date': 'datetime'})

       # 2. Imputer les valeurs manquantes
       self.handle_missing_values()

       # 3. Supprimer les doublons
       self.remove_duplicates()

       # 4. Créer des features dérivées
       self.create_derived_features()

       # 5. Traiter les outliers
       self.handle_outliers(action='cap')

       # 6. Sauvegarder
       if save_path:
           self.df.to_csv(save_path, index=False)

       return self.df
   ```

4. **Validez le nettoyage** :

   ```
   Crée des tests dans tests/test_pipeline.py pour vérifier :
   - Aucune valeur manquante après nettoyage
   - Aucun doublon
   - Types de données corrects
   - Valeurs dans les plages attendues
   ```

   **💡 Astuce** : Vérifier que les données sont vraiment nettoyées :

   ```python
   # Après le nettoyage
   assert df_clean.isnull().sum().sum() == 0, "Il reste des NaN !"
   assert df_clean.duplicated().sum() == 0, "Il reste des doublons !"
   ```

### ✅ Critères de Validation

- [ ] Preprocessor créé et fonctionnel
- [ ] Toutes les transformations sont implémentées
- [ ] Pipeline de nettoyage complète
- [ ] Données nettoyées

### 💡 Techniques de Nettoyage

**Valeurs manquantes** :

```python
# Pour colonnes numériques
df[col] = df[col].fillna(df[col].median())

# Pour colonnes catégorielles
df[col] = df[col].fillna(df[col].mode()[0])

# Exemple complet dans handle_missing_values()
def handle_missing_values(self, strategy='median'):
    """Impute les valeurs manquantes"""
    for col in self.df.select_dtypes(include=['float64', 'int64']).columns:
        if self.df[col].isnull().any():
            if strategy == 'median':
                # ✅ Assignation directe
                self.df[col] = self.df[col].fillna(self.df[col].median())
            elif strategy == 'mean':
                self.df[col] = self.df[col].fillna(self.df[col].mean())

    for col in self.df.select_dtypes(include=['object']).columns:
        if self.df[col].isnull().any():
            # ✅ Assignation directe
            self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
```

**Outliers** :

La détection et le traitement des outliers (valeurs aberrantes) est crucial pour la qualité des données.

**💡 Conseil** : Toujours **visualiser les données avant** de supprimer les outliers !

```python
# Méthode 1 : IQR (Inter-Quartile Range) - Standard
# Avantages : Simple, robuste, fonctionne pour distributions asymétriques
# Inconvénients : Facteur 1.5 arbitraire, peut être trop agressif

Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR  # Facteur 1.5 = standard
upper_bound = Q3 + 1.5 * IQR
# ✅ Assignation directe
df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

# Méthode 2 : IQR Conservateur (facteur 3.0)
# Utilise quand tu veux garder plus de données
lower_bound = Q1 - 3.0 * IQR  # Facteur 3.0 = plus conservateur
upper_bound = Q3 + 3.0 * IQR
df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

# Méthode 3 : Z-Score (pour distributions normales)
# Avantages : Basé sur écarts-types, théoriquement fondé
# Inconvénients : Suppose distribution normale, sensible aux outliers

from scipy import stats
z_scores = np.abs(stats.zscore(df[col]))
df = df[z_scores < 3]  # Garde valeurs < 3 écarts-types

# Méthode 4 : Percentiles (très conservateur)
# Avantages : Simple, garde 98% des données
# Inconvénients : Peut garder des outliers extrêmes

lower = df[col].quantile(0.01)  # 1er percentile
upper = df[col].quantile(0.99)  # 99ème percentile
df[col] = df[col].clip(lower=lower, upper=upper)
```

**⚠️ Attention** : Il est important de ne pas demander à Bob de supprimer automatiquement tous les outliers !

- Certains outliers sont des **valeurs légitimes** (ex: vente exceptionnelle)
- C'est important d'analyser le contexte métier avant de décider
- Il vaut mieux en outre systématiquement documenter les outliers supprimés

**Normalisation** :

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[col] = scaler.fit_transform(df[[col]])
```

**Encoding** :

```python
# One-hot encoding
df = pd.get_dummies(df, columns=['category'], drop_first=True)

# Label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[col] = le.fit_transform(df[col])
```

---

## 📈 Exercice 3 : Visualisation de Données (20 min)

### Objectif

Créer des visualisations pour comprendre les patterns dans les données.

### Instructions

1. **Créez un visualizer** :

   ```
   Crée src/visualizer.py avec une classe DataVisualizer qui génère :
   - Histogrammes pour les distributions
   - Box plots pour détecter les outliers
   - Scatter plots pour les corrélations
   - Bar charts pour les comparaisons
   - Time series plots pour les tendances temporelles
   - Heatmap de corrélation
   ```

2. **Créez des visualisations spécifiques** :

   ```
   Génère ces graphiques dans data/results/ :

   1. sales_by_category.png : Ventes totales par catégorie
   2. sales_trend.png : Évolution des ventes dans le temps
   3. price_distribution.png : Distribution des prix
   4. correlation_matrix.png : Matrice de corrélation
   5. customer_demographics.png : Répartition par âge et genre
   6. regional_performance.png : Performance par région
   ```

3. **Créez un dashboard** :

   ```
   Crée un notebook notebooks/03_visualization.ipynb qui :
   - Charge les données nettoyées
   - Génère toutes les visualisations
   - Ajoute des commentaires et insights
   - Utilise un style cohérent (seaborn style)
   ```

4. **Analysez les insights** :
   ```
   Crée data/results/insights.md avec :
   - Top 3 produits les plus vendus
   - Catégorie la plus rentable
   - Tendances temporelles observées
   - Corrélations intéressantes
   - Recommandations business
   ```

### ✅ Critères de Validation

- [ ] Visualizer créé avec au moins 6 types de graphiques
- [ ] Toutes les visualisations générées
- [ ] Notebook interactif créé
- [ ] Insights documentés
- [ ] Graphiques clairs et informatifs

### 💡 Exemples de Visualisations

**Configuration de base** :

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Style global
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
```

**Ventes par catégorie (Bar chart)** :

```python
sales_by_cat = df.groupby('category')['total_sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sales_by_cat.plot(kind='bar', color='steelblue')
plt.title('Total Sales by Category', fontsize=14, fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('data/results/sales_by_category.png', dpi=300)
plt.close()
```

**Évolution temporelle (Line plot)** :

```python
df['date'] = pd.to_datetime(df['date'])
daily_sales = df.groupby('date')['total_sales'].sum()
plt.figure(figsize=(12, 6))
daily_sales.plot(color='darkgreen', linewidth=2)
plt.title('Sales Trend Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('data/results/sales_trend.png', dpi=300)
plt.close()
```

**Matrice de corrélation (Heatmap)** :

```python
numeric_cols = df.select_dtypes(include=[np.number]).columns
corr_matrix = df[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=1)
plt.title('Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('data/results/correlation_matrix.png', dpi=300)
plt.close()
```

**Distribution (Histogram)** :

```python
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=30, color='coral', edgecolor='black', alpha=0.7)
plt.title('Price Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.axvline(df['price'].mean(), color='red', linestyle='--',
            linewidth=2, label=f'Mean: ${df["price"].mean():.2f}')
plt.legend()
plt.tight_layout()
plt.savefig('data/results/price_distribution.png', dpi=300)
plt.close()
```

💡 **Conseil** : Toujours fermer les figures avec `plt.close()` pour éviter les fuites mémoire.

---

## 🤖 Exercice 4A : Machine Learning - Base (20 min)

### Objectif

Construire et comparer plusieurs modèles de machine learning.

### Instructions

1. **Définissez le problème** :

   ```
   Objectif : Prédire le montant total des ventes (revenue)
   en fonction des autres variables.

   Type : Régression
   Target : revenue (montant en €)

   Features à utiliser :
   ✅ quantity, price, customer_age (originales)
   ✅ month, day_of_week, is_weekend (temporelles)
   ✅ category_*, region_* (encodées one-hot)
   ✅ discount, shipping_cost (si disponibles)

   Features à EXCLURE :
   ❌ quantity_x_price (= revenue par définition)
   ❌ Toute combinaison exacte de la target
   ```

2. **Créez un modèle** :

   ```
   Crée src/model.py avec une classe SalesPredictor qui :
   - Sépare les données en train/test (80/20)
   - Prépare les features en EXCLUANT les features problématiques
   - Entraîne 2-3 modèles simples :
     * Linear Regression (baseline)
     * Random Forest (recommandé)
     * Gradient Boosting (optionnel)
   - Compare les performances (RMSE, R², MAE)
   - Sélectionne le meilleur modèle
   ```

   **⚠️ Vérification importante** : il est important de s'assurer que le script de préparation exclus bien les features de data leakage

   ```python
   # Dans prepare_features(), exclure les features de data leakage
   exclude_cols = [
       'date', 'product', 'customer_gender',  # Identifiants/non encodés
       'revenue',  # Target
       'quantity_x_price',  # = revenue (data leakage!)
       'customer_age_x_price'  # Corrélation artificielle
   ]
   ```

3. **Évaluez les modèles** :
   ```
   Crée une analyse de base :
   - Métriques de performance sur le test set
   - Feature importance (top 5 variables importantes)
   - Graphique simple : prédictions vs réalité
   - Sauvegarde le meilleur modèle (joblib)
   ```

### ✅ Critères de Validation

- [ ] Au moins 2 modèles entraînés et comparés
- [ ] R² entre 0.70 et 0.90 sur le test set (réaliste)
- [ ] Feature importance calculée
- [ ] Modèle sauvegardé
- [ ] Rapport de comparaison créé

### 💡 Comprendre les Résultats

**Qu'est-ce qu'un bon R² ?**

| R²              | Interprétation | Action                                      |
| --------------- | -------------- | ------------------------------------------- |
| **0.90 - 1.00** | Excellent      | ⚠️ Vérifier le data leakage !               |
| **0.70 - 0.90** | Très bon       | ✅ Objectif réaliste pour ce lab            |
| **0.50 - 0.70** | Bon            | Le modèle capture les tendances principales |
| **0.30 - 0.50** | Moyen          | Revoir les features ou le modèle            |
| **< 0.30**      | Faible         | Problème avec les données ou le modèle      |

**⚠️ Si vous obtenez R² > 0.95 ou R² = 1.0, c'est probablement du data leakage** :

Instructions pour Bob :

```
Si tu obtiens R² > 0.95 ou R² = 1.0, c'est probablement du **data leakage** :
- Vérifie que tu n'as pas inclus des features qui sont des combinaisons exactes de la target
- Exclus les features suspectes et ré-entraîne
```

**Résultats attendus avec le dataset fourni** :

- Linear Regression : R² ~ 0.70-0.80
- Random Forest : R² ~ 0.80-0.90 (meilleur attendu)
- Gradient Boosting : R² ~ 0.80-0.90

### 💡 Conseil

Focalisez vous sur la **comparaison des modèles** plutôt que l'optimisation.
L'objectif est de comprendre quel type de modèle fonctionne le mieux pour ce problème.

---

**⚠️ Note** : Cet exercice est **optionnel**. Pas la peine de le faire si vous manquez de temps.

## 🚀 Exercice 4B : Optimisation Avancée (Bonus - Optionnel)

### Objectif

Optimiser le meilleur modèle et créer une API de prédiction.

**⏱️ Temps estimé** : 15-20 minutes supplémentaires

### Instructions

1. **Optimisez les hyperparamètres** :

   ```
   Améliore le meilleur modèle obtenu jusqu'ici :
   - Utilise RandomizedSearchCV (plus rapide que GridSearch)
   - Teste 3-5 combinaisons de paramètres
   - Utilise la validation croisée (3-fold pour gagner du temps)
   - Compare avec le modèle de base
   ```

2. **Analyse approfondie** :

   ```
   Crée une analyse détaillée :
   - Graphiques de prédictions vs réalité (avec intervalles de confiance)
   - Analyse des erreurs (où le modèle se trompe ?)
   - Feature importance détaillée (top 10)
   - Rapport complet dans data/results/model_evaluation.md
   ```

3. **Créez une API de prédiction** :
   ```
   Crée src/predict_api.py qui :
   - Charge le modèle optimisé
   - Expose une fonction predict(features) au travers d'un api de façon à :
       - Valide les inputs
       - Retourner la prédiction avec un score de confiance
   ```

### ✅ Critères de Validation

- [ ] Hyperparamètres optimisés
- [ ] Amélioration mesurable vs modèle de base
- [ ] Analyse des erreurs complète
- [ ] API de prédiction fonctionnelle
- [ ] Documentation complète

### 💡 Exemple d'Optimisation Rapide

```python
from sklearn.model_selection import RandomizedSearchCV

# Paramètres à tester (exemple pour Random Forest)
param_distributions = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}

# Recherche rapide (3-fold CV, 10 combinaisons)
random_search = RandomizedSearchCV(
    RandomForestRegressor(random_state=42),
    param_distributions,
    n_iter=10,
    cv=3,
    scoring='r2',
    n_jobs=-1,
    random_state=42
)

random_search.fit(X_train, y_train)
best_model = random_search.best_estimator_
```

### 💡 Exemple de Modèle

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

class SalesPredictor:
    def __init__(self):
        self.model = None
        self.scaler = None

    def train(self, X, y):
        """Entraîne le modèle"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        self.model = RandomForestRegressor(n_estimators=100)
        self.model.fit(X_train, y_train)

        # Évaluation
        y_pred = self.model.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        r2 = r2_score(y_test, y_pred)

        return {'rmse': rmse, 'r2': r2}
```

---

**⚠️ Note** : Cet exercice est **optionnel**. Pas la peine de le faire si vous manquez de temps.

## 🎯 Exercice Bonus : Projet Complet (Optionnel)

### Mission

Créer une pipeline complète d'analyse de données de bout en bout.

### Instructions

```
Crée un projet complet qui :

1. Pipeline automatisé :
   - Script main.py qui exécute toute la pipeline
   - Logging à chaque étape
   - Gestion des erreurs
   - Configuration via fichier YAML

2. Analyse avancée :
   - Clustering des clients (K-means)
   - Analyse de séries temporelles (prévisions)
   - Détection d'anomalies
   - Analyse de sentiment (si données texte)

3. Dashboard interactif :
   - Utilise Streamlit ou Dash
   - Visualisations interactives
   - Filtres dynamiques
   - Export de rapports PDF

4. Documentation :
   - README complet
   - Docstrings pour toutes les fonctions
   - Notebook de démonstration
   - Guide d'utilisation

5. Déploiement :
   - Dockerize l'application
   - API REST pour les prédictions
   - CI/CD avec GitHub Actions
```

### ✅ Critères de Validation

- [ ] Pipeline automatisée fonctionnelle
- [ ] Au moins 2 analyses avancées
- [ ] Dashboard interactif
- [ ] Documentation complète
- [ ] Application déployable

---

## 📊 Auto-Évaluation

Avant de passer au Lab suivant, vérifiez :

- [ ] Je sais charger et explorer des données avec Bob
- [ ] Je peux nettoyer et préparer des données avec Bob
- [ ] Je sais créer des visualisations informatives avec Bob
- [ ] Je peux évaluer et optimiser des modèles avec Bob
- [ ] Je me sens à l'aise pour continuer

**Excellent travail !** 🎉

---

_Lab créé pour le Bobathon 2026_

---

## 🔧 Problèmes Courants et Solutions

### Erreur : ImportError: Import tabulate failed

**Problème** : `DataFrame.to_markdown()` nécessite la bibliothèque `tabulate`.

**Solution** :

```bash
pip install tabulate
```

### Warning : ChainedAssignmentError

**Problème** : Utilisation de `inplace=True` sur des colonnes sélectionnées.

**Solution** : Ne pas utiliser `inplace=True` sur `df[col]`. Utiliser plutôt :

```python
df[col] = df[col].fillna(value)
```

### Warning : select_dtypes avec 'object'

**Problème** : Dépréciation de `select_dtypes(include=['object'])`.

**Solution** :

```python
# Au lieu de
df.select_dtypes(include=['object'])

# Utiliser
df.select_dtypes(include=['object', 'string'])
```

### Les valeurs manquantes ne sont pas imputées

**Problème** : Utilisation incorrecte de `fillna()` avec Copy-on-Write.

**Solution** : Toujours assigner le résultat :

```python
# ❌ Ne fonctionne pas
df[col].fillna(value, inplace=True)

# ✅ Fonctionne
df[col] = df[col].fillna(value)
```

### Tests pytest échouent

**Problème** : Les données ne sont pas nettoyées correctement.

**Solution** : Vérifier que :

- Les transformations sont appliquées dans le bon ordre
- Les résultats sont assignés correctement (pas d'`inplace=True`)
- Les fixtures pytest sont bien configurées

---
