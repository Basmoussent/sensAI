# 🗺️ PROJECT ROADMAP - sensAI

**Objectif:** Créer un projet production-ready pour postuler dans des boîtes d'IA.

**Timeline:** 3-4 semaines (adaptable selon disponibilité)

---

## 👥 Répartition des Rôles

### Personne 1 - Spécialiste IA/ML 🤖
**Focus:** Prompt engineering, intégration LLM, logique pédagogique

**Tâches principales:**
- Optimisation des prompts
- Intégration vLLM/Mistral
- Logique de conversation intelligente
- Système de progression pédagogique
- Analyse de code par IA

**Voir:** `TASKS_AI.md`

---

### Personne 2 - Backend/DevOps Engineer ⚙️
**Focus:** API, infrastructure, database, déploiement

**Tâches principales:**
- Backend FastAPI complet
- Database & ORM
- Docker & containerisation
- Authentication & rate limiting
- Tests & CI/CD

**Voir:** `TASKS_SERVER.md`

---

### Tâches Partagées 🤝
- Frontend Streamlit (selon affinités)
- Tests d'intégration
- Documentation
- Code review mutuel

**Voir:** `TASKS_FRONTEND.md`

---

## 🎯 SPRINT 1 - MVP Foundation (Semaine 1)

**Objectif:** Backend fonctionnel + Intégration IA basique + UI de base

### 🤖 IA/ML (Personne 1)
- [x] **JOUR 1-2:** Setup vLLM + Mistral-7B
  - Configuration du modèle
  - Tests d'inférence basiques
  - Paramètres optimaux (temperature, top-p, max tokens)

- [ ] **JOUR 2-3:** Système de prompts
  - Améliorer `backend/prompts.py`
  - Créer prompts spécialisés par langage (Python, JS, Java)
  - Tester différentes formulations
  - Few-shot learning avec exemples

- [ ] **JOUR 3-4:** Intégration dans service
  - Créer `backend/services/llm_service.py`
  - Streaming des réponses (SSE)
  - Gestion du contexte conversationnel (5 derniers messages)
  - Gestion des erreurs (timeout, overload)

- [ ] **JOUR 4-5:** Tests et validation
  - Tester avec différents codes
  - Validation de la qualité des réponses
  - Documentation des prompts

**Livrables:**
- ✅ vLLM opérationnel
- ✅ Prompts optimisés pour 3+ langages
- ✅ Service LLM avec streaming
- ✅ Documentation technique

---

### ⚙️ Backend/DevOps (Personne 2)
- [ ] **JOUR 1-2:** Architecture Backend
  - Créer structure complète (voir `TASKS_SERVER.md`)
  - `backend/main.py` - FastAPI app
  - `backend/core/config.py` - Configuration
  - `backend/api/routes/` - Routes de base
  - Setup SQLAlchemy + models

- [ ] **JOUR 2-3:** Database & CRUD
  - Models: Sessions, Conversations, UsageLogs
  - CRUD operations
  - Migrations Alembic
  - Scripts d'initialisation

- [ ] **JOUR 3-4:** API Endpoints
  - POST `/api/review` avec validation Pydantic
  - GET `/health` avec checks complets
  - Middleware logging et error handling
  - Tests avec httpx/pytest

- [ ] **JOUR 4-5:** Docker & Déploiement
  - Dockerfile.backend
  - Dockerfile.frontend
  - docker-compose.yml complet
  - Scripts de démarrage
  - Tests d'intégration Docker

**Livrables:**
- ✅ Backend FastAPI complet et testé
- ✅ Database SQLite opérationnelle
- ✅ Endpoints API documentés (Swagger)
- ✅ Docker Compose fonctionnel
- ✅ Tests basiques passants

---

### 🎨 Frontend (Partagé - 1-2 jours)
- [ ] **Amélioration UI basique**
  - Meilleur affichage du streaming
  - Syntax highlighting pour code
  - Bouton "Copy code"
  - Messages d'erreur clairs

**Responsable:** Selon affinité (IA ou Backend)

---

## 🚀 SPRINT 2 - Robustesse & Features (Semaine 2)

**Objectif:** Features avancées + Production-ready

### 🤖 IA/ML (Personne 1)
- [ ] **JOUR 1-2:** Contexte conversationnel intelligent
  - Créer `backend/ai/conversation_memory.py`
  - Tracking des concepts expliqués
  - Détection du niveau de l'étudiant
  - Résumé intelligent de conversation

- [ ] **JOUR 2-3:** Analyse de code avancée
  - Créer `backend/ai/code_analyzer.py`
  - Détection automatique de complexité
  - Identification de patterns
  - Suggestions de refactoring

- [ ] **JOUR 3-4:** Système de progression
  - Créer `backend/ai/skill_tracker.py`
  - Modèle de compétences par langage
  - Tracking de progression
  - Recommandations personnalisées

