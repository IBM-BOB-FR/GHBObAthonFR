# 🚀 Lab 7 : DevOps, Automation & Playbooks

> **Durée estimée** : 90-120 minutes  
> **Niveau** : Expert ⭐⭐⭐⭐⭐  
> **Prérequis** : Connaissance en DevOps, CI/CD, et automatisation

---

## 📋 Objectifs du Lab

À la fin de ce lab, vous serez capable de :  
✅ Créer des playbooks Ansible avec Bob  
✅ Configurer des pipelines GitLab CI/CD  
✅ Intégrer des tests de performance (NeoLoad + Dynatrace)  
✅ Automatiser des workflows avec RPA et IA Factory  
✅ Utiliser l'API Marketplace et TSDL  
✅ Orchestrer des déploiements complexes  

---

## 🛠️ Technologies Utilisées

### Infrastructure & Orchestration
- **Ansible Automation Platform** - Scripts YAML, orchestration, API
- **GitLab** - SCM + CI/CD + automatisation

### Testing & Monitoring
- **Tricentis NeoLoad** - Tests de performance
- **Dynatrace** - Monitoring et observabilité
- **Intégration CI/CD** - Tests automatisés dans la pipeline

### APIs & Services
- **API Marketplace** - Catalogue d'APIs
- **TSDL** (Test Service Description Language)

---

## 🎯 Structure du Lab

```
Lab 7 : DevOps & Automation
├── Exercice 1 : Playbooks Ansible (20 min)
├── Exercice 2 : Pipeline GitLab CI/CD (25 min)
├── Exercice 3 : Tests de Performance (20 min)
├── Exercice 4 : RPA & IA Factory (25 min)
└── Exercice 5 : Projet Intégré (30 min)
```

---

## 📚 Exercice 1 : Playbooks Ansible avec Bob

**Durée** : 20 minutes  
**Objectif** : Créer des playbooks Ansible pour automatiser le déploiement

### Contexte

Vous devez créer une infrastructure complète pour une application web avec :
- Serveurs web (Nginx)
- Base de données (PostgreSQL)
- Cache (Redis)
- Monitoring (Prometheus + Grafana)

### Instructions

1. **Demandez à Bob de créer la structure du projet** :
   ```
   Crée une structure de projet Ansible dans labs/lab7-devops-automation/ansible/ 
   avec les dossiers suivants :
   - inventory/
   - playbooks/
   - roles/
   - group_vars/
   - host_vars/
   ```

2. **Créez le playbook principal** :
   ```
   Crée un playbook Ansible main.yml qui :
   1. Configure des serveurs web avec Nginx
   2. Installe et configure PostgreSQL
   3. Configure Redis pour le cache
   4. Installe Prometheus et Grafana pour le monitoring
   
   Utilise les bonnes pratiques Ansible (roles, variables, handlers, tags)
   ```

3. **Ajoutez l'orchestration via API** :
   ```
   Crée un script Python qui utilise l'API Ansible Automation Platform 
   pour lancer le playbook et récupérer les résultats
   ```

### ✅ Critères de Validation

- Structure Ansible correcte avec roles
- Playbooks idempotents
- Variables externalisées
- Handlers pour les services
- Tags pour exécution sélective
- Script API fonctionnel

### 💡 Points Clés

- Utilisez `ansible-vault` pour les secrets
- Implémentez des checks de santé
- Ajoutez des stratégies de rollback
- Documentez les variables requises

---

## 🔄 Exercice 2 : Pipeline GitLab CI/CD

**Durée** : 25 minutes  
**Objectif** : Créer une pipeline CI/CD complète avec GitLab

### Contexte

Vous devez créer une pipeline qui :
- Build l'application
- Exécute les tests unitaires et d'intégration
- Analyse la qualité du code
- Déploie sur différents environnements
- Exécute des tests de performance

### Instructions

