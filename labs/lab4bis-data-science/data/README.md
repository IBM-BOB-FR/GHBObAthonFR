# 📊 Dataset de Ventes - Documentation

## Vue d'ensemble

Ce dataset contient **1000 transactions de ventes** sur l'année 2023, générées avec des **corrélations réalistes** entre les variables.

**Fichier** : `sales_data.csv`  
**Période** : 2023-01-01 à 2023-12-31  
**Lignes** : 1000  
**Colonnes** : 11

---

## 📋 Description des Colonnes

| Colonne | Type | Description | Valeurs |
|---------|------|-------------|---------|
| `date` | string | Date de la transaction | Format YYYY-MM-DD |
| `product` | string | Nom du produit vendu | 15 produits différents |
| `category` | string | Catégorie du produit | Electronics, Clothing, Food |
| `quantity` | int | Quantité vendue | 1-50 (avec quelques outliers 80-150) |
| `price` | float | Prix unitaire en euros | 10-1000 € selon catégorie |
| `customer_age` | int | Âge du client | 18-80 ans (distribution normale) |
| `customer_gender` | string | Genre du client | M, F |
| `region` | string | Région de vente | North, South, West |
| `discount` | float | Remise appliquée | 0.0-0.20 (10% des transactions) |
| `shipping_cost` | float | Frais de livraison | 0-15 € (gratuit si > 100€) |
| `revenue` | float | **TARGET** - Montant total | 19-95000 € |

---

## 🔗 Corrélations Réalistes

Le dataset a été généré avec des **patterns réalistes** :

### Corrélations avec `revenue` (target)

| Variable | Corrélation | Explication |
|----------|-------------|-------------|
| `quantity` | **+0.602** | Plus on achète, plus le montant est élevé |
| `price` | **+0.186** | Prix plus élevé → montant plus élevé |
| `customer_age` | **-0.022** | Faible corrélation (quasi nulle) |
| `discount` | **+0.046** | Faible corrélation positive |
| `shipping_cost` | **-0.074** | Faible corrélation négative |

### Patterns Temporels

- **Saisonnalité** : Plus d'électronique en novembre-décembre (fêtes)
- **Été** : Plus de vêtements en juin-août
- **Distribution** : Uniforme sur l'année avec variations saisonnières

### Patterns Régionaux

- **North** : Prix 15% plus élevés (coût de la vie)
- **South** : Prix 10% moins élevés
- **West** : Prix 5% plus élevés
- **Frais de livraison** : Plus élevés dans le North

### Patterns Démographiques

- **Jeunes (< 35 ans)** : Achètent plus d'électronique
- **Familles (35-55 ans)** : Achètent plus de nourriture
- **Distribution d'âge** : Normale centrée sur 45 ans

---

## ⚠️ Problèmes de Qualité (Intentionnels)

Le dataset contient des problèmes réalistes pour l'exercice de nettoyage :

### Valeurs Manquantes (~5%)

- **`customer_age`** : ~25 valeurs manquantes
- **`discount`** : ~25 valeurs manquantes
- **Total** : 50 valeurs manquantes (0.5% du dataset)

### Outliers (~2%)

- **`quantity`** : ~20 transactions avec quantités anormalement élevées (80-150)
- Ces outliers représentent des commandes en gros ou des erreurs de saisie

---

## 🎯 Objectif du Lab

**Prédire `revenue`** (montant total des ventes) en fonction des autres variables.

### R² Attendu

Avec des features appropriées, tu devrais obtenir :
- **Linear Regression** : R² ~ 0.70-0.80
- **Random Forest** : R² ~ 0.80-0.90 (meilleur attendu)
- **Gradient Boosting** : R² ~ 0.80-0.90

### ⚠️ Data Leakage à Éviter

**NE PAS créer ces features** (elles contiennent la réponse) :
- ❌ `quantity × price` (= revenue par définition)
- ❌ `quantity × price × (1 - discount)` (= revenue - shipping)
- ❌ Toute combinaison exacte de la target

**Features appropriées** :
- ✅ `quantity`, `price`, `customer_age` (originales)
- ✅ `month`, `day_of_week`, `is_weekend` (temporelles)
- ✅ `category_*`, `region_*` (encodées)
- ✅ `avg_price_category` (moyenne par catégorie)

---

## 📊 Statistiques Descriptives

### Revenue (Target)

- **Moyenne** : 947.53 €
- **Médiane** : ~400 € (distribution asymétrique)
- **Min** : 19.20 €
- **Max** : 94,803.72 € (outlier)
- **Écart-type** : ~2000 €

### Quantité

- **Moyenne** : ~5 unités
- **Médiane** : 3 unités
- **Min** : 1
- **Max** : 150 (outliers)

### Prix

- **Electronics** : 200-1000 € (moyenne ~500 €)
- **Clothing** : 20-150 € (moyenne ~60 €)
- **Food** : 10-50 € (moyenne ~25 €)

---

## 🔧 Utilisation

### Charger le Dataset

```python
import pandas as pd

# Charger les données
df = pd.read_csv('labs/lab4bis-data-science/data/sales_data.csv')

# Afficher les premières lignes
print(df.head())

# Informations sur le dataset
print(df.info())

# Statistiques descriptives
print(df.describe())
```

### Vérifier les Valeurs Manquantes

```python
# Compter les valeurs manquantes
print(df.isnull().sum())

# Pourcentage de valeurs manquantes
print(df.isnull().sum() / len(df) * 100)
```

### Détecter les Outliers

```python
# Méthode IQR pour quantity
Q1 = df['quantity'].quantile(0.25)
Q3 = df['quantity'].quantile(0.75)
IQR = Q3 - Q1
outliers = (df['quantity'] < Q1 - 1.5*IQR) | (df['quantity'] > Q3 + 1.5*IQR)
print(f"Outliers détectés : {outliers.sum()}")
```

---

## 📚 Références

- **Génération** : Script `generate_realistic_data.py`
- **Seed** : 42 (reproductible)
- **Méthode** : Distributions normales et poisson avec facteurs réalistes

---

*Dataset créé pour le Lab 4bis du Bobathon 2026*