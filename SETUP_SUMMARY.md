# 🚀 Setup Summary - sensAI

**Date:** 27 Octobre 2025

---

## ✅ Ce qui a été créé

### 📋 Documentation de Planification
1. **TASKS_AI.md** - Toutes les tâches IA/ML (Personne 1)
2. **TASKS_SERVER.md** - Toutes les tâches Backend/DevOps (Personne 2)
3. **TASKS_FRONTEND.md** - Toutes les tâches UI/UX (Partagé)
4. **PROJECT_ROADMAP.md** - Roadmap complète sur 3-4 semaines avec sprints
5. **CLAUDE.md** - Documentation technique pour Claude Code

### 🎯 Système de Prompts Complet
```
backend/prompts/
├── __init__.py                    # Exports principaux
├── README.md                      # Documentation complète
├── base_prompts.py                # Prompts système de base
├── language_specific.py           # 7 langages (Python, JS, TS, Java, C++, Go, Rust)
└── specialized_prompts.py         # 8 prompts spécialisés
```

**Prompts disponibles:**
- ✅ Base system prompt (Socratic teaching)
- ✅ 7 prompts spécifiques par langage
- ✅ Performance analysis
- ✅ Security review
- ✅ Best practices
- ✅ Refactoring guide
- ✅ Debug help
- ✅ Code review checklist
- ✅ Beginner/Advanced adaptations

### 🛠️ Scripts et Outils
1. **scripts/create_github_project.py** - Script pour créer GitHub Project
2. **INSTALL_GH_CLI.md** - Instructions d'installation GitHub CLI

---

## 🎯 Prochaines Étapes IMMÉDIATES

### 1. Installer GitHub CLI (5 minutes)

```bash
# Sur Fedora 41
sudo dnf install gh -y

# Vérifier l'installation
gh --version

# S'authentifier
gh auth login
# → Choisir HTTPS
# → Choisir browser authentication
# → Suivre les instructions dans le navigateur

# Vérifier la connexion
gh auth status
```

### 2. Créer le GitHub Project (10 minutes)

**Option A: Automatique (avec le script)**
```bash
# Générer les fichiers CSV/JSON
python scripts/create_github_project.py

# OU créer les issues automatiquement
# (Besoin d'un token GitHub avec scope 'repo' et 'project')
python scripts/create_github_project.py YOUR_TOKEN owner/repo
```

**Option B: Manuel (recommandé pour débuter)**
1. Aller sur GitHub → votre repo
2. Cliquer sur "Projects" → "New project"
3. Choisir "Board" template
4. Créer les colonnes:
   - 📋 Backlog
   - 🏗️ To Do
   - 🚧 In Progress
   - 👀 Review
   - ✅ Done

5. Créer les labels:
   - `AI/ML` (violet)
   - `Backend` (bleu)
   - `Frontend` (vert)
   - `critical` (rouge)
   - `high` (orange)
   - `medium` (jaune)

6. Importer les tâches depuis les fichiers .md ou utiliser le CSV généré

### 3. Répartition du Travail

**Personne 1 (IA/ML):**
- Lire `TASKS_AI.md`
- Commencer par Sprint 1: Setup vLLM + Prompts
- Utiliser le dossier `backend/prompts/` comme base

**Personne 2 (Backend/DevOps):**
- Lire `TASKS_SERVER.md`
- Commencer par Sprint 1: Backend FastAPI complet (PRIORITÉ!)
- Suivre l'architecture dans TASKS_SERVER.md

**Ensemble:**
- Daily sync de 15 min
- Code reviews mutuels via GitHub PRs
- Communication via Slack/Discord

---

## 📊 État Actuel du Projet

### ✅ Ce qui existe
- Frontend Streamlit basique
- Composants UI (dashboard, history, chat)
- Structure frontend complète
- Prompts basiques (maintenant améliorés!)

