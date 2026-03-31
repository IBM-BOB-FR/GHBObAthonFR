# Lab 4 : BobShell et Utilisation en Ligne de Commande

## Vue d'ensemble

Dans ce lab, vous apprendrez à utiliser l'interface en ligne de commande de Bob (BobShell) pour automatiser les tâches de développement, intégrer Bob dans les pipelines CI/CD et créer des scripts d'automatisation puissants. BobShell vous permet d'exploiter les capacités IA de Bob dans des scripts, des processus de build et des workflows automatisés.

> **🧠 Différenciateur Bob : [Optimisation Intelligente des Ressources](../bob-differentiators.md#2--intelligent-resource-optimization)**  
> BobShell exploite la [sélection automatique de modèles](../bob-differentiators.md#automatic-model-selection) de Bob pour optimiser chaque commande. Les tâches simples comme le formatage de code utilisent des modèles légers pour la rapidité, tandis que les analyses complexes utilisent des modèles de classe frontière pour la précision. Cela se produit automatiquement en arrière-plan, réduisant les coûts jusqu'à 60% tout en maintenant la qualité.

**Durée :** 45-60 minutes  
**Difficulté :** Intermédiaire  
**Prérequis :** Complétion des Labs 0-1-1bis, connaissances de base en ligne de commande  

## Objectifs d'apprentissage

À la fin de ce lab, vous serez capable de :

1. Utiliser BobShell pour l'exécution de commandes interactive et non-interactive
2. Créer des scripts d'automatisation qui exploitent les capacités IA de Bob
3. Intégrer Bob dans les pipelines CI/CD
4. Utiliser Bob pour la génération, l'analyse et le refactoring de code via CLI
5. Implémenter des revues de code automatisées et des vérifications de qualité
6. Créer des workflows personnalisés combinant Bob avec d'autres outils CLI

## Qu'est-ce que BobShell ?

BobShell est l'interface en ligne de commande de Bob qui fournit :

- **Mode Interactif** : Discutez avec Bob directement depuis le terminal
- **Mode Non-Interactif** : Exécutez des commandes uniques pour l'automatisation
- **Intégration de Scripts** : Utilisez Bob dans des scripts shell et des workflows d'automatisation
- **Intégration CI/CD** : Incorporez Bob dans les pipelines de build et de déploiement
- **Traitement par Lots** : Traitez plusieurs fichiers ou tâches en séquence

## Structure du Lab

```
lab4-bobshell/
├── README.md                 # Ce fichier
├── examples/                 # Exemples de commandes et cas d'usage
│   ├── basic-commands.md     # Commandes BobShell de base
│   ├── code-generation.md    # Exemples de génération de code
│   └── analysis-examples.md  # Exemples d'analyse de code
├── scripts/                  # Scripts d'automatisation
│   ├── code-review.sh        # Script de revue de code automatisée
│   ├── refactor-batch.sh     # Script de refactoring par lots
│   └── generate-docs.sh      # Script de génération de documentation
└── ci-cd/                    # Exemples d'intégration CI/CD
    ├── github-actions.yml    # Workflow GitHub Actions
    ├── gitlab-ci.yml         # Configuration GitLab CI
    └── jenkins-pipeline.txt  # Exemple de pipeline Jenkins
```

## Partie 1 : Démarrage avec BobShell

### Étape 1.1 : Installer et Vérifier BobShell

**⚠️ Important pour les utilisateurs Windows :**

BobShell ne s'installe pas automatiquement avec Bob sur Windows. Vous devez l'installer séparément en suivant le guide d'installation officiel :

👉 **[Guide d'Installation BobShell](https://bob.ibm.com/docs/shell/getting-started/install-and-setup)**

**📚 Note :** La documentation publique de Bob est disponible sur : **https://ibm.biz/bob-doc**

**Pour tous les utilisateurs**, vérifiez que BobShell est installé et accessible :

```bash
# Vérifier la version de BobShell
bob --version

# Afficher les informations d'aide
bob --help
```

**Sortie attendue :**
```
Bob CLI v1.x.x
Usage: bob [options] [command]
...
```

**Si vous voyez "command not found" ou une erreur similaire :**
- Utilisateurs Windows : Suivez le [guide d'installation](https://bob.ibm.com/docs/shell/getting-started/install-and-setup) pour installer BobShell
- Utilisateurs macOS/Linux : Vérifiez que Bob est installé et que le composant shell est activé
- Vérifiez que BobShell est dans votre PATH système

**Ce qui se passe :**
- Le flag `--version` affiche la version installée de BobShell
- Le flag `--help` montre toutes les commandes et options disponibles
- Cela confirme que BobShell est correctement installé et dans votre PATH

### Étape 1.2 : Mode Interactif

Lancez Bob en mode interactif pour discuter directement depuis le terminal :

```bash
# Démarrer une session BobShell interactive
bob
```

**Ce qui se passe :**
- Taper simplement `bob` lance une session BobShell interactive
- Vous verrez une invite où vous pouvez discuter avec Bob directement
- Toutes les capacités de Bob sont disponibles via des commandes en langage naturel

**Essayez ces commandes en mode interactif :**

```
# Demander à Bob d'expliquer un concept
> Explique ce qu'est une closure en JavaScript

# Demander la génération de code
> Crée une fonction Python pour calculer les nombres de Fibonacci

# Demander une revue de code
> Revois ce code : [coller le code ici]
```

Pour quitter le mode interactif, appuyez deux fois sur `Ctrl+C`.

**📚 En savoir plus :** Consultez la [documentation du Mode Interactif BobShell](https://bob.ibm.com/docs/shell) pour des fonctionnalités et options supplémentaires.

**Ce qui se passe :**
- Le mode interactif fournit une interface conversationnelle dans le terminal
- Vous pouvez poser des questions, demander du code et obtenir des explications
- Parfait pour des requêtes rapides sans ouvrir l'IDE complet
- L'historique de session est maintenu pendant la conversation

### Étape 1.3 : Mode Non-Interactif

Exécutez des commandes uniques sans entrer en mode interactif. Créons d'abord un fichier de test simple `calculator.py` :

```bash
# macOS/Linux
echo 'def add(a, b):
    return a + b

def multiply(x, y):
    return x * y' > calculator.py
```
```bash
# Windows (PowerShell)
@"
def add(a, b):
    return a + b

def multiply(x, y):
    return x * y
"@ | Out-File -FilePath calculator.py -Encoding UTF8
```
```bash
# Windows (CMD)
(echo def add(a, b):
echo     return a + b
echo.
echo def multiply(x, y):
echo     return x * y) > calculator.py
```

Maintenant essayez ces commandes non-interactives :

```bash
# Expliquer le code dans un fichier
bob "Explique ce que fait le fichier calculator.py"

# Demander une revue de code
bob "Revois calculator.py et suggère des améliorations"

# Générer du nouveau code
bob "Crée une fonction Python qui calcule la factorielle d'un nombre, et mets la dans un fichier factorial.py" --yolo

# Poser une question rapide
bob "Quelle est la différence entre une liste et un tuple en Python ?"
```

**Ce qui se passe :**
- Le mode non-interactif exécute une seule commande et se termine
- Utilisez simplement `bob "votre prompt"` pour des commandes ponctuelles
- Pour les commandes qui nécessitent une approbation explicite pour appeler des outils spécifiques chez Bob, vous devez ajouter l'argument --yolo pour l'auto-approbation
- Parfait pour l'automatisation et les scripts
- Les résultats sont envoyés vers stdout pour une capture facile
- Peut être chaîné avec d'autres outils CLI en utilisant des pipes

### Étape 1.4 : Utilisation de la Reprise de Session

Bob sauvegarde automatiquement vos sessions interactives, vous permettant de reprendre les conversations précédentes et de continuer là où vous vous êtes arrêté.

**Reprendre des Sessions (en mode interactif)-:**

```bash
# Lister les sessions disponibles
bob --list-sessions

# Reprendre la session la plus récente
bob --resume latest

# Reprendre une session spécifique par index
bob --resume 5
```

**Utiliser la Reprise de Session dans votre Workflow :**

Bob sauvegarde automatiquement votre historique de conversation, vous pouvez donc revenir au travail précédent :

```
# Démarrer une nouvelle session
bob

# Travailler sur votre code
> Revois calculator.py et suggère des améliorations

# Bob fournit des suggestions...

# Quitter la session (Ctrl+C deux fois)

# Plus tard, reprendre la même session
bob --resume latest

# Continuer là où vous vous êtes arrêté
> Implémentons ces suggestions maintenant
```

**Comment fonctionne la Reprise de Session :**

- Bob sauvegarde automatiquement toutes les sessions interactives
- Chaque session est indexée et peut être listée avec `--list-sessions`
- Utilisez `--resume latest` pour continuer votre travail le plus récent
- Utilisez `--resume <index>` pour revenir à une session spécifique
- L'historique de session inclut tout le contexte de conversation

**Gestion des Sessions :**

```bash
# Lister toutes les sessions disponibles
bob --list-sessions

# Supprimer une session spécifique
bob --delete-session 3

# Reprendre et continuer à travailler
bob --resume latest
```

**Quand utiliser la Reprise de Session :**

1. **Continuer le Travail :** Reprendre là où vous vous êtes arrêté après une pause
2. **Préservation du Contexte :** Maintenir le contexte de conversation entre les sessions
3. **Projets Multiples :** Basculer entre différentes sessions de projet
4. **Apprentissage et Expérimentation :** Revenir aux explorations précédentes

**Exemple de Workflow :**

```bash
# Commencer à travailler sur une fonctionnalité
bob
> Analyse myapp.js pour les problèmes de performance
# Bob identifie plusieurs problèmes
> Suggère des optimisations pour les requêtes de base de données
# Quitter la session

# Plus tard, reprendre pour continuer
bob --resume latest
> Implémentons ces optimisations de base de données maintenant
# Bob se souvient de l'analyse précédente et continue
```

**💡 Astuce :** Utilisez `--resume latest` quand vous voulez continuer votre travail le plus récent, ou `--list-sessions` pour voir toutes les sessions disponibles et en choisir une spécifique.


## Partie 2 : Génération de Code via CLI

### Étape 2.1 : Générer des Fichiers Individuels

Utilisez Bob pour générer des fichiers de code complets depuis la ligne de commande en utilisant des prompts en langage naturel :

```bash
# Générer une classe Python
bob "Crée une classe Python pour gérer un panier d'achat avec des méthodes add, remove et calculate total, dans cart.py" --yolo

#remarque: --yolo permet de changer automatiquement de mode, et en partticulier permet l'écriture de code dans le fichier demandé avec plusieurs fichiers

# Générer un composant React
bob "Crée un composant React pour une carte de profil utilisateur avec avatar, nom et bio, dans UserProfile.jsx" --yolo

# Générer un fichier de test
bob "Crée des tests unitaires pour le fichier cart.py en utilisant pytest, dans test_cart.py" --yolo
```

**Ce qui se passe :**
- Utilisez le langage naturel pour décrire le code que vous voulez
- Bob analyse la demande et génère du code approprié et fonctionnel
- Soyez spécifique sur le langage, le framework et les exigences dans votre prompt

### Étape 2.2 : Générer Plusieurs Fichiers Liés

Pour des projets complexes avec plusieurs fichiers, décrivez la structure complète :

```bash
# Générer un module API complet
bob "Crée une API REST complète pour une application todo en Python avec routes, modèles et configuration de base de données. Fournis tous les fichiers nécessaires." --yolo

# Générer des composants frontend
bob "Crée un ensemble de composants React pour un tableau de bord : Header, Sidebar, MainContent et Footer. Fournis chaque composant dans un bloc de code séparé, et cela dans un repertoire avec un nom signifiant." --yolo
```

**Ce qui se passe :**
- Décrivez la structure complète du projet dans votre prompt
- Bob fournira plusieurs blocs de code ou fichiers
- Vous pouvez enregistrer chaque partie séparément ou demander à Bob de les organiser
- Incluez des détails sur l'organisation des fichiers dans votre prompt

**💡 Astuce :** Pour les projets multi-fichiers, vous pouvez demander à Bob de fournir d'abord une structure de fichiers, puis générer chaque fichier individuellement.

### Étape 2.3 : Utilisation de Prompts Sauvegardés pour la Cohérence

Sauvegardez les prompts courants pour une utilisation répétée :

```bash
# macOS/Linux
cat > api-prompt.txt << 'EOF'
Crée un endpoint d'API REST avec :
- Validation des requêtes
- Gestion des erreurs
- Formatage des réponses
- Codes de statut HTTP appropriés
EOF

# Utiliser le prompt sauvegardé avec des détails spécifiques
bob "$(cat api-prompt.txt) Crée un endpoint POST dans /api/users pour créer de nouveaux utilisateurs, dans user-endpoint.js" --yolo

# Ou combiner avec un contexte supplémentaire
bob "$(cat api-prompt.txt) Crée un endpoint GET dans /api/products pour lister les produits avec pagination, dans products-endpoint.js" --yolo
```
```bash
# Windows (PowerShell)
@"
Crée un endpoint d'API REST avec :
- Validation des requêtes
- Gestion des erreurs
- Formatage des réponses
- Codes de statut HTTP appropriés
"@ | Out-File -FilePath api-prompt.txt -Encoding UTF8

# Utiliser le prompt sauvegardé
$prompt = Get-Content api-prompt.txt -Raw
bob "$prompt Crée un endpoint POST dans /api/users pour créer de nouveaux utilisateurs, dans user-endpoint.js" --yolo
```

**Ce qui se passe :**
- Sauvegardez les exigences communes dans des fichiers texte
- Combinez les prompts sauvegardés avec des détails spécifiques
- Assure la cohérence dans votre base de code
- Réduit la répétition dans vos prompts

## Partie 3 : Analyse et Revue de Code - Exemples de Cas d'Usage

**📝 Note :** Cette section démontre des exemples de prompts montrant comment BobShell peut être utilisé pour l'analyse et la revue de code dans des projets réels. Ce sont des exemples de référence, pas des commandes à exécuter dans le cadre de ce lab.

### Étape 3.1 : Exemples d'Analyse de Qualité de Code

BobShell peut analyser le code pour les problèmes de qualité en utilisant des prompts en langage naturel. Voici des exemples de prompts que vous pourriez utiliser dans vos projets :

```bash
# Exemple : Analyser un seul fichier
bob "Analyse la qualité du code, les performances et la sécurité de ./src/app.js"
#utilisez le nom de repertoire correspondant à votre source, comme "react-dasboad" par exemple

#Note: Pour sauvegarder l'analyse, utilisez --yolo pour éviter de capturer les messages de Bob:
bob "Analyse la qualité du code, les performances et la sécurité de ./src/app.js et sauvegarde dans analysis-report.txt" --yolo

#...ou pour générer un .md
bob "Analyse la qualité du code, les performances et la sécurité de ./src/app.js et sauvegarde dans analyse.md" --yolo


# Exemple : Analyser un répertoire entier et sauvegarder
bob "Analyse tous les fichiers dans ./src récursivement, fournis un rapport détaillé et sauvegarde dans analysis-report.txt" --yolo

# Exemple : Obtenir des métriques spécifiques
bob "Analyse ./src et fournis des métriques sur la complexité, la maintenabilité et la couverture de tests"
```

**Comment cela fonctionne :**
- Utilisez le langage naturel pour décrire ce que vous voulez que Bob analyse
- Soyez spécifique sur les aspects : qualité, performance, sécurité, etc.
- Mentionnez si vous voulez une analyse récursive de répertoire
- Utilisez la redirection de sortie (`>`) pour enregistrer les résultats dans des fichiers texte, ou utilisez `--yolo` pour générer des fichiers markdown explicitement demandés dans le prompt

### Étape 3.2 : Exemples de Revue de Code Automatisée

BobShell peut effectuer des revues de code complètes en utilisant des prompts conversationnels. Exemples de prompts :

```bash
# Exemple : Revoir les changements dans une branche
bob "Revois les changements de code entre main et feature-branch"

# Exemple : Revoir des fichiers spécifiques avec un guide de style
bob "Revois les composants React dans ./src/components en suivant le guide de style Airbnb"

# Exemple : Revoir avec un focus spécifique et sauvegarder
bob "Revois ./src pour les problèmes de qualité de code, fournis des suggestions au format markdown et sauvegarde dans review-report.md" --yolo
```

**Comment cela fonctionne :**
- Décrivez quel code vous voulez revoir (fichiers, répertoires, changements git)
- Spécifiez les guides de style ou standards à suivre (Airbnb, Google, etc.)
- Mentionnez les domaines de focus spécifiques (sécurité, performance, meilleures pratiques)
- Utilisez la redirection de sortie pour enregistrer les rapports de revue

### Étape 3.3 : Exemples d'Analyse de Sécurité

BobShell peut scanner le code pour les vulnérabilités de sécurité en utilisant le langage naturel. Exemples de prompts :

```bash
# Exemple : Scan de sécurité avec focus sur la sévérité
bob "Scanne ./src pour les vulnérabilités de sécurité de haute et critique sévérité"

# Exemple : Vérifier des vulnérabilités spécifiques
bob "Vérifie ./src pour les injections SQL, XSS et secrets exposés"

# Exemple : Générer un rapport de sécurité
bob "Effectue une analyse de sécurité complète de ./src et génère un rapport securite.html" --yolo
```

**Comment cela fonctionne :**
- Demandez à Bob de scanner ou analyser pour les problèmes de sécurité
- Spécifiez les niveaux de sévérité (haute, critique) ou types de vulnérabilités
- Demandez des formats de sortie spécifiques (HTML, markdown, JSON)
- Similaire aux vulnérabilités que vous avez corrigées dans le Lab 2

**💡 Quand utiliser ces prompts :**
- Pendant les revues de code avant de fusionner les pull requests
- Dans le cadre des pipelines CI/CD pour les vérifications de qualité automatisées
- Lors de l'audit de bases de code existantes pour les problèmes de sécurité
- Pour générer des rapports de conformité et de sécurité

## Partie 4 : Scripts d'Automatisation

### Étape 4.1 : Script de Revue de Code Automatisée

Dans ce lab,, nous vous demandons d'examiner des scripts, mais pas de les effectuer, car cela suppose que vous disposiez de code géré dans git, dans différentes branches.
Si vous souhaitez néanmoins executer ces scripts, il faut mettre en place l'envrironnement qui va avec.

**Fichier : `scripts/code-review.sh`**

Ce script effectue une revue de code automatisée sur les fichiers modifiés :

```bash
#!/bin/bash
# Script de Revue de Code Automatisée
# Revoit tous les fichiers modifiés dans la branche actuelle

# Configuration
BRANCH="${1:-main}"
OUTPUT_DIR="./review-reports"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Créer le répertoire de sortie
mkdir -p "$OUTPUT_DIR"

# Obtenir la liste des fichiers modifiés
echo "Comparaison avec la branche : $BRANCH"
CHANGED_FILES=$(git diff --name-only "$BRANCH"...HEAD | grep -E '\.(js|jsx|ts|tsx|py|java)$')

if [ -z "$CHANGED_FILES" ]; then
    echo "Aucun fichier de code modifié"
    exit 0
fi

echo "Fichiers à revoir :"
echo "$CHANGED_FILES"

# Revoir chaque fichier
for file in $CHANGED_FILES; do
    if [ -f "$file" ]; then
        echo "Revue de : $file"
        REPORT_FILE="$OUTPUT_DIR/${file//\//_}_review_$TIMESTAMP.md"
        bob "Revois $file pour la qualité du code, les bugs potentiels et les meilleures pratiques et sauvegarde le rapport dans $REPORT_FILE" --yolo
    fi
done

# Générer un rapport de synthèse
echo "Génération du rapport de synthèse..."
SUMMARY_FILE="$OUTPUT_DIR/summary_$TIMESTAMP.md"
bob "Crée un résumé de toutes les revues de code dans $OUTPUT_DIR et sauvegarde dans $SUMMARY_FILE" --yolo

echo "Revue terminée ! Rapports sauvegardés dans $OUTPUT_DIR"
```

**Usage :**
```bash
# Revoir les changements par rapport à la branche main
./scripts/code-review.sh

# Revoir les changements par rapport à une branche différente
./scripts/code-review.sh develop
```

**Ce qui se passe :**
- Le script identifie tous les fichiers de code modifiés en utilisant git diff
- Chaque fichier est revu individuellement par Bob
- Les revues sont sauvegardées en tant que fichiers markdown avec horodatage
- Un rapport de synthèse agrège toutes les découvertes
- Parfait pour les vérifications pré-commit ou pré-fusion

### Étape 4.2 : Script de Refactoring par Lots

**Fichier : [`scripts/refactor-batch.sh`](scripts/refactor-batch.sh)**

Ce script refactorise en toute sécurité plusieurs fichiers selon des critères spécifiés en utilisant l'interface en langage naturel de Bob.

**Fonctionnalités :**
- Création automatique de sauvegarde avant le refactoring
- Plusieurs types de refactoring : moderniser, optimiser, nettoyer, sécurité
- Traite plusieurs fichiers par lots
- Journalisation détaillée et gestion des erreurs
- Restauration automatique en cas d'échec
- Invite de confirmation avant de procéder

**Usage :**
```bash
# Moderniser le code dans le répertoire actuel
./scripts/refactor-batch.sh modernize .

# Optimiser les performances dans le répertoire src
./scripts/refactor-batch.sh optimize ./src

# Nettoyer le code
./scripts/refactor-batch.sh cleanup ./lib

# Corriger les problèmes de sécurité
./scripts/refactor-batch.sh security ./src
```

**Exemple de sortie :**
```
Refactoring par Lots
================================
Type de Refactoring : modernize
Répertoire Cible : ./src
Répertoire de Sauvegarde : ./refactor-backups/20240202_143000

Création de la Sauvegarde ... ✓ Terminé
Recherche de Fichiers ... ✓ 15 fichier(s) trouvé(s)

Refactoring des Fichiers
Traitement : ./src/app.js ... ✓ Terminé
Traitement : ./src/utils.js ... ✓ Terminé
...

Refactoring Terminé
Réussis : 15
Échoués : 0
```

**Ce qui se passe :**
- Le script crée une sauvegarde complète avant tout changement
- Utilise les prompts en langage naturel de Bob pour le refactoring
- Chaque fichier est traité individuellement avec gestion des erreurs
- Les fichiers échoués sont automatiquement restaurés depuis la sauvegarde
- Génère un rapport détaillé de tous les changements

**💡 Astuce :** Consultez le [script complet](scripts/refactor-batch.sh) pour voir comment l'interface en langage naturel de Bob gère le refactoring par lots en toute sécurité.

Vous pouvez tester ces scripts sur du code précédemment créé ou généré dans un lab antérieur, en donnant les bons chemins relatifs.

### Étape 4.3 : Script de Génération de Documentation

**Fichier : [`scripts/generate-docs.sh`](scripts/generate-docs.sh)**

Ce script complet génère automatiquement une documentation complète pour votre base de code en utilisant l'interface en langage naturel de Bob.

**Fonctionnalités :**
- Génère la documentation API
- Crée la documentation d'architecture
- Produit des exemples d'utilisation
- Génère README, CHANGELOG, guide CONTRIBUTING
- Crée des guides FAQ et de dépannage
- Supporte les formats de sortie markdown et HTML
- Inclut une journalisation détaillée et la gestion des erreurs

**Usage :**
```bash
# Générer la documentation pour le répertoire actuel (format markdown)
./scripts/generate-docs.sh

# Générer la documentation pour un répertoire spécifique
./scripts/generate-docs.sh ./src ./documentation

# Générer la documentation HTML
./scripts/generate-docs.sh ./src ./docs html
```

**Exemple de sortie :**
```
Génération de Documentation
================================
Source : ./src
Sortie : ./docs
Format : markdown

Génération de la Documentation API ... ✓ Terminé
Génération de la Documentation d'Architecture ... ✓ Terminé
Génération des Exemples d'Utilisation ... ✓ Terminé
Génération du README ... ✓ Terminé
Génération du Changelog ... ✓ Terminé
Génération du Guide de Contribution ... ✓ Terminé

Génération de Documentation Terminée
8 fichier(s) de documentation généré(s)
```

**Ce qui se passe :**
- Le script utilise les prompts en langage naturel de Bob pour générer chaque type de documentation
- Crée automatiquement une suite de documentation complète
- Génère README et changelog depuis l'historique git
- Supporte plusieurs formats de sortie (markdown, HTML)
- Inclut une page d'index HTML pour une navigation facile
- Fournit une journalisation détaillée pour le dépannage

**💡 Astuce :** Consultez le [script complet](scripts/generate-docs.sh) pour voir comment l'interface en langage naturel de Bob est utilisée pour la génération automatique de documentation.

Vous pouvez tester ces scripts sur du code précédemment créé ou généré, en donnant les bon chemins relatifs.

## Partie 5 : Intégration CI/CD

### Étape 5.1 : Intégration GitHub Actions

Consultez la configuration complète du workflow GitHub Actions dans [`ci-cd/github-actions.yml`](ci-cd/github-actions.yml).

**Fonctionnalités Clés :**
- S'exécute sur chaque pull request et push vers main/develop
- Installe et configure Bob CLI dans l'environnement CI
- Effectue une revue de code sur les fichiers modifiés en utilisant des prompts en langage naturel
- Exécute un scan de sécurité et une analyse de qualité
- Télécharge les rapports en tant qu'artefacts
- Poste des commentaires de revue directement sur les pull requests
- Échoue le build si des problèmes de sécurité critiques sont trouvés

**Démarrage Rapide :**
1. Copiez `ci-cd/github-actions.yml` vers `.github/workflows/bob-ci.yml` dans votre dépôt
2. Ajoutez `BOB_API_KEY` aux secrets de votre dépôt (Settings > Secrets and variables > Actions)
3. Personnalisez les seuils de qualité et les niveaux d'analyse selon vos besoins

### Étape 5.2 : Intégration GitLab CI

Consultez la configuration complète GitLab CI dans [`ci-cd/gitlab-ci.yml`](ci-cd/gitlab-ci.yml).

**Fonctionnalités Clés :**
- Pipeline multi-étapes : setup, review, security, quality, documentation, report
- Chaque étape produit des artefacts pour revue
- Le scan de sécurité fait échouer la pipeline si des problèmes critiques sont identifiés
- La vérification de qualité impose un score de qualité minimum
- Analyse de complexité et de dépendances pour des vérifications approfondies
- Génération de la documentation sur la branche main
- Génération d'un rapport de synthèse avec tous les résultats

**Démarrage Rapide :**
1. Copiez `ci-cd/gitlab-ci.yml` vers `.gitlab-ci.yml` à la racine de votre dépôt
2. Ajoutez `BOB_API_KEY` comme variable CI/CD (Settings > CI/CD > Variables)
3. Configurez la rétention des artefacts et les seuils de qualité selon vos besoins

### Étape 5.3 : Intégration Pipeline Jenkins

Consultez la configuration complète de la pipeline Jenkins dans [`ci-cd/jenkins-pipeline.groovy`](ci-cd/jenkins-pipeline.groovy).

**Fonctionnalités Clés :**
- Pipeline multi-étapes avec intégration Bob
- Credentials gérés en toute sécurité via Jenkins
- La revue de code s'exécute uniquement sur les pull requests en utilisant des prompts en langage naturel
- Le scan de sécurité échoue le build sur les problèmes critiques
- L'analyse de qualité marque le build comme instable si en dessous du seuil
- Étapes d'analyse de complexité et de dépendances
- Documentation générée et publiée sur la branche main
- Paramètres de build pour des niveaux d'analyse personnalisables
- Artefacts archivés pour toutes les étapes
- Workspace nettoyé après exécution

**Démarrage Rapide : ceci est un mode d'emploi générique. Il n'est pas demandé pour ce lab de le rendre opérationnel, car cela demande la mise en place d'un environnement CI/CD**
1. Copiez le contenu de `ci-cd/jenkins-pipeline.groovy` vers un `Jenkinsfile` à la racine de votre dépôt
2. Ajoutez la clé API Bob comme credential Jenkins avec l'ID `bob-api-key` (Jenkins > Credentials > System > Global credentials)
3. Installez les plugins Jenkins requis : Pipeline, Git, HTML Publisher, Email Extension
4. Configurez le webhook pour les builds automatiques
5. Personnalisez les seuils de qualité et les niveaux d'analyse selon vos besoins

## Partie 6 : Workflows Avancés

### Étape 6.1 : Combiner Bob avec d'Autres Outils

Créez des workflows puissants en combinant Bob avec d'autres outils CLI :

```bash
# Trouver les commentaires TODO et créer des tâches
# Cette commande peut être effectivement testée sur le répertoire ./scr de ce lab4-bobshell
grep -r "TODO" ./src | bob "Convertis ces commentaires TODO en issues GitHub avec un formatage approprié au format JSON dans issues.json" --yolo

# Analyser l'historique git et générer des insights
git log --since="1 month ago" --pretty=format:"%h %s" | bob "Analyse ces messages de commit et fournis des insights sur les patterns de développement au format markdown" > dev-insights.md
#cette commande nécessite un historique git ancien

# Traiter les résultats de tests
npm test -- --json | bob "Analyse ces résultats de tests et suggère des améliorations au format markdown test-analysis.md" --yolo
#cette commande nécessite un fichier package.json avec un script "test". Ne pas la lancer dans ce lab4-bobshell
# si besoin, pour que ce test fonctionne, faite d'abord:
cd labs/lab4-bobshell
npm install
npm test -- --json

# Vérification de style de code
if ! bob "Analyse le code source et vérifie le style de code selon les règles définies" --yolo; then
  echo "Erreur de style détectée. Vérifiez les commentaires de Bob."
  exit 1
fi
#effectivement executable dans ce lab

# Analyse de couverture de code
npm run coverage -- --json | bob "Crée un rapport de couverture avec des recommandations pour améliorer la couverture de tests au format markdown dans coverage-report.md" --yolo
```

**Ce qui se passe :**
- Pipe la sortie d'outils standard vers Bob pour l'analyse IA
- Convertit les données non structurées en insights actionnables
- Génère des rapports et des recommandations
- S'intègre parfaitement avec les chaînes d'outils existantes
- **Note** : Ici, la redirection `>` est appropriée car Bob analyse des données en entrée et produit un rapport texte en sortie, pas de la génération de fichiers de code

### Étape 6.2 : Exemple de Workflow Personnalisé

Créez un workflow pré-commit complet :
# Note: ce batch nécessite un environnement npm test

```bash
#!/bin/bash
# Workflow pré-commit avec Bob

echo "Exécution des vérifications pré-commit avec Bob..."

# 1. Formater le code
echo "Formatage du code..."
bob "Formate tout le code dans le répertoire ./src en utilisant les directives de style Prettier"

# 2. Linter le code
echo "Linting du code..."
bob lint ./src --fix

# 3. Revoir les changements
echo "Revue des changements..."
bob "Revois les changements non commités (git diff HEAD) pour les problèmes de qualité de code et sauvegarde dans pre-commit-review.md" --yolo

# 4. Vérification de sécurité
echo "Scan de sécurité..."
bob "Effectue un scan de sécurité de ./src en se concentrant sur les vulnérabilités de haute et critique sévérité et sauvegarde dans security-check.json" --yolo

# 5. Vérifier les problèmes critiques
CRITICAL=$(jq '.critical | length' security-check.json)
if [ "$CRITICAL" -gt 0 ]; then
    echo "❌ Problèmes de sécurité critiques trouvés ! Commit bloqué."
    cat security-check.json
    exit 1
fi

# 6. Exécuter les tests
echo "Exécution des tests..."
npm test

# 7. Générer une suggestion de message de commit
echo "Génération de suggestion de message de commit..."
bob "Basé sur les changements stagés, suggère un message de commit conventionnel et sauvegarde dans suggested-commit.txt" --yolo

echo "✅ Vérifications pré-commit réussies !"
echo "Message de commit suggéré :"
cat suggested-commit.txt
```

**Ce qui se passe :**
- Workflow pré-commit complet
- Formate et linte le code automatiquement
- Revoit les changements avant le commit
- Bloque les commits avec des problèmes de sécurité
- Exécute les tests pour assurer la fonctionnalité
- Suggère des messages de commit appropriés
- Assure la qualité du code au moment du commit

## Partie 7 : Meilleures Pratiques

### 7.1 : Meilleures Pratiques BobShell

1. **Utiliser des Commandes Spécifiques** : Soyez spécifique dans vos demandes pour de meilleurs résultats
   ```bash
   # Bien
   bob generate "Crée un composant React pour l'authentification utilisateur avec des champs email et mot de passe, validation et gestion des erreurs"
   
   # Moins spécifique
   bob generate "Crée un formulaire de connexion"
   ```

2. **Exploiter les Formats de Sortie** : Utilisez des formats appropriés pour différents cas d'usage
   ```bash
   # JSON pour le traitement programmatique (redirection pour capturer la sortie texte)
   bob "Analyse ./src et fournis les résultats au format JSON dans analysis.json" --yolo 

   # Markdown pour la documentation (--yolo pour générer le fichier)
   bob "Revois ./src pour la qualité du code et sauvegarde dans review.md" --yolo

   # HTML pour les rapports (--yolo pour générer le fichier)
   bob "Effectue un scan de sécurité de ./src et génère security-report.html" --yolo
   ```
   
   **Note** : Utilisez le flag`--yolo` avec le nom de fichier dans le prompt quand vous voulez que Bob génère un fichier structuré.

> **💡 Optimisation Automatique**  
> Lorsque vous exécutez des commandes BobShell, l'[optimisation intelligente des ressources](../../bob-differentiators.md#2--intelligent-resource-optim) de Bob sélectionne automatiquement le modèle le plus approprié pour chaque tâche. Vous n'avez pas besoin de spécifier quel modèle utiliser—Bob gère cela de manière transparente, optimisant à la fois la qualité et le coût.

3. **Utiliser l'Intégration Git** : Revoir uniquement le code modifié
   ```bash
   # Revoir les changements dans la branche actuelle
   bob "Revois les changements de code entre les branches main et HEAD"

   # Revoir les changements non commités
   bob "Revois les changements non commités (git diff HEAD)"
   ```

4. **Implémenter le Caching** : Utiliser les notions de session
   ```bash
    bob --resume latest "<questions à bob>"
   ```

### 7.2 : Meilleures Pratiques d'Automatisation

1. **Toujours Créer des Sauvegardes** : Avant le refactoring automatisé
2. **Utiliser le Contrôle de Version** : Commiter avant d'exécuter des changements automatisés
3. **Tester Après l'Automatisation** : Toujours vérifier que les changements automatisés fonctionnent
4. **Tout Journaliser** : Conserver les logs des opérations automatisées
5. **Gérer les Erreurs avec Élégance** : Implémenter une gestion appropriée des erreurs dans les scripts

### 7.3 : Meilleures Pratiques CI/CD

1. **Sécuriser les Clés API** : Utiliser la gestion des secrets pour les clés API Bob
2. **Définir des Seuils Appropriés** : Définir des seuils de qualité et de sécurité
3. **Archiver les Rapports** : Conserver les rapports pour l'audit et la revue
4. **Échouer Rapidement** : Arrêter la pipeline sur les problèmes critiques
5. **Fournir du Feedback** : Commenter sur les PRs avec les résultats de revue

> **🔍 Bob Findings dans CI/CD**  
> Intégrez [Bob Findings](../../bob-differentiators.md#3--bob-findings-automated-analysis-engine) dans votre pipeline CI/CD pour le scan de sécurité automatisé et les vérifications de qualité de code. Bob peut détecter les vulnérabilités et les problèmes de code avant qu'ils n'atteignent la production, avec des recommandations de remédiation spécifiques incluses dans vos rapports de pipeline.

## Exercices

### Exercice 1 : Créer un Script de Revue Personnalisé

Créez un script qui :
1. Revoit tous les fichiers Python dans un répertoire
2. Vérifie la conformité PEP 8
3. Identifie les bugs potentiels
4. Génère un rapport de synthèse

### Exercice 2 : Construire une pipeline CI/CD

Configurez une pipeline CI/CD complet qui :
1. S'exécute sur les pull requests
2. Effectue une revue de code
3. Exécute un scan de sécurité
4. Vérifie la qualité du code
5. Poste les résultats en tant que commentaires PR

### Exercice 3 : Automatiser la Documentation

Créez un workflow qui :
1. Génère la documentation API
2. Crée des exemples d'utilisation
3. Met à jour le README
4. Commite les changements de documentation

## Dépannage

### Problèmes Courants

1. **Bob CLI Non Trouvé**
   ```bash
   # Vérifier l'installation
   which bob
   
   # Réinstaller si nécessaire
   npm install -g @ibm/bob-cli
   ```

2. **Erreurs d'Authentification**
   ```bash
   # Vérifier la configuration de la clé API
   bob config get api-key
   
   # Reconfigurer si nécessaire
   bob config set api-key VOTRE_CLE_API
   ```

3. **Limitation de Débit**
   ```bash
   # Vérifier le statut de limitation de débit
   bob status
   
   # Utiliser le caching pour réduire les appels API
   bob config set cache-enabled true
   ```

## Résumé

Dans ce lab, vous avez appris :

✅ Comment utiliser BobShell pour les opérations interactives et non-interactives  
✅ Génération, analyse et revue de code via des commandes sytème  
✅ Création de scripts d'automatisation pour les tâches de développement courantes  
✅ Intégration de Bob dans des pipelines CI/CD (GitHub Actions, GitLab CI, Jenkins)  
✅ Construction de workflows personnalisés combinant Bob avec d'autres outils  
✅ Meilleures pratiques pour l'utilisation CLI et l'automatisation


## Ressources Supplémentaires

- [Documentation de Bob](https://bob.ibm.com/docs)
- [Documentation du BobShell](https://bob.ibm.com/docs/shell)

---

**Besoin d'Aide ?** Si vous rencontrez des problèmes :

0. Demandez à Bob lui-même
1. Consultez la section dépannage ci-dessus
2. Consultez la documentation BobShell
3. Posez des questions dans les forums de la communauté Bob
4. Contactez le support IBM

**Feedback :** Aidez-nous à améliorer ce lab en fournissant des retours sur ce qui a bien fonctionné et ce qui pourrait être amélioré !