- [ ] **JOUR 4-5:** Fine-tuning & optimisation
  - Optimisation des prompts basée sur usage réel
  - Réduction de latence
  - Amélioration de la qualité pédagogique
  - Documentation des learnings

**Livrables:**
- ✅ Mémoire conversationnelle fonctionnelle
- ✅ Analyse de code intelligente
- ✅ Système de progression basique
- ✅ Métriques de qualité IA

---

### ⚙️ Backend/DevOps (Personne 2)
- [ ] **JOUR 1-2:** Authentication & Security
  - Session-based auth
  - Middleware d'authentification
  - Rate limiting (Redis ou in-memory)
  - CORS et security headers

- [ ] **JOUR 2-3:** Monitoring & Logging
  - Logging structuré (JSON)
  - Middleware de logging
  - Health check avancé
  - Métriques (optionnel: Prometheus)

- [ ] **JOUR 3-4:** Tests complets
  - Tests unitaires (80%+ coverage)
  - Tests d'intégration
  - Tests de charge (locust)
  - CI/CD GitHub Actions

- [ ] **JOUR 4-5:** Scripts GDPR & Admin
  - Scripts d'export/delete/anonymize
  - Documentation API complète
  - Admin endpoints (optionnel)

**Livrables:**
- ✅ Auth + rate limiting opérationnels
- ✅ Logging production-ready
- ✅ Tests coverage > 80%
- ✅ CI/CD pipeline
- ✅ Scripts GDPR

---

### 🎨 Frontend (Partagé - 2-3 jours)
- [ ] **Dashboard amélioré**
  - Statistiques enrichies
  - Graphiques Plotly
  - Badges de progression

- [ ] **Historique avancé**
  - Recherche full-text
  - Filtres multiples
  - Export Markdown

**Responsable:** À définir selon charge

---

## 🎨 SPRINT 3 - Polish & Demo (Semaine 3)

**Objectif:** Production-ready + Documentation + Démo

### 🤖 IA/ML (Personne 1)
- [ ] **JOUR 1-2:** Génération d'exemples
  - Créer `backend/ai/example_generator.py`
  - Génération d'exemples de code
  - Génération de contre-exemples
  - Exercices interactifs

- [ ] **JOUR 2-3:** Amélioration continue
  - A/B testing de prompts
  - Optimisation based on feedback
  - Documentation des best practices
  - Guide de prompt engineering

- [ ] **JOUR 3-4:** Support multi-langues
  - Détection de langue utilisateur
  - Prompts FR/EN
  - Tests bilingues

- [ ] **JOUR 4-5:** Préparation démo
  - Scénarios de démo
  - Dataset d'exemples impressionnants
  - Documentation des capacités IA
  - Métriques et benchmarks

**Livrables:**
- ✅ Features IA avancées
- ✅ Documentation complète IA
- ✅ Démo impressionnante
- ✅ Metrics & benchmarks

---

### ⚙️ Backend/DevOps (Personne 2)
- [ ] **JOUR 1-2:** Optimisations performance
  - Database indexes
  - Query optimization
  - Caching stratégique
  - Load testing

- [ ] **JOUR 2-3:** Documentation complète
  - API documentation (Swagger enrichi)
  - README technique
  - Architecture diagrams
  - Deployment guide

- [ ] **JOUR 3-4:** Déploiement production
  - PostgreSQL pour prod (optionnel)
  - Docker optimisé
  - SSL/HTTPS
  - Monitoring setup

- [ ] **JOUR 4-5:** Final polish
  - Code cleanup
  - Refactoring
  - Security audit
  - Performance tuning

**Livrables:**
- ✅ Backend optimisé
- ✅ Documentation complète
- ✅ Déploiement production-ready
- ✅ Code quality impeccable

---

### 🎨 Frontend (Partagé - 2-3 jours)
- [ ] **UI Polish**
  - Dark mode
  - Animations
  - Responsive design
  - Accessibility (A11y)

- [ ] **Mode exercices**
  - Quiz interactifs
  - Challenges de code
  - Sandbox d'exécution

**Responsable:** À définir

---

## 📊 SPRINT 4 - Refinement (Semaine 4 - Optionnel)

**Objectif:** Fine-tuning, features bonus, préparation postulation

### Tous ensemble
- [ ] Testing complet end-to-end
- [ ] Bug fixes
- [ ] Performance optimization
- [ ] Documentation finale
- [ ] Vidéo de démo
- [ ] Présentation projet (slides)

---

## 📋 Checklist Final (Production Ready)