1. **Créez le fichier .gitlab-ci.yml** :
   ```
   Crée une pipeline GitLab CI/CD dans labs/lab7-devops-automation/.gitlab-ci.yml avec :
   
   Stages:
   - build
   - test
   - quality
   - deploy-dev
   - test-performance
   - deploy-staging
   - deploy-prod
   
   Inclus:
   - Build Docker
   - Tests unitaires (pytest)
   - Tests d'intégration
   - SonarQube analysis
   - Déploiement avec Ansible
   - Tests NeoLoad
   - Monitoring Dynatrace
   ```

2. **Ajoutez les scripts de déploiement** :
   ```
   Crée des scripts de déploiement pour chaque environnement 
   qui utilisent Ansible et vérifient la santé des services
   ```

3. **Configurez les variables d'environnement** :
   ```
   Documente toutes les variables CI/CD nécessaires dans un fichier 
   VARIABLES.md avec leur description et valeurs par défaut
   ```

### ✅ Critères de Validation

- Pipeline multi-stages fonctionnel
- Déploiements conditionnels (branches, tags)
- Rollback automatique en cas d'échec
- Notifications (Slack, email)
- Artifacts et cache optimisés
- Documentation complète

### 💡 Points Clés

- Utilisez des jobs parallèles pour accélérer
- Implémentez des approval gates pour la prod
- Ajoutez des métriques de pipeline
- Utilisez GitLab Container Registry

---

## 📊 Exercice 3 : Tests de Performance Intégrés

**Durée** : 20 minutes  
**Objectif** : Intégrer NeoLoad et Dynatrace dans la CI/CD

### Contexte

Vous devez automatiser les tests de performance et le monitoring dans votre pipeline.

### Instructions

1. **Créez des scénarios NeoLoad** :
   ```
   Crée des scénarios de test NeoLoad dans labs/lab7-devops-automation/neoload/ pour :
   1. Test de charge (100 utilisateurs concurrents)
   2. Test de stress (montée en charge progressive)
   3. Test d'endurance (2 heures)
   
   Format: YAML ou JSON pour l'API NeoLoad
   ```

2. **Intégrez NeoLoad dans GitLab CI** :
   ```
   Ajoute un job dans .gitlab-ci.yml qui :
   - Lance les tests NeoLoad via API
   - Récupère les résultats
   - Fait échouer la pipeline si les SLAs ne sont pas respectés
   - Génère un rapport HTML
   ```

3. **Configurez Dynatrace** :
   ```
   Crée un script qui :
   1. Configure les tags Dynatrace pour le déploiement
   2. Crée des événements de déploiement
   3. Récupère les métriques après déploiement
   4. Valide les SLO (Service Level Objectives)
   ```

4. **Créez un dashboard de synthèse** :
   ```
   Crée un script Python qui génère un rapport combinant :
   - Résultats NeoLoad (temps de réponse, throughput)
   - Métriques Dynatrace (CPU, mémoire, erreurs)
   - Comparaison avec la baseline
   ```

### ✅ Critères de Validation

- Tests NeoLoad automatisés
- Intégration Dynatrace fonctionnelle
- SLA/SLO définis et vérifiés
- Rapports générés automatiquement
- Alertes en cas de dégradation

### 💡 Points Clés

- Définissez des baselines de performance
- Utilisez des tags pour tracer les déploiements
- Implémentez des seuils adaptatifs
- Historisez les résultats

---

## 🤖 Exercice 4 : RPA, IA Factory & Automatisation RSF

**Durée** : 25 minutes  
**Objectif** : Automatiser des processus métier avec RPA et IA

### Contexte

Vous devez automatiser des processus complexes qui impliquent :
- Validation de données
- Interactions avec des systèmes legacy
- Décisions basées sur l'IA
- Génération de rapports

### Instructions