### 🔴 Ce qui MANQUE (CRITIQUE)
- **Backend FastAPI** (n'existe pas!)
- **API /api/review** (endpoint principal)
- **Database & ORM**
- **Docker & docker-compose**
- **Intégration vLLM**

### 🎯 Priorité #1 (Semaine 1)
1. **Backend FastAPI complet** (Personne 2)
2. **vLLM + Mistral setup** (Personne 1)
3. **Integration des deux** (Ensemble)
4. **Docker Compose** (Personne 2)

---

## 📚 Documentation à Lire

### Pour Personne 1 (IA/ML)
1. `TASKS_AI.md` - Vos tâches
2. `backend/prompts/README.md` - Guide des prompts
3. `backend/prompts/language_specific.py` - Exemples de prompts
4. [vLLM Documentation](https://docs.vllm.ai/)
5. [Mistral AI Docs](https://docs.mistral.ai/)

### Pour Personne 2 (Backend/DevOps)
1. `TASKS_SERVER.md` - Vos tâches
2. `CLAUDE.md` - Architecture technique
3. [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
4. [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
5. [Docker Compose Docs](https://docs.docker.com/compose/)

### Pour les Deux
1. `PROJECT_ROADMAP.md` - Plan complet
2. `README.md` - Vue d'ensemble du projet
3. Communication et coordination!

---

## 🎯 Objectifs des 3 Prochains Jours

### Jour 1 (Aujourd'hui)
- [ ] Setup GitHub CLI
- [ ] Créer GitHub Project
- [ ] Lire la documentation respective
- [ ] Définir les horaires de sync
- [ ] Setup environnement de dev

### Jour 2-3
**Personne 1:**
- [ ] Setup vLLM local ou accès API
- [ ] Tester Mistral-7B avec prompts de base
- [ ] Optimiser les paramètres (temperature, top-p)
- [ ] Documenter les configurations

**Personne 2:**
- [ ] Créer structure backend/
- [ ] Implémenter backend/main.py (FastAPI)
- [ ] Créer models SQLAlchemy
- [ ] Implémenter endpoint /api/review (basique)

### Fin de Semaine 1
- [ ] Backend + vLLM qui communiquent
- [ ] Endpoint /api/review fonctionnel
- [ ] Frontend Streamlit connecté
- [ ] Docker Compose qui lance tout

---

## 💡 Conseils pour Démarrer

### Personne 1 (IA/ML)
```bash
# Tester les prompts localement
cd backend/prompts
python -c "
from base_prompts import SYSTEM_PROMPT, create_code_review_prompt
from language_specific import PYTHON_PROMPT

code = '''
def factorial(n):
    return n * factorial(n-1)
'''

prompt = create_code_review_prompt(code, 'python', 'Is this correct?')
print(SYSTEM_PROMPT)
print(PYTHON_PROMPT)
print(prompt)
"
```

### Personne 2 (Backend/DevOps)
```bash
# Créer la structure backend
mkdir -p backend/{api/routes,core,db,models,schemas,services,crud,middleware,scripts}
touch backend/main.py
touch backend/core/{__init__,config,security,logging,exceptions}.py
touch backend/api/routes/{__init__,review,health}.py

# Setup venv
python3 -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

---

## 🔗 Liens Utiles

### GitHub
- [Repo sensAI](https://github.com/Basmoussent/sensai)
- [GitHub CLI Docs](https://cli.github.com/manual/)
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)

### Documentation Technique
- [FastAPI](https://fastapi.tiangolo.com/)
- [vLLM](https://docs.vllm.ai/)
- [Streamlit](https://docs.streamlit.io/)
- [Docker](https://docs.docker.com/)

### Learning Resources
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LangChain Docs](https://python.langchain.com/)

---

## ❓ Questions Fréquentes

**Q: On commence par quoi exactement?**
A: Personne 1 → Setup vLLM, Personne 2 → Backend FastAPI. Voir PROJECT_ROADMAP.md Sprint 1.

**Q: Comment on se coordonne?**
A: Daily sync 15 min + GitHub PRs + Slack/Discord pour questions rapides.

**Q: Les prompts sont où?**
A: `backend/prompts/` - Tout est documenté dans le README.md du dossier.

**Q: Le backend existe déjà?**
A: Non! C'est la priorité #1. Voir TASKS_SERVER.md pour la structure à créer.

**Q: On doit tout finir en combien de temps?**
A: 3-4 semaines pour un projet production-ready. Voir PROJECT_ROADMAP.md.

---

## 🎉 Let's Go!

Tout est prêt pour démarrer. Bonne chance! 🚀

**N'oubliez pas:** L'objectif est de créer un projet impressionnant pour postuler dans des boîtes d'IA. Qualité > Quantité!

---

**Créé le:** 27 Octobre 2025
