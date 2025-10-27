# 🔧 Git Workflow - Guide pour les Développeurs

Guide des bonnes pratiques Git pour le projet sensAI.

---

## 📋 Table des Matières

- [Configuration Initiale](#configuration-initiale)
- [Workflow Quotidien](#workflow-quotidien)
- [Conventions de Commits](#conventions-de-commits)
- [Branches](#branches)
- [Pull Requests](#pull-requests)
- [Commandes Utiles](#commandes-utiles)

---

## 🚀 Configuration Initiale

### Cloner le Repository

```bash
# Clone via SSH (recommandé)
git clone git@github.com:Basmoussent/sensAI.git
cd sensAI

# Ou via HTTPS
git clone https://github.com/Basmoussent/sensAI.git
cd sensAI
```

### Configuration Git

```bash
# Configurer votre identité
git config user.name "Votre Nom"
git config user.email "votre.email@example.com"

# Vérifier la configuration
git config --list
```

### Installation des Dépendances

```bash
# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -e ".[dev]"
```

---

## 🔄 Workflow Quotidien

### 1. Toujours Commencer par Mettre à Jour

```bash
# S'assurer d'être sur main
git checkout main

# Récupérer les dernières modifications
git pull origin main
```

### 2. Créer une Branche pour votre Tâche

```bash
# Format: type/description-courte
git checkout -b feat/setup-vllm
git checkout -b fix/api-endpoint
git checkout -b docs/update-readme
```

### 3. Travailler sur votre Code

```bash
# Vérifier les fichiers modifiés
git status

# Voir les modifications en détail
git diff

# Ajouter les fichiers modifiés
git add fichier1.py fichier2.py
# ou tout ajouter
git add .
```

### 4. Commiter Régulièrement

```bash
# Commit avec un message clair
git commit -m "feat: add vLLM integration with Mistral-7B"

# Voir l'historique
git log --oneline
```

### 5. Pousser votre Branche

```bash
# Première fois
git push -u origin feat/setup-vllm

# Fois suivantes
git push
```

### 6. Créer une Pull Request

```bash
# Via GitHub CLI (recommandé)
gh pr create --title "feat: Setup vLLM + Mistral-7B" --body "Closes #1"

# Ou via l'interface web GitHub
```

---

## 📝 Conventions de Commits

### Format

```
<type>(<scope>): <description courte>

[corps optionnel]

[footer optionnel]
```

### Types de Commits

| Type | Description | Exemple |
|------|-------------|---------|
| `feat` | Nouvelle fonctionnalité | `feat: add code analysis endpoint` |
| `fix` | Correction de bug | `fix: resolve streaming timeout issue` |
| `docs` | Documentation | `docs: update API documentation` |
| `style` | Formatage, ponctuation | `style: format code with black` |
| `refactor` | Refactoring du code | `refactor: simplify prompt generation` |
| `perf` | Amélioration des performances | `perf: optimize database queries` |
| `test` | Ajout/modification de tests | `test: add unit tests for LLM service` |
| `chore` | Tâches de maintenance | `chore: update dependencies` |
| `ci` | CI/CD | `ci: add GitHub Actions workflow` |

### Exemples de Bons Commits

```bash
# ✅ Bon - Clair et descriptif
git commit -m "feat(backend): implement streaming SSE for code review endpoint"
git commit -m "fix(frontend): resolve syntax highlighting in code blocks"
git commit -m "docs: add setup instructions for vLLM configuration"

# ❌ Mauvais - Trop vague
git commit -m "update"
git commit -m "fix bug"
git commit -m "changes"
```

### Commits Multi-lignes

```bash
git commit -m "feat(ai): add conversation memory system

- Implement conversation_memory.py
- Track explained concepts
- Detect student level
- Add intelligent summarization

Closes #9"
```

---

## 🌿 Branches

### Nommage des Branches

**Format:** `<type>/<description-courte-en-kebab-case>`

**Types:**
- `feat/` - Nouvelle fonctionnalité
- `fix/` - Correction de bug
- `docs/` - Documentation
- `refactor/` - Refactoring
- `test/` - Tests
- `chore/` - Maintenance

**Exemples:**
```bash
feat/setup-vllm-mistral
feat/implement-auth-system
fix/streaming-timeout
docs/update-api-docs
refactor/prompt-system
test/add-unit-tests
```

### Gestion des Branches

```bash
# Lister les branches
git branch -a

# Changer de branche
git checkout main
git checkout feat/setup-vllm

# Créer et basculer sur une nouvelle branche
git checkout -b feat/new-feature

# Supprimer une branche locale
git branch -d feat/old-feature

# Supprimer une branche distante
git push origin --delete feat/old-feature
```

### Mettre à Jour sa Branche avec Main

```bash
# Option 1: Rebase (historique plus propre) - RECOMMANDÉ
git checkout feat/your-feature
git fetch origin
git rebase origin/main

# Résoudre les conflits si nécessaire
# git add <fichiers-résolus>
# git rebase --continue

git push --force-with-lease

# Option 2: Merge (plus simple mais historique moins propre)
git checkout feat/your-feature
git merge main
git push
```

---

## 🔍 Pull Requests

### Créer une Pull Request

```bash
# Via GitHub CLI (recommandé)
gh pr create \
  --title "feat: Setup vLLM + Mistral-7B" \
  --body "
## Description
Configure vLLM with Mistral-7B-Instruct-v0.3 for code review inference.

## Changes
- Install and configure vLLM
- Load Mistral-7B model
- Optimize inference parameters
- Add configuration documentation

## Testing
- [x] Model loads correctly
- [x] Inference works with sample prompts
- [x] Parameters optimized (temp: 0.7, top-p: 0.9)

## Related Issues
Closes #1
" \
  --label "AI/ML,critical,sprint-1" \
  --assignee @me
```

### Checklist PR

Avant de créer une PR, vérifier:

- [ ] Le code compile/fonctionne
- [ ] Les tests passent (`pytest`)
- [ ] Le code est formaté (`black .`, `isort .`)
- [ ] Pas d'erreurs de lint (`flake8`, `mypy`)
- [ ] La documentation est à jour
- [ ] Les commits suivent les conventions
- [ ] La branche est à jour avec `main`

### Commandes GitHub CLI pour PRs

```bash
# Créer une PR
gh pr create

# Lister vos PRs
gh pr list --author @me

# Voir le status d'une PR
gh pr view 123

# Voir les checks (CI/CD)
gh pr checks

# Merger une PR (après review)
gh pr merge 123 --squash

# Fermer une PR
gh pr close 123
```

---

## 🛠️ Commandes Utiles

### Annuler des Modifications

```bash
# Annuler les modifications d'un fichier non stagé
git restore fichier.py

# Unstage un fichier
git restore --staged fichier.py

# Annuler le dernier commit (garde les modifications)
git reset --soft HEAD~1

# Annuler le dernier commit (supprime les modifications) ⚠️
git reset --hard HEAD~1
```

### Stash (Mettre de Côté)

```bash
# Mettre de côté les modifications
git stash save "work in progress"

# Lister les stash
git stash list

# Réappliquer le dernier stash
git stash pop

# Réappliquer un stash spécifique
git stash apply stash@{0}

# Supprimer un stash
git stash drop stash@{0}
```

### Résolution de Conflits

```bash
# 1. Voir les fichiers en conflit
git status

# 2. Éditer les fichiers et résoudre les conflits
# Chercher les marqueurs: <<<<<<<, =======, >>>>>>>

# 3. Marquer comme résolu
git add fichier-resolu.py

# 4. Continuer le rebase/merge
git rebase --continue
# ou
git merge --continue

# Abandonner si nécessaire
git rebase --abort
git merge --abort
```

### Historique et Logs

```bash
# Historique condensé
git log --oneline

# Historique avec graphe
git log --oneline --graph --all

# Voir les modifications d'un fichier
git log -p fichier.py

# Qui a modifié quoi (blame)
git blame fichier.py

# Chercher dans les commits
git log --grep="vLLM"
```

### Différences

```bash
# Voir les modifications non stagées
git diff

# Voir les modifications stagées
git diff --staged

# Comparer avec une branche
git diff main..feat/my-feature

# Voir les fichiers modifiés uniquement
git diff --name-only
```

---

## 🚨 Erreurs Courantes et Solutions

### "Your branch is behind 'origin/main'"

```bash
# Solution: Pull les dernières modifications
git pull origin main
```

### "Your branch and 'origin/main' have diverged"

```bash
# Solution 1: Rebase (recommandé)
git pull --rebase origin main

# Solution 2: Merge
git pull origin main
```

### "Merge conflict"

```bash
# 1. Voir les fichiers en conflit
git status

# 2. Éditer et résoudre
# 3. Ajouter les fichiers résolus
git add .

# 4. Continuer
git rebase --continue  # si rebase
git commit             # si merge
```

### "fatal: refusing to merge unrelated histories"

```bash
# Si vous devez vraiment merger des historiques non liés
git pull origin main --allow-unrelated-histories
```

### J'ai committé sur main par erreur

```bash
# Créer une branche avec vos modifications
git branch feat/my-feature

# Revenir sur main avant le commit
git reset --hard origin/main

# Basculer sur votre branche
git checkout feat/my-feature
```

---

## 🔐 Bonnes Pratiques de Sécurité

### ⚠️ NE JAMAIS COMMITER

- ❌ Mots de passe ou tokens
- ❌ Clés API
- ❌ Fichiers `.env`
- ❌ Credentials de base de données
- ❌ Clés SSH privées

### ✅ À FAIRE

```bash
# Ajouter .env au .gitignore
echo ".env" >> .gitignore
echo "*.key" >> .gitignore
echo "credentials.json" >> .gitignore

# Vérifier avant de commiter
git status
git diff

# Utiliser des variables d'environnement
# Utiliser des secrets GitHub pour CI/CD
```

### Si vous avez committé un secret par erreur

```bash
# ⚠️ URGENT: Révoquer le secret immédiatement!
# Ensuite, supprimer de l'historique Git (complexe)
# Contacter l'équipe pour aide
```

---

## 📊 Code Review Checklist

### Pour l'Auteur (avant de créer la PR)

- [ ] Le code compile et fonctionne
- [ ] Les tests passent
- [ ] Le code est formaté (`black`, `isort`)
- [ ] Pas d'erreurs de lint
- [ ] La documentation est à jour
- [ ] Les commits sont clairs
- [ ] Pas de secrets committés
- [ ] La PR est liée à une issue

### Pour le Reviewer

- [ ] Le code est lisible et maintenable
- [ ] La logique est correcte
- [ ] Les edge cases sont gérés
- [ ] Les tests couvrent les changements
- [ ] Pas de code dupliqué
- [ ] Les erreurs sont bien gérées
- [ ] La performance est acceptable
- [ ] La sécurité est respectée

---

## 🎯 Workflow Complet - Exemple

```bash
# 1. Partir de main à jour
git checkout main
git pull origin main

# 2. Créer une branche pour votre tâche
git checkout -b feat/setup-vllm

# 3. Travailler sur votre code
# ... éditer les fichiers ...

# 4. Vérifier les modifications
git status
git diff

# 5. Tester votre code
pytest
black .
flake8

# 6. Commiter régulièrement
git add .
git commit -m "feat(ai): configure vLLM with Mistral-7B

- Install vLLM dependencies
- Load Mistral-7B-Instruct-v0.3 model
- Optimize inference parameters
- Add configuration documentation

Closes #1"

# 7. Pousser vers GitHub
git push -u origin feat/setup-vllm

# 8. Créer une Pull Request
gh pr create --title "feat: Setup vLLM + Mistral-7B" --body "Closes #1"

# 9. Attendre la review et merger
# 10. Supprimer la branche après merge
git checkout main
git pull origin main
git branch -d feat/setup-vllm
```

---

## 📚 Ressources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub CLI Manual](https://cli.github.com/manual/)

---

## 💡 Tips

### Aliases Utiles

Ajouter dans `~/.gitconfig`:

```ini
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    cm = commit -m
    lg = log --oneline --graph --all
    unstage = restore --staged
    last = log -1 HEAD
    amend = commit --amend --no-edit
```

Usage:
```bash
git st          # au lieu de git status
git co main     # au lieu de git checkout main
git lg          # joli log graphique
```

---

## 🆘 Besoin d'Aide?

- **Git Questions:** Demandez sur le Discord/Slack de l'équipe
- **GitHub Issues:** https://github.com/Basmoussent/sensAI/issues
- **Documentation:** [docs/README.md](README.md)

---

**Dernière mise à jour:** 2025-10-27