1. **Créez un workflow RPA** :
   ```
   Crée un workflow RPA dans labs/lab7-devops-automation/rpa/ qui :
   1. Lit des données depuis une API
   2. Valide les données avec des règles métier
   3. Interagit avec un système legacy (simulation)
   4. Génère un rapport Excel
   5. Envoie le rapport par email
   
   Utilise Python + Selenium/Playwright pour l'automatisation
   ```

2. **Intégrez l'IA Factory** :
   ```
   Crée un module IA Factory qui :
   1. Utilise un modèle ML pour classifier des données
   2. Prend des décisions automatiques basées sur les prédictions
   3. Apprend des corrections manuelles (feedback loop)
   4. S'intègre dans le workflow RPA
   
   Utilise scikit-learn ou TensorFlow
   ```

3. **Automatisez les processus RSF** :
   ```
   Crée des scripts d'automatisation RSF pour :
   1. Provisioning automatique de ressources
   2. Configuration de services
   3. Validation de conformité
   4. Génération de documentation
   ```

4. **Créez un orchestrateur** :
   ```
   Crée un orchestrateur Python qui :
   - Coordonne les workflows RPA
   - Gère les files d'attente
   - Monitore l'exécution
   - Gère les erreurs et retry
   - Expose une API REST
   ```

### ✅ Critères de Validation

- Workflow RPA fonctionnel
- Modèle IA intégré et performant
- Automatisation RSF complète
- Orchestrateur robuste avec gestion d'erreurs
- Monitoring et logs détaillés

---

## 🌐 Exercice 5 : Projet Intégré - API Marketplace & TSDL

**Durée** : 30 minutes  
**Objectif** : Créer un projet complet intégrant toutes les technologies

### Mission

Créer une plateforme d'automatisation complète qui :
1. Expose des APIs via un marketplace
2. Utilise TSDL pour décrire les services de test
3. Orchestre des déploiements avec Ansible
4. Exécute des pipelines GitLab
5. Lance des tests de performance
6. Automatise des processus avec RPA

### Instructions

1. **Créez l'API Marketplace** :
   ```
   Crée une API Marketplace dans labs/lab6-devops-automation/api-marketplace/ avec :
   
   Endpoints:
   - GET /apis - Liste des APIs disponibles
   - POST /apis/{id}/deploy - Déployer une API
   - POST /apis/{id}/test - Tester une API
   - GET /apis/{id}/metrics - Métriques d'une API
   
   Fonctionnalités:
   - Catalogue d'APIs avec métadonnées
   - Déploiement automatique via Ansible
   - Tests automatiques via NeoLoad
   - Monitoring via Dynatrace
   - Documentation OpenAPI/Swagger
   ```

2. **Implémentez TSDL** :
   ```
   Crée des descripteurs TSDL pour :
   1. Tests fonctionnels
   2. Tests de performance
   3. Tests de sécurité
   4. Tests d'intégration
   
   Format YAML avec validation de schéma
   ```

3. **Créez le workflow d'automatisation complet** :
   ```
   Crée un workflow qui orchestre :
   1. Le build et les tests unitaires
   2. Le versioning du code sur GitLab qui déchenchera le build et les tests CI
   3. Le déploiement en dev avec Ansible
   4. Les tests TSDL
   5. Les tests de performance NeoLoad
   6. Le déploiement en staging (avec approval)
   7. Les tests RPA de bout en bout
   8. Le déploiement en prod (avec approval)
   9. La publication au sein de l'API Marketplace
   ```

4. **Créez un dashboard de pilotage** :
   ```
   Crée un dashboard web (React ou Vue.js) qui affiche :
   - État des pipelines en cours
   - Métriques de performance
   - Statut des déploiements
   - Résultats des tests
   - Alertes et incidents
   - Catalogue API Marketplace
   ```

### ✅ Critères de Validation

- API Marketplace fonctionnelle
- TSDL implémenté et validé
- Workflow complet automatisé
- Dashboard opérationnel
- Documentation complète
- Démo fonctionnelle de bout en bout

---

## 📊 Livrables du Lab

À la fin du lab, vous devez avoir :

