# Guide Formateur - Lab 8 : Skills et Rules

## 📋 Vue d'Ensemble

Ce lab enseigne aux participants comment personnaliser Bob en utilisant les **Skills** (fichiers de configuration YAML) et les **Rules** (fichier de règles en Markdown) selon la documentation officielle de Bob.

**Durée** : 45-60 minutes  
**Niveau** : Avancé ⭐⭐⭐  
**Prérequis** : Labs 0, 1 et 2 recommandés

---

## 🎯 Objectifs Pédagogiques

### Compétences Acquises

1. **Comprendre les Skills de Bob**
   - Qu'est-ce qu'un skill (fichier YAML dans `.bob/skills/`)
   - Comment créer et configurer des skills
   - Quand utiliser les skills

2. **Maîtriser les Rules de Bob**
   - Qu'est-ce que le fichier rules (`.bob/rules.md`)
   - Comment écrire des rules efficaces
   - Différence entre skills et rules

3. **Créer des configurations réutilisables**
   - Combiner skills et rules
   - Partager des configurations dans l'équipe
   - Créer une bibliothèque de skills

---

## 📚 Structure du Lab

### Documents Fournis

1. **README.md** (603 lignes)
   - Guide complet du lab corrigé
   - 4 exercices progressifs + 1 bonus
   - Explications des vraies définitions

2. **REFERENCE_RAPIDE.md** (488 lignes)
   - Référence condensée
   - Templates de skills et rules
   - FAQ et troubleshooting

3. **EXEMPLES_PRATIQUES.md** (610 lignes)
   - 5 exemples concrets
   - Cas d'usage réels
   - Code généré par Bob

