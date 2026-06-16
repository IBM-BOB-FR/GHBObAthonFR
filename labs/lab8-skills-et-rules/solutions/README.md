# 📚 Solutions des Exercices - Lab 8

Ce dossier contient les solutions des 4 exercices du Lab 8 sur les Skills et Rules.

---

## 📁 Structure

```
solutions/
├── ex1-premier-skill/
│   └── .bob/skills/python-style.yaml
├── ex2-rules-personnalises/
│   └── .bob/rules.md
├── ex3-skill-avance/
│   └── .bob/skills/tdd-workflow.yaml
└── ex4-workflow-complet/
    ├── .bob/skills/api-development.yaml
    ├── .bob/skills/security.yaml
    └── .bob/rules.md
```

---

## 🎯 Exercice 1 : Premier Skill

**Fichier** : `ex1-premier-skill/.bob/skills/python-style.yaml`

**Ce que démontre cette solution** :
- ✅ Structure de base d'un skill YAML
- ✅ Sections : name, description, version
- ✅ Configuration : preferences, conventions
- ✅ Skill simple et fonctionnel

**Points clés** :
- Format YAML valide
- Préférences de style Python (PEP 8, Black, Ruff)
- Type hints requis
- Docstrings Google style

---

## 📏 Exercice 2 : Rules Personnalisées

**Fichier** : `ex2-rules-personnalises/.bob/rules.md`

**Ce que démontre cette solution** :
- ✅ Structure de base d'un fichier rules
- ✅ Sections : Architecture, Conventions, Bonnes Pratiques
- ✅ Format Markdown lisible
- ✅ Instructions claires et actionnables

**Points clés** :
- Architecture en couches définie
- Conventions de nommage explicites
- Liste de bonnes pratiques
- Liste de ce qu'il faut éviter

---

## 🔧 Exercice 3 : Skill Avancé avec Workflow

**Fichier** : `ex3-skill-avance/.bob/skills/tdd-workflow.yaml`

**Ce que démontre cette solution** :
- ✅ Skill avec workflow défini
- ✅ Étapes séquentielles (Red-Green-Refactor)
- ✅ Configuration de test (pytest, coverage)
- ✅ Conventions TDD

**Points clés** :
- Section `workflow` avec `steps`
- Chaque étape a : name, description, action
- Test framework et coverage minimum spécifiés
- Conventions TDD documentées

---

## 🎯 Exercice 4 : Workflow Complet

**Fichiers** :
- `ex4-workflow-complet/.bob/skills/api-development.yaml`
- `ex4-workflow-complet/.bob/skills/security.yaml`
- `ex4-workflow-complet/.bob/rules.md`

**Ce que démontre cette solution** :
- ✅ Configuration complète avec plusieurs skills
- ✅ Skill API : architecture, validation, documentation
- ✅ Skill Security : authentification, autorisation, vulnérabilités
- ✅ Rules : projet complet avec stack technique, conventions, sécurité

**Points clés** :
- **Séparation des préoccupations** : Un skill par domaine (API, Security)
- **Complémentarité** : Skills (technique) + Rules (contexte projet)
- **Réutilisabilité** : Les skills peuvent être réutilisés dans d'autres projets
- **Spécificité** : Les rules sont spécifiques au projet d'articles de blog

---

## 💡 Comment Utiliser Ces Solutions

### 1. Comparer avec Votre Travail

```bash
# Voir la différence
diff -r exercices/ex1-premier-skill/ solutions/ex1-premier-skill/
```

### 2. Copier pour Tester

```bash
# Copier une solution dans votre projet
cp -r solutions/ex1-premier-skill/.bob .
```

### 3. Adapter à Vos Besoins

Les solutions sont des **exemples**, pas des réponses uniques :
- Modifiez les conventions selon votre équipe
- Ajoutez des sections spécifiques à votre projet
- Combinez plusieurs skills selon vos besoins

---

## 🎓 Points d'Apprentissage

### Skills (YAML)

**Format** :
```yaml
name: "Nom du Skill"
description: "Description"
version: "1.0.0"

# Configuration spécifique
section:
  key: value
  list:
    - item1
    - item2
```

**Bonnes pratiques** :
- Un skill = un domaine (Python, API, Security, etc.)
- Versionnez vos skills (semantic versioning)
- Documentez avec description claire
- Structurez avec des sections logiques

### Rules (Markdown)

**Format** :
```markdown
# Règles du Projet

## Section 1
Contenu...

## Section 2
Contenu...
```

**Bonnes pratiques** :
- Soyez spécifique et concis
- Utilisez des sections claires
- Donnez des exemples concrets
- Listez ce qu'il faut faire ET éviter

### Combinaison Skills + Rules

**Principe** :
- **Skills** = Configuration technique réutilisable
- **Rules** = Contexte et décisions spécifiques au projet
- **Ensemble** = Bob personnalisé pour votre projet

**Exemple** :
```
Skill (api-development.yaml)     Rules (.bob/rules.md)
         ↓                              ↓
    "Utiliser FastAPI"          "Ce projet est une API
    "Valider avec Pydantic"      de blog avec JWT"
         ↓                              ↓
              ↘              ↙
            Bob comprend :
    - Framework : FastAPI
    - Validation : Pydantic
    - Contexte : Blog API
    - Auth : JWT
```

---

## 🔍 Vérification

### Checklist de Validation

Pour chaque solution, vérifiez :

**Skills** :
- [ ] Format YAML valide
- [ ] Champs obligatoires présents (name, description, version)
- [ ] Structure logique et cohérente
- [ ] Conventions claires et actionnables

**Rules** :
- [ ] Format Markdown valide
- [ ] Sections organisées logiquement
- [ ] Instructions claires et spécifiques
- [ ] Exemples concrets fournis

**Intégration** :
- [ ] Skills et rules sont complémentaires
- [ ] Pas de contradiction entre eux
- [ ] Couvrent les aspects importants du projet
- [ ] Peuvent être utilisés ensemble par Bob

---

## 🚀 Aller Plus Loin

### Exercices Supplémentaires

1. **Créez vos propres skills** pour :
   - Votre langage préféré
   - Votre framework favori
   - Vos pratiques d'équipe

2. **Écrivez des rules** pour :
   - Un projet personnel
   - Un projet d'équipe
   - Un projet open source

3. **Combinez** :
   - Plusieurs skills dans un projet
   - Skills génériques + rules spécifiques
   - Créez une bibliothèque de skills réutilisables

### Ressources

- **Documentation Skills** : https://internal.bob.ibm.com/docs/ide/features/skills
- **Documentation Rules** : https://internal.bob.ibm.com/docs/ide/configuration/rules
- **Exemples** : Consultez le dossier `exemples/` du lab

---

## 💬 Questions Fréquentes

**Q: Mes solutions sont différentes, est-ce grave ?**  
R: Non ! Il n'y a pas UNE seule bonne réponse. L'important est que vos skills/rules soient valides et utiles.

**Q: Puis-je mélanger YAML et Markdown pour les skills ?**  
R: Oui ! Les skills peuvent être en `.yaml` ou `.md`. YAML pour la structure, Markdown pour la documentation.

**Q: Combien de skills dois-je avoir ?**  
R: Commencez avec 1-2 skills de base, puis ajoutez selon vos besoins. Qualité > Quantité.

**Q: Les rules doivent-elles être longues ?**  
R: Non ! Des rules courtes et percutantes (10-20 lignes) peuvent être très efficaces. Voir `exemples/rules/ai-rag-hygiene.md`.

---

**Bravo d'avoir complété le Lab 8 ! Vous maîtrisez maintenant Skills et Rules ! 🎉**