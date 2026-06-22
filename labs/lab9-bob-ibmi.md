# 🖥️ Lab 9 : Introduction à Bob & IBM i — Modernisation d'applications IBM i

**Durée estimée** : 60-90 minutes (~95 min pour les 6 labs complets)
**Niveau** : Intermédiaire à Avancé ⭐⭐⭐
**Prérequis** : Avoir suivi les Labs 0 et 1 (bases de Bob)

---

## 🎯 Vue d'ensemble

Six labs pratiques pour apprendre la modernisation IBM i avec Bob, votre assistant IA. Chaque lab se concentre sur un cas d'usage concret que vous pouvez réaliser rapidement.

L'application **SAMCO** est un système de gestion de commandes doté d'une interface écran vert et d'un code RPG vieux de plus de 20 ans — un exemple idéal de système à moderniser sur la plateforme IBM i !

> 💡 **Note d'introduction** : La session d'introduction à ce lab inclut une **démonstration du Package Premium Bob pour i**, qui étend les capacités de Bob (superpouvoirs) avec des centaines d'outils IBM i, des modes, des compétences (skills) dédiés IBM i. Les labs ci-dessous fonctionnent avec Bob en version standard mais ils fonctionnent encore mieux avec ce Premium Package. 

🔗 **[Accéder au lab complet sur GitHub](https://github.com/bmarolleau/IBM-i-Application-Modernization-with-Bob/blob/main/README.md)**

---

## 🎯 Les Labs

| Lab | Description | Durée |
|-----|-------------|-------|
| **Lab 0** | Découvrir l'application SAMCO — comprendre la structure, les règles métier et le flux des programmes | 15 min |
| **Lab 1** | Modernisation et refactoring RPG — convertir du code RPG à format fixe en RPG libre | 15 min |
| **Lab 2** | Créer une liste d'articles — construire une interface web moderne avec React et Carbon Design System | 15 min |
| **Lab 3** | Convertir RLA en SQL — transformer des accès RLA en SQL moderne avec JOIN | 15 min |
| **Lab 4** | Bob avec IBM i MCP — configurer Bob pour le développement IBM i avec les outils MCP et les modes personnalisés | 15 min |
| **Lab 5** | Assistant Ansible pour la gestion des PTF — automatiser la gestion système IBM i avec Bob & Ansible | 20 min |

---

## 📋 Détail des Labs

### Lab 0 : Découvrir l'application SAMCO
**Durée** : 15 minutes

**Ce que vous allez faire :**
- Demander à Bob d'expliquer la finalité et la structure de l'application SAMCO
- Comprendre les règles métier (TVA, commandes, suppressions logiques)
- Apprendre le schéma panel-step utilisé dans les programmes interactifs
- Retracer le flux complet de création d'une commande

**Cas d'usage** : Utiliser Bob comme outil de découverte pour comprendre du code legacy avant de le moderniser

---

### Lab 1 : Conversion RPG Fixe vers Libre
**Durée** : 15 minutes

**Ce que vous allez faire :**
- Demander à Bob d'expliquer du code RPG legacy
- Convertir une sous-routine du format fixe vers le format libre
- Remplacer les nombres magiques par des constantes nommées

**Cas d'usage** : Convertir la logique de chargement du sous-fichier (s01lod) en RPG moderne

---

### Lab 2 : Créer une liste d'articles
**Durée** : 15 minutes

**Ce que vous allez faire :**
- Demander à Bob de vous montrer la mise en page écran vert
- Créer des données d'exemple avec l'aide de Bob
- Construire un tableau web moderne avec recherche intégrée

**Cas d'usage** : Afficher les articles dans un navigateur web avec Carbon Design System

---

### Lab 3 : Convertir RLA en SQL
**Durée** : 15 minutes

**Ce que vous allez faire :**
- Demander à Bob d'expliquer une opération CHAIN
- La convertir en SELECT SQL
- Utiliser JOIN pour récupérer les données liées en une seule requête

**Cas d'usage** : Convertir la recherche d'articles de RLA vers SQL avec JOIN

---

### Lab 4 : Bob avec IBM i MCP
**Durée** : 15 minutes

**Ce que vous allez faire :**
- Configurer Bob pour le développement IBM i avec MCP et les modes spécialisés
- Utiliser les modes agents spécifiques à IBM i
- Interroger des systèmes IBM i en langage naturel
- Exploiter les outils IBM i préconfigurés

**Cas d'usage** : Personnaliser Bob pour le développement IBM i et tirer parti des outils spécifiques à la plateforme

---

### Lab 5 : Assistant Ansible pour la gestion des PTF
**Durée** : 20 minutes

**Ce que vous allez faire :**
- Configurer Bob avec Ansible pour l'expertise IBM i
- Générer des playbooks automatisés de vérification des PTF
- Créer des rapports de conformité pour les administrateurs système
- Explorer des scénarios AIOps pour les environnements IBM i

**Cas d'usage** : Pallier la pénurie de compétences IBM i DevOps grâce à l'automatisation système assistée par IA et la gestion des PTF

---

## 📚 Ressources

- 🔗 [Lab complet sur GitHub — IBM i Application Modernization with Bob](https://github.com/bmarolleau/IBM-i-Application-Modernization-with-Bob/blob/main/README.md)
- 🔗 [Lab 0 — Découverte de SAMCO](https://github.com/bmarolleau/IBM-i-Application-Modernization-with-Bob/blob/main/lab0-rpg-project-introduction.md)
- 🔗 [Concepts Bob & Bonnes pratiques IBM i](https://github.com/bmarolleau/IBM-i-Application-Modernization-with-Bob/blob/main/bob-concepts-and-best-practices.md)
- 🔗 [Carbon Design System](https://carbondesignsystem.com/)
- 🔗 [Code for IBM i (extension VS Code)](https://marketplace.visualstudio.com/items?itemName=HalcyonTechLtd.code-for-ibmi)

---

*Ces labs sont conçus pour les débutants en modernisation IBM i. Aucune expérience préalable en modernisation n'est requise !* 🚀
