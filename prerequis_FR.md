# Guide des Prérequis et Configuration

Ce guide vous aidera à configurer votre environnement de développement pour les labs du Bootcamp Bob.

## Table des Matières
- [Configuration Système Requise](#configuration-système-requise)
- [Logiciels Requis](#logiciels-requis)
- [Configuration des Comptes](#configuration-des-comptes)
- [Étapes de Vérification](#étapes-de-vérification)
- [Dépannage](#dépannage)

## Configuration Système Requise

### Systèmes d'Exploitation
- **Windows** : Windows 10 ou ultérieur
- **macOS** : macOS 10.15 (Catalina) ou ultérieur
- **Linux** : Ubuntu 20.04+, Fedora 33+, ou équivalent

### Matériel
- **RAM** : 4 Go minimum, 8 Go recommandé
- **Espace Disque** : 2 Go d'espace libre
- **Internet** : Connexion internet stable requise

## Logiciels Requis

### 1. Python 3.8 ou Supérieur

Python est requis pour le backend Flask dans les Labs 1 et 2.

#### Installation

**Windows :**
1. Télécharger depuis [python.org](https://www.python.org/downloads/)
2. Exécuter l'installateur
3. ✅ Cocher "Add Python to PATH"
4. Cliquer sur "Install Now"

**macOS :**
```bash
# Utiliser Homebrew (recommandé)
brew install python@3.11

# Ou télécharger depuis python.org
```

**Linux :**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

#### Vérification
```bash
python --version
# ou
python3 --version

# Devrait afficher : Python 3.8.x ou supérieur
```

#### Installer pip (si non inclus)
```bash
# Windows/macOS
python -m ensurepip --upgrade

# Linux
sudo apt install python3-pip  # Ubuntu/Debian
```

### 2. Node.js 14 ou Supérieur

Node.js est requis pour le développement JavaScript et le Lab 3.

#### Installation

**Windows/macOS :**
1. Télécharger depuis [nodejs.org](https://nodejs.org/)
2. Choisir la version LTS (recommandé)
3. Exécuter l'installateur avec les paramètres par défaut

**Linux :**
```bash
# Utiliser le dépôt NodeSource (recommandé)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs

# Ou utiliser nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install --lts
```

#### Vérification
```bash
node --version
# Devrait afficher : v14.x.x ou supérieur

npm --version
# Devrait afficher : 6.x.x ou supérieur
```

### 3. Git 2.x ou Supérieur

Git est requis pour le contrôle de version dans le Lab 1.

#### Installation

**Windows :**
1. Télécharger depuis [git-scm.com](https://git-scm.com/)
2. Exécuter l'installateur
3. Utiliser les paramètres recommandés
4. Choisir votre éditeur préféré

**macOS :**
```bash
# Utiliser Homebrew
brew install git

# Ou installer Xcode Command Line Tools
xcode-select --install
```

**Linux :**
```bash
# Ubuntu/Debian
sudo apt install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

#### Vérification
```bash
git --version
# Devrait afficher : git version 2.x.x ou supérieur
```

#### Configuration Git
```bash
# Définir votre nom et email
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@exemple.com"

# Vérifier la configuration
git config --list
```

### 4. Bob

Bob est l'assistant de développement alimenté par l'IA utilisé dans tous les labs.

#### Installation

Suivez le guide d'installation officiel de Bob pour votre plateforme :
- [Documentation d'Installation Bob](https://pages.github.ibm.com/code-assistant/bob-docs/) (interne)
- [Documentation d'Installation Bob](https://ibm.biz/bob-doc)

#### Vérification
```bash
# Vérifier que Bob est installé et accessible
bob --version

# Ou vérifier dans votre IDE/éditeur
# Bob devrait apparaître dans vos extensions/plugins
```

#### Configuration

1. **Se connecter à Bob**
   - Ouvrir l'interface Bob
   - Se connecter avec vos identifiants
   - Vérifier la connexion

2. **Configurer les Paramètres**
   - Définir le mode préféré (Architect/Code/Ask)
   - Configurer les auto-approbations (optionnel)
   - Définir les préférences de l'espace de travail

3. **Tester Bob**
   - Ouvrir le chat Bob
   - Essayer une requête simple : "Bonjour, peux-tu m'aider ?"
   - Vérifier que Bob répond

### 5. Éditeur de Texte ou IDE

Un éditeur de code est requis pour visualiser et éditer les fichiers.

#### Recommandé : Visual Studio Code

**Pourquoi VS Code ?**
- Excellente intégration avec Bob
- Terminal intégré
- Intégration Git
- Support Python et JavaScript
- Gratuit et open source

**Installation :**
1. Télécharger depuis [code.visualstudio.com](https://code.visualstudio.com/)
2. Installer avec les paramètres par défaut
3. Installer les extensions recommandées :
   - Python (Microsoft)
   - JavaScript (ES6) code snippets
   - GitLens
   - Extension Bob (si disponible)

**Éditeurs Alternatifs :**
- PyCharm (orienté Python)
- WebStorm (orienté JavaScript)
- Sublime Text
- Atom
- Vim/Neovim (utilisateurs avancés)

## Configuration des Comptes

### 1. Compte GitHub

Requis pour le Lab 1 (intégration GitHub MCP).

#### Créer un Compte
1. Aller sur [github.com](https://github.com/)
2. Cliquer sur "Sign up"
3. Suivre le processus d'inscription
4. Vérifier votre email

#### Configurer SSH (Optionnel mais Recommandé)
```bash
# Générer une clé SSH
ssh-keygen -t ed25519 -C "votre.email@exemple.com"

# Démarrer l'agent SSH
eval "$(ssh-agent -s)"

# Ajouter la clé à l'agent
ssh-add ~/.ssh/id_ed25519

# Copier la clé publique
cat ~/.ssh/id_ed25519.pub
# Copier la sortie

# Ajouter à GitHub :
# 1. Aller dans Paramètres GitHub > SSH and GPG keys
# 2. Cliquer sur "New SSH key"
# 3. Coller votre clé publique
# 4. Sauvegarder
```

#### Vérifier la Connexion SSH
```bash
ssh -T git@github.com
# Devrait afficher : Hi username! You've successfully authenticated...
```

### 2. Compte Bob

Assurez-vous que votre compte Bob est correctement configuré.

#### Étapes de Configuration
1. **Créer un Compte** (si nécessaire)
   - Visiter la page d'inscription Bob
   - Compléter le processus d'inscription
   - Vérifier l'email

2. **Configurer le Profil**
   - Définir le nom d'affichage
   - Configurer les préférences
   - Configurer l'espace de travail

3. **Connecter les Services**
   - Lier le compte GitHub (pour MCP)
   - Configurer les intégrations
   - Tester les connexions

### 3. Serveur GitHub MCP (Optionnel)

Le serveur GitHub MCP permet à Bob d'interagir directement avec GitHub.

#### Configuration
1. **Activer MCP dans Bob**
   - Ouvrir les paramètres Bob (en haut à droite de la fenêtre de chat Bob)
   - Naviguer vers les serveurs MCP
   - Activer GitHub MCP

2. **S'Authentifier**
   - Suivre le flux d'authentification
   - Accorder les permissions nécessaires
   - Vérifier la connexion

3. **Tester la Connexion**
   - Demander à Bob : "Liste mes dépôts GitHub"
   - Vérifier que Bob peut accéder à vos dépôts

## Étapes de Vérification

Exécutez ces commandes pour vérifier votre configuration :

### Script de Vérification Complet

**Windows (PowerShell) :**
```powershell
Write-Host "=== Vérification de Configuration Bootcamp Bob ===" -ForegroundColor Green

Write-Host "`nPython:" -ForegroundColor Yellow
python --version

Write-Host "`nNode.js:" -ForegroundColor Yellow
node --version

Write-Host "`nNPM:" -ForegroundColor Yellow
npm --version

Write-Host "`nGit:" -ForegroundColor Yellow
git --version

Write-Host "`nConfiguration Git:" -ForegroundColor Yellow
git config user.name
git config user.email

Write-Host "`n=== Vérification Terminée ===" -ForegroundColor Green
```

**macOS/Linux (Bash) :**
```bash
#!/bin/bash
echo "=== Vérification de Configuration Bootcamp Bob ==="

echo -e "\nPython:"
python3 --version

echo -e "\nNode.js:"
node --version

echo -e "\nNPM:"
npm --version

echo -e "\nGit:"
git --version

echo -e "\nConfiguration Git:"
git config user.name
git config user.email

echo -e "\n=== Vérification Terminée ==="
```

### Sortie Attendue

Toutes les commandes devraient retourner des numéros de version :
- ✅ Python 3.8.x ou supérieur
- ✅ Node.js 14.x.x ou supérieur
- ✅ NPM 6.x.x ou supérieur
- ✅ Git 2.x.x ou supérieur
- ✅ Git user.name et user.email configurés

## Configuration d'Environnement Virtuel Python

Il est recommandé d'utiliser des environnements virtuels pour les projets Python.

### Créer un Environnement Virtuel

```bash
# Naviguer vers le répertoire du lab
cd lab1

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows :
venv\Scripts\activate

# macOS/Linux :
source venv/bin/activate

# Votre invite devrait maintenant afficher (venv)
```

### Installer les Dépendances

```bash
# Avec l'environnement virtuel activé
pip install --upgrade pip
pip install flask flask-cors

# Vérifier l'installation
pip list
```

### Désactiver l'Environnement Virtuel

```bash
deactivate
```

## Gestion des Packages Node.js

### Initialiser un Projet Node.js

```bash
# Naviguer vers le répertoire du projet
cd frontend

# Initialiser package.json
npm init -y

# Installer les dépendances (quand nécessaire)
npm install

# Vérifier l'installation
npm list
```

## Dépannage

### Problèmes Python

**Problème** : `python: command not found`
```bash
# Essayer python3 à la place
python3 --version

# Ou ajouter Python au PATH (Windows)
# Ajouter le répertoire d'installation Python aux Variables d'Environnement Système
```

**Problème** : `pip: command not found`
```bash
# Utiliser python -m pip à la place
python -m pip --version

# Ou installer pip
python -m ensurepip --upgrade
```

**Problème** : Permission refusée lors de l'installation de packages
```bash
# Utiliser un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows

# Ou utiliser le flag --user (non recommandé)
pip install --user nom-du-package
```

### Problèmes Node.js

**Problème** : `node: command not found`
```bash
# Vérifier le chemin d'installation
which node  # macOS/Linux
where node  # Windows

# Réinstaller Node.js ou ajouter au PATH
```

**Problème** : `npm: command not found`
```bash
# npm devrait venir avec Node.js
# Réinstaller Node.js depuis nodejs.org
```

**Problème** : Erreurs de permission avec npm
```bash
# Utiliser nvm (Node Version Manager) à la place
# Ou corriger les permissions npm :
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

### Problèmes Git

**Problème** : `git: command not found`
```bash
# Vérifier l'installation
which git  # macOS/Linux
where git  # Windows

# Réinstaller Git ou ajouter au PATH
```

**Problème** : Identifiants Git non sauvegardés
```bash
# Configurer l'assistant d'identifiants
git config --global credential.helper store  # Linux
git config --global credential.helper osxkeychain  # macOS
git config --global credential.helper manager  # Windows
```

**Problème** : La connexion SSH à GitHub échoue
```bash
# Tester la connexion
ssh -T git@github.com

# Si échec, vérifier :
# 1. La clé SSH est générée
# 2. La clé SSH est ajoutée à ssh-agent
# 3. La clé publique est ajoutée à GitHub
# 4. Le service SSH est en cours d'exécution
```

### Problèmes Bob

**Problème** : Bob ne répond pas
- Vérifier la connexion internet
- Vérifier que le service Bob est en cours d'exécution
- Redémarrer l'application Bob
- Vérifier la page de statut Bob

**Problème** : Le serveur MCP ne se connecte pas
- Vérifier que MCP est activé dans les paramètres
- Se ré-authentifier avec GitHub
- Vérifier les permissions accordées
- Redémarrer Bob

**Problème** : Les auto-approbations ne fonctionnent pas
- Vérifier les paramètres d'auto-approbation
- Vérifier que la fonctionnalité est activée
- Revoir les règles d'approbation
- Contacter le support Bob

## Ressources Additionnelles

### Documentation
- [Documentation Python](https://docs.python.org/)
- [Documentation Node.js](https://nodejs.org/docs/)
- [Documentation Git](https://git-scm.com/doc)
- [Documentation Bob](https://pages.github.ibm.com/code-assistant/bob-docs/) (interne)
- [Documentation Bob](https://ibm.biz/bob-doc)

### Ressources d'Apprentissage
- [Tutoriel Python](https://docs.python.org/fr/3/tutorial/)
- [Tutoriel JavaScript](https://javascript.info/)
- [Tutoriel Git](https://git-scm.com/book/fr/v2)
- [Documentation Flask](https://flask.palletsprojects.com/)

### Support Communautaire
- Forum Communautaire Bob
- Stack Overflow
- GitHub Discussions
- Canaux Discord/Slack

## Prochaines Étapes

Une fois que vous avez complété toutes les étapes de configuration :

1. ✅ Vérifier que tous les logiciels sont installés
2. ✅ Configurer Git avec vos informations
3. ✅ Tester la connexion Bob
4. ✅ Configurer le compte GitHub et MCP
5. ✅ Créer un projet de test pour vérifier que tout fonctionne

**Prêt à commencer ?** → [Retour au README Principal](README.md) → [Démarrer le Lab 1](lab1-decouverte/README.md)

---

*Dernière Mise à Jour : Décembre 2025*  
*Version : 1.0*