### 1. Infrastructure as Code
```
ansible/
├── inventory/
│   ├── dev.yml
│   ├── staging.yml
│   └── prod.yml
├── playbooks/
│   ├── main.yml
│   ├── deploy-app.yml
│   └── rollback.yml
├── roles/
│   ├── nginx/
│   ├── postgresql/
│   ├── redis/
│   └── monitoring/
└── group_vars/
    └── all.yml
```

### 2. CI/CD Pipeline
```
.gitlab-ci.yml
scripts/
├── deploy.sh
├── test.sh
├── rollback.sh
└── health-check.sh
```

### 3. Tests & Monitoring
```
neoload/
├── scenarios/
│   ├── load-test.yaml
│   ├── stress-test.yaml
│   └── endurance-test.yaml
└── reports/

dynatrace/
├── config/
│   ├── tags.json
│   └── slo.json
└── scripts/
    └── validate-deployment.py
```

### 4. Automation
```
rpa/
├── workflows/
│   ├── data-validation.py
│   └── report-generation.py
├── ia-factory/
│   ├── models/
│   └── training/
└── orchestrator/
    └── main.py
```

### 5. API Marketplace
```
api-marketplace/
├── api/
│   ├── main.py
│   ├── models.py
│   └── routes.py
├── tsdl/
│   ├── schemas/
│   └── tests/
└── dashboard/
    └── src/
```

---

## 🎓 Sujets Couverts

### DevOps & Infrastructure
✅ Ansible Automation Platform  
✅ Infrastructure as Code  
✅ Configuration Management  
✅ Orchestration complexe  

### CI/CD
✅ GitLab CI/CD  
✅ Pipeline multi-stages  
✅ Déploiements automatisés  
✅ Stratégies de Rollback  

### Tests & Qualité
✅ Tests de performance (NeoLoad)  
✅ Monitoring (Dynatrace)  
✅ TSDL pour tests automatisés  

### Automation Avancée
✅ RPA (Robotic Process Automation)  
✅ IA Factory & ML Ops  
✅ Automatisation RSF  
✅ Orchestration de workflows  

### APIs & Integration
✅ API Marketplace  
✅ API Management   

---

## 💡 Bonnes Pratiques DevOps

### Infrastructure
- **Infrastructure as Code** : Tout doit être versionné
- **Immutable Infrastructure** : Ne jamais modifier, toujours recréer
- **Configuration Management** : Centraliser les configurations
- **Secrets Management** : Utiliser des vaults (Ansible Vault, HashiCorp Vault)

### CI/CD
- **Shift Left** : Tester tôt et souvent
- **Fail Fast** : Détecter les problèmes rapidement
- **Automated Rollback** : Retour arrière automatique en cas d'échec
- **Blue-Green Deployment** : Déploiements sans downtime

### Monitoring & Observabilité
- **Three Pillars** : Logs, Metrics, Traces
- **SLO-based Alerting** : Alertes basées sur les objectifs métier
- **Distributed Tracing** : Tracer les requêtes end-to-end
- **Chaos Engineering** : Tester la résilience

### Automatisation
- **Idempotence** : Exécutions multiples = même résultat
- **Error Handling** : Gérer tous les cas d'erreur
- **Retry Logic** : Réessayer avec backoff exponentiel
- **Circuit Breaker** : Éviter les cascades de pannes

---

## 🎉 Félicitations !

Vous avez terminé le Lab 7 - DevOps, Automation & Playbooks !

Vous maîtrisez maintenant :  
✅ L'automatisation complète avec Ansible  
✅ Les pipelines CI/CD avancés avec GitLab  
✅ Les tests de performance et le monitoring  
✅ L'automatisation intelligente avec RPA et IA  
✅ La création d'API Marketplaces  

**Vous êtes prêt(e) à automatiser n'importe quel workflow DevOps !** 🚀

---

*Lab créé pour le Bobathon 2026*