4. **exemples/** (nouveau)
   - `skills/` : Exemples de skills YAML
   - `rules/` : Exemples de rules Markdown

### Exercices

1. **Exercice 1** : Créer Votre Premier Skill (15 min)
   - Créer un skill Python simple
   - Comprendre la structure YAML
   - Tester avec Bob

2. **Exercice 2** : Configurer des Rules Personnalisées (15 min)
   - Créer un fichier `.bob/rules.md`
   - Définir architecture et conventions
   - Observer l'influence sur Bob

3. **Exercice 3** : Skill Avancé avec Workflow (15 min)
   - Créer un skill TDD
   - Définir un workflow
   - Automatiser un processus

4. **Exercice 4** : Workflow Complet (15 min)
   - Combiner skills et rules
   - Créer une API complète
   - Analyser la synergie

5. **Bonus** : Skills Réutilisables (15 min)
   - Créer une bibliothèque de skills
   - Partager dans l'équipe

---

## 🚀 Préparation du Lab

### Avant le Lab

1. **Vérifier l'environnement**
   ```bash
   # Python 3.8+
   python3 --version
   
   # Éditeur YAML (optionnel)
   code --install-extension redhat.vscode-yaml
   ```

2. **Préparer les participants**
   - Avoir complété les Labs 0, 1 et 2
   - Comprendre les bases de YAML
   - Avoir un projet VS Code ouvert

3. **Matériel à distribuer**
   - Lien vers le lab
   - README.md
   - REFERENCE_RAPIDE.md (à imprimer si possible)
   - Accès aux exemples

### Pendant le Lab

#### Introduction (5 min)

**Message clé** : "Skills et Rules sont les deux façons de personnaliser Bob. Skills = configuration technique (YAML), Rules = instructions contextuelles (Markdown)."

**Points à souligner** :
- **Skills** : Fichiers YAML dans `.bob/skills/` pour la configuration technique
- **Rules** : Fichier Markdown `.bob/rules.md` pour les instructions projet
- **Complémentaires** : Skills = "comment", Rules = "pourquoi et quoi"
- **Documentation officielle** : 
  - Skills : https://internal.bob.ibm.com/docs/ide/features/skills
  - Rules : https://internal.bob.ibm.com/docs/ide/configuration/rules

#### Démonstration Live (10 min)

Montrez un exemple concret :

```yaml
# 1. Créer un skill simple
# .bob/skills/python-style.yaml
name: "Python Style"
version: "1.0.0"
language: python
formatter: black
type_hints: required
```

```markdown
# 2. Créer des rules
# .bob/rules.md
# Règles du Projet

## Architecture
- Layered architecture (Routes → Services → Repositories)

## Conventions
- Classes : PascalCase
- Functions : snake_case
```

```
# 3. Demander à Bob
"Crée un service UserService qui respecte nos skills et rules"

# Observer comment Bob :
# - Applique le formatage Black (skill)
# - Utilise des type hints (skill)
# - Suit l'architecture en couches (rules)
# - Respecte les conventions de nommage (rules)
```

#### Exercices Guidés (30-40 min)

**Exercice 1** : Premier Skill (10 min)
- Expliquez la structure YAML
- Montrez comment créer `.bob/skills/`
- Faites tester avec Bob
- Insistez sur la différence avec les "compétences" génériques

**Exercice 2** : Rules Personnalisées (10 min)
- Expliquez le format Markdown
- Montrez la structure recommandée
- Faites observer l'influence sur Bob
- Clarifiez la différence avec les skills

**Exercice 3** : Skill Avancé (10 min)
- Introduisez les workflows
- Montrez comment définir des étapes
- Expliquez les cas d'usage

**Exercice 4** : Combinaison (10 min)
- Montrez la synergie skills + rules
- Faites créer une configuration complète
- Analysez les résultats ensemble

#### Conclusion (5 min)

**Récapitulatif** :
- Skills = Configuration technique (YAML)
- Rules = Instructions contextuelles (Markdown)
- Complémentaires et puissants ensemble

**Questions fréquentes** :
- "Quelle est la vraie différence ?" → Skills = config structurée, Rules = langage naturel
- "Lequel utiliser ?" → Les deux ! Ils sont complémentaires
- "Comment partager ?" → Git repo de skills + rules dans chaque projet

---

## 💡 Conseils pour le Formateur

### Do's ✅

1. **Clarifiez la confusion**
   - Expliquez que ce ne sont PAS les "compétences génériques" de Bob
   - Montrez la documentation officielle
   - Insistez sur les fichiers `.bob/skills/*.yaml` et `.bob/rules.md`

2. **Montrez des exemples concrets**
   - Utilisez les exemples fournis dans `exemples/`
   - Démontrez avec du code réel
   - Montrez l'avant/après

3. **Expliquez le "pourquoi"**
   - Pourquoi YAML pour les skills ? → Structure, réutilisabilité
   - Pourquoi Markdown pour les rules ? → Flexibilité, lisibilité
   - Pourquoi les deux ? → Complémentaires

4. **Encouragez l'expérimentation**
   - Testez différentes configurations
   - Observez l'impact sur Bob
   - Itérez et améliorez

### Don'ts ❌

1. **Ne confondez pas avec les concepts génériques**
   - Ce ne sont PAS les "8 skills" (analyse, génération, etc.)
   - Ce ne sont PAS les "7 rules" (un outil par message, etc.)
   - Ce sont des fichiers de configuration spécifiques

2. **N'allez pas trop vite**
   - YAML peut être nouveau pour certains
   - Prenez le temps d'expliquer la syntaxe
   - Montrez des exemples simples d'abord

3. **Ne négligez pas la documentation**
   - Référez toujours à la doc officielle
   - Montrez où trouver plus d'informations
   - Encouragez la lecture de la doc

---

## 🎓 Points Clés à Transmettre

### Skills (.bob/skills/*.yaml)

**Définition** : Fichiers de configuration YAML qui définissent des comportements techniques

**Structure** :
```yaml
name: "Nom"
version: "1.0.0"
# Configuration...
```

**Utilisations** :
- Standards de code (formatage, linting)
- Configuration d'outils
- Workflows automatisés
- Patterns de code

**Avantages** :
- Réutilisables
- Versionnables
- Partageables
- Structurés

### Rules (.bob/rules.md)

**Définition** : Fichier Markdown avec des instructions en langage naturel

**Structure** :
```markdown
# Règles du Projet

## Architecture
...

## Conventions
...
```

**Utilisations** :
- Architecture du projet
- Conventions d'équipe
- Contexte métier
- Décisions techniques

**Avantages** :
- Flexibles
- Lisibles
- Expressifs
- Évolutifs

### Différence Clé

| Aspect | Skills (YAML) | Rules (Markdown) |
|--------|---------------|------------------|
| Format | Structuré | Libre |
| Contenu | Configuration technique | Instructions contextuelles |
| Portée | Réutilisable entre projets | Spécifique au projet |
| Exemple | "formatter: black" | "Utiliser Black car..." |

---

## 📊 Évaluation

### Critères de Réussite

**Participant a réussi si** :
- [ ] Comprend ce qu'est un skill (fichier YAML)
- [ ] Comprend ce qu'est le fichier rules (Markdown)
- [ ] Sait créer un skill simple
- [ ] Sait écrire des rules efficaces
- [ ] Comprend la différence entre skills et rules
- [ ] Peut combiner les deux

### Questions d'Évaluation

1. **Où se trouvent les fichiers skills ?**
   - Réponse : `.bob/skills/*.yaml`

2. **Quel est le nom du fichier rules ?**
   - Réponse : `.bob/rules.md`

3. **Quelle est la différence entre skills et rules ?**
   - Réponse : Skills = config technique (YAML), Rules = instructions contextuelles (Markdown)

4. **Donnez un exemple d'utilisation de skill**
   - Réponse : Définir le formatter (black), le linter (ruff), etc.

5. **Donnez un exemple d'utilisation de rules**
   - Réponse : Décrire l'architecture, les conventions d'équipe, etc.

---

## 🔧 Dépannage

### Problèmes Courants

**"Bob n'utilise pas mon skill"**
- Solution : Vérifier que le fichier est dans `.bob/skills/`
- Solution : Vérifier la syntaxe YAML
- Solution : Demander explicitement : "en utilisant le skill X"

**"Bob ignore mes rules"**
- Solution : Vérifier que le fichier est `.bob/rules.md`
- Solution : Être plus spécifique dans les rules
- Solution : Rappeler les rules dans la demande

**"Je ne comprends pas la différence"**
- Solution : Montrer un exemple concret côte à côte
- Solution : Expliquer : Skills = technique, Rules = contexte
- Solution : Faire un exercice pratique

**"YAML est compliqué"**
- Solution : Commencer avec un exemple simple
- Solution : Utiliser un validateur YAML
- Solution : Fournir des templates

---

## 📈 Métriques de Succès

### Pour le Formateur

- **Compréhension** : 90%+ comprennent la différence skills/rules
- **Pratique** : 80%+ créent un skill et des rules fonctionnels
- **Satisfaction** : 4/5 minimum
- **Temps** : Respecter les 45-60 minutes

### Pour les Participants

- **Clarté** : Comprennent les vraies définitions
- **Pratique** : Peuvent créer des configurations
- **Autonomie** : Peuvent appliquer dans leurs projets
- **Partage** : Peuvent expliquer à leurs collègues

---

## 🎁 Ressources Supplémentaires

### À Partager Après le Lab

1. **Documentation Officielle**
   - Skills : https://internal.bob.ibm.com/docs/ide/features/skills
   - Rules : https://internal.bob.ibm.com/docs/ide/configuration/rules

2. **Exemples du Lab**
   - `exemples/skills/` : Skills Python, FastAPI
   - `exemples/rules/` : Rules pour API, Frontend

3. **Templates**
   - Template skill minimal
   - Template skill complet
   - Template rules minimal
   - Template rules complet

### Pour Aller Plus Loin

- Créer une bibliothèque de skills d'équipe
- Versionner les skills avec Git
- Automatiser la distribution des skills
- Créer des skills pour d'autres langages/frameworks

---

## 📝 Checklist Formateur

### Avant le Lab
- [ ] Environnement testé
- [ ] Exemples préparés
- [ ] Documentation accessible
- [ ] Timing vérifié

### Pendant le Lab
- [ ] Introduction claire (skills vs rules)
- [ ] Démonstration live
- [ ] Exercices guidés
- [ ] Questions/réponses
- [ ] Récapitulatif

### Après le Lab
- [ ] Feedback collecté
- [ ] Ressources partagées
- [ ] Questions répondues
- [ ] Suivi planifié

---

## 🎯 Message Final

**"Skills et Rules sont les deux piliers de la personnalisation de Bob. Skills pour la configuration technique, Rules pour le contexte projet. Ensemble, ils permettent à Bob de générer du code parfaitement adapté à vos besoins et standards. Utilisez-les, partagez-les, et votre équipe gagnera en productivité et en qualité !"**

---

## 📚 Références

### Documentation Officielle Bob

- **Skills** : https://internal.bob.ibm.com/docs/ide/features/skills
- **Rules** : https://internal.bob.ibm.com/docs/ide/configuration/rules
- **Configuration** : https://internal.bob.ibm.com/docs/ide/configuration

### Vidéos

- [Compétences vs modes vs règles – Laissez IBM Bob parler comme un pirate](https://www.youtube.com/watch?v=example)

---

_Guide créé pour le Bobathon 2026_