### Backend ⚙️
- [ ] FastAPI avec tous les endpoints
- [ ] Database (SQLite/PostgreSQL) avec migrations
- [ ] Authentication & sessions
- [ ] Rate limiting
- [ ] Logging structuré
- [ ] Tests > 80% coverage
- [ ] CI/CD pipeline
- [ ] Docker & docker-compose
- [ ] Documentation API (Swagger)
- [ ] Scripts GDPR

### IA/ML 🤖
- [ ] vLLM + Mistral opérationnel
- [ ] Prompts optimisés multi-langages
- [ ] Streaming SSE fonctionnel
- [ ] Mémoire conversationnelle
- [ ] Analyse de code intelligente
- [ ] Système de progression
- [ ] Documentation prompts
- [ ] Métriques de qualité

### Frontend 🎨
- [ ] Chat interface clean
- [ ] Syntax highlighting
- [ ] Dashboard avec stats
- [ ] Historique avec recherche
- [ ] Dark mode
- [ ] Responsive design
- [ ] UX polie

### Général 📚
- [ ] README impressionnant
- [ ] CLAUDE.md à jour
- [ ] Architecture diagrams
- [ ] Vidéo de démo (2-3 min)
- [ ] Code clean et commenté
- [ ] Type hints partout (mypy 100%)
- [ ] Zero warnings (flake8)

---

## 🎯 Livrables Finaux pour Postulation

### 1. Repository GitHub 📦
- Code source complet et clean
- README avec GIFs/screenshots
- Documentation technique
- Architecture diagrams
- Badges (build, coverage, license)

### 2. Démo Live 🌐
- Application déployée (Railway, Render, DigitalOcean)
- URL publique accessible
- Performance optimale

### 3. Vidéo de Démo 🎥
- 2-3 minutes
- Montrer les features clés
- Focus sur l'IA et la pédagogie
- Qualité professionnelle

### 4. Documentation 📚
- Guide d'utilisation
- Documentation technique
- API documentation
- Deployment guide

### 5. Présentation 📊
- Slides PowerPoint/PDF
- Problème → Solution → Architecture → Résultats
- Métriques et benchmarks
- Learnings et future work

---

## 💡 Conseils pour un Rendu Clean

### Code Quality
- ✅ **Consistent:** Style uniforme (black, isort)
- ✅ **Typed:** Type hints partout (mypy)
- ✅ **Tested:** Coverage > 80%
- ✅ **Documented:** Docstrings clairs
- ✅ **Clean:** Pas de code mort, pas de TODOs

### Architecture
- ✅ **SOLID principles**
- ✅ **Separation of concerns**
- ✅ **DRY (Don't Repeat Yourself)**
- ✅ **Dependency injection**

### Git Hygiene
- ✅ **Commit messages clairs:** feat/fix/docs/refactor/test
- ✅ **Branches:** feature branches + PR reviews
- ✅ **No secrets:** .env dans .gitignore
- ✅ **Clean history:** Rebase si nécessaire

### Documentation
- ✅ **README avec:**
  - Description claire
  - Screenshots/GIFs
  - Quick start (3 étapes max)
  - Architecture overview
  - Tech stack
  - Contributing guide
- ✅ **Inline comments** pour logique complexe
- ✅ **API docs** auto-générées (Swagger)

---

## 📞 Coordination

### Daily Sync (15 min)
- **Quand:** Tous les jours (matin ou soir)
- **Format:** Quick standup
  - Ce qui a été fait hier
  - Ce qui sera fait aujourd'hui
  - Blockers éventuels

### Code Review
- **Process:** PR sur GitHub
- **Review mutuel:** Chacun review le code de l'autre
- **Merge:** Après validation + tests passants

### Communication
- **Slack/Discord:** Pour questions rapides
- **GitHub Issues:** Pour tracking des bugs/features
- **GitHub Projects:** Kanban board (To Do / In Progress / Done)

---

## 🎉 Milestones

- **Fin Semaine 1:** ✅ MVP fonctionnel (backend + IA + UI basique)
- **Fin Semaine 2:** ✅ Features avancées + Tests + GDPR
- **Fin Semaine 3:** ✅ Production-ready + Documentation
- **Fin Semaine 4:** ✅ Polish + Démo + Présentation

---

## 🚀 Go Live!

**Prêt pour postuler dans des boîtes d'IA!** 🎊

---

**Créé le:** 27 Octobre 2025
**Dernière mise à jour:** 27 Octobre 2025

---

## 📎 Références Utiles

### Documentation
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [vLLM Docs](https://docs.vllm.ai/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)

### Inspiration
- [OpenAI Playground](https://platform.openai.com/playground)
- [Claude.ai](https://claude.ai/)
- [GitHub Copilot](https://github.com/features/copilot)

### Deployment
- [Railway](https://railway.app/)
- [Render](https://render.com/)
- [DigitalOcean](https://www.digitalocean.com/)
