# ⚙️ TASKS SERVER - Backend & Infrastructure

Ce document liste toutes les tâches backend, serveur, DevOps et infrastructure pour le projet sensAI.

## 🎯 Objectif
Construire un backend robuste, scalable et production-ready avec des APIs performantes et une infrastructure fiable.

---

## 📋 BACKLOG - Priorité CRITIQUE (MVP)

### 1. 🚨 Implémentation du Backend FastAPI (MANQUANT!)
**Objectif:** Créer l'API REST complète pour le backend

**Tâches:**
- [ ] **Créer la structure backend complète**
  - `backend/main.py` - Application FastAPI principale
  - `backend/api/` - Routes et endpoints
  - `backend/models/` - Modèles SQLAlchemy
  - `backend/services/` - Business logic
  - `backend/schemas/` - Pydantic schemas (validation)
  - `backend/core/` - Configuration et settings
  - `backend/db/` - Database configuration

- [ ] **Endpoint `/api/review` (POST)**
  - Validation du payload (code, language, question)
  - Intégration avec vLLM
  - Streaming SSE (Server-Sent Events)
  - Gestion des erreurs

- [ ] **Endpoint `/health` (GET)**
  - Health check de l'API
  - Vérification du modèle vLLM
  - Status de la database

- [ ] **Intégration vLLM**
  - Configuration du modèle Mistral-7B-Instruct-v0.3
  - Gestion du context window (8192 tokens)
  - Optimisation de l'inférence
  - Batch processing si nécessaire

**Fichiers à créer:**
- `backend/main.py`
- `backend/api/routes/review.py`
- `backend/api/routes/health.py`
- `backend/services/llm_service.py`
- `backend/schemas/review.py`
- `backend/core/config.py`

**Status:** 🔴 **BLOQUANT - À faire en priorité #1**

---

### 2. 🗄️ Setup Database & ORM
**Objectif:** Mettre en place SQLite/PostgreSQL avec SQLAlchemy

**Tâches:**
- [ ] **Configuration SQLAlchemy**
  - Database URL configuration (SQLite pour dev, PostgreSQL pour prod)
  - Session management
  - Connection pooling

- [ ] **Créer les modèles de données**
  ```python
  # Users (pour future freemium)
  - id, username, email, created_at

  # Sessions
  - id, user_id, session_token, created_at, expires_at

  # Conversations
  - id, session_id, code, language, question, response, timestamp

  # UsageLogs (rate limiting)
  - id, session_id, endpoint, timestamp, tokens_used
  ```

- [ ] **Migrations Alembic**
  - Setup Alembic
  - Initial migration
  - Scripts de migration

- [ ] **Scripts CRUD de base**
  - Create/Read/Update/Delete pour chaque modèle
  - Queries optimisées

**Fichiers à créer:**
- `backend/db/session.py`
- `backend/db/base.py`
- `backend/models/user.py`
- `backend/models/session.py`
- `backend/models/conversation.py`
- `backend/models/usage_log.py`
- `backend/crud/` (CRUD operations)
- `alembic/` (migrations)

**Status:** 🔴 **BLOQUANT - À faire en priorité #2**

---

### 3. 🐳 Docker & Docker Compose Setup
**Objectif:** Containerisation complète de l'application

**Tâches:**
- [ ] **Dockerfile pour le backend FastAPI**
  - Base image Python 3.10+
  - Installation des dépendances
  - Configuration vLLM
  - CUDA support pour GPU
  - Multi-stage build pour optimisation

- [ ] **Dockerfile pour le frontend Streamlit**
  - Base image Python 3.10+
  - Installation des dépendances
  - Configuration du port 8501

- [ ] **Dockerfile pour vLLM (optionnel)**
  - Image optimisée pour l'inférence
  - Configuration GPU

- [ ] **docker-compose.yml complet**
  ```yaml
  services:
    backend:
      - FastAPI sur port 8000
      - Variables d'environnement
      - Volume pour la database

    frontend:
      - Streamlit sur port 8501
      - Dépend du backend

    vllm:
      - Modèle Mistral chargé
      - GPU passthrough
      - Health checks

    postgres (optionnel pour prod):
      - PostgreSQL 15
      - Persistent volume
  ```

- [ ] **Scripts de démarrage**
  - `docker-compose.yml` (production)
  - `docker-compose.dev.yml` (development avec hot reload)
  - `.dockerignore`
  - Health checks pour tous les services

**Fichiers à créer:**
- `Dockerfile.backend`
- `Dockerfile.frontend`
- `Dockerfile.vllm` (optionnel)
- `docker-compose.yml`
- `docker-compose.dev.yml`
- `.dockerignore`

**Status:** 🔴 **BLOQUANT - À faire en priorité #3**

---

## 📋 BACKLOG - Priorité Haute

### 4. 🔐 Authentication & Sessions
**Objectif:** Système d'authentification session-based

**Tâches:**
- [ ] Génération de session tokens
- [ ] Middleware d'authentification
- [ ] Cookie management (HttpOnly, Secure)
- [ ] Session expiration (TTL)
- [ ] Rate limiting par session

**Fichiers à créer:**
- `backend/core/security.py`
- `backend/middleware/auth.py`
- `backend/services/session_service.py`

---

### 5. ⚡ Rate Limiting & Quotas
**Objectif:** Protection contre l'abus et préparation freemium

**Tâches:**
- [ ] Implémentation rate limiting (Redis ou in-memory)
  - X requêtes par minute par session
  - X tokens par jour par user
- [ ] Middleware de rate limiting
- [ ] Endpoints pour vérifier les quotas
- [ ] Response headers avec quotas restants
- [ ] Système de quotas par tier (gratuit/premium)

**Fichiers à créer:**
- `backend/middleware/rate_limit.py`
- `backend/services/quota_service.py`

---

### 6. 📝 Logging & Monitoring
**Objectif:** Logs structurés et monitoring de production

**Tâches:**
- [ ] Configuration logging structuré (JSON)
  - Logs applicatifs
  - Logs d'accès
  - Logs d'erreurs
- [ ] Logging middleware
- [ ] Métriques Prometheus (optionnel)
  - Request duration
  - Request count
  - Error rate
  - Token usage
- [ ] Health check endpoint avancé
  - Database connectivity
  - vLLM status
  - Disk space
  - Memory usage

**Fichiers à créer:**
- `backend/core/logging.py`
- `backend/middleware/logging_middleware.py`
- `backend/api/routes/metrics.py`

---

### 7. 🛡️ Validation & Error Handling
**Objectif:** Validation robuste et gestion d'erreurs propre

**Tâches:**
- [ ] Pydantic schemas pour tous les endpoints
  - Request validation
  - Response serialization
- [ ] Custom exception handlers
  - ValidationError
  - DatabaseError
  - LLMError (timeout, overload)
- [ ] Error responses standardisés
  ```json
  {
    "error": "validation_error",
    "message": "Code field is required",
    "details": {...}
  }
  ```
- [ ] Sanitization des inputs (XSS, injection)

**Fichiers à créer:**
- `backend/schemas/` (tous les schemas)
- `backend/core/exceptions.py`
- `backend/middleware/error_handler.py`

---

## 📋 BACKLOG - Priorité Moyenne

### 8. 🧪 Tests Backend
**Objectif:** Couverture de tests complète

**Tâches:**
- [ ] Setup pytest et fixtures
- [ ] Tests unitaires
  - Services
  - CRUD operations
  - Utilities
- [ ] Tests d'intégration
  - Endpoints API
  - Database interactions
- [ ] Tests de charge (locust ou k6)
  - Performance du streaming
  - Concurrency handling
- [ ] CI/CD GitHub Actions
  - Lint (flake8, black, isort, mypy)
  - Tests automatiques
  - Coverage report

**Fichiers à créer:**
- `tests/unit/`
- `tests/integration/`
- `tests/load/`
- `.github/workflows/ci.yml`
- `conftest.py`

---

### 9. 📚 Documentation API
**Objectif:** Documentation interactive et complète

**Tâches:**
- [ ] OpenAPI/Swagger automatique (FastAPI)
- [ ] Descriptions détaillées des endpoints
- [ ] Exemples de requêtes/réponses
- [ ] Documentation des erreurs possibles
- [ ] Postman collection (optionnel)

**Fichiers à créer:**
- `backend/api/docs.py`
- `docs/api/`

---

### 10. 🔄 Asynchronous Task Queue
**Objectif:** Traitement asynchrone pour tâches longues

**Tâches:**
- [ ] Setup Celery + Redis (ou alternative)
- [ ] Background tasks pour analytics
- [ ] Export GDPR asynchrone
- [ ] Email notifications (future)
- [ ] Batch processing de conversations

**Fichiers à créer:**
- `backend/tasks/`
- `backend/core/celery_app.py`

---

## 📋 BACKLOG - Améliorations Futures

### 11. 🌐 CORS & Security Headers
**Tâches:**
- [ ] Configuration CORS appropriée
- [ ] Security headers (HSTS, CSP, X-Frame-Options)
- [ ] HTTPS enforcement en production

---

### 12. 💾 Caching Strategy
**Tâches:**
- [ ] Redis pour session storage
- [ ] Cache des réponses fréquentes (optionnel)
- [ ] Cache des prompts templates

---

### 13. 📊 Admin Dashboard API
**Tâches:**
- [ ] Endpoints admin (protégés)
- [ ] Statistiques d'usage
- [ ] Management des users
- [ ] Logs viewer

---

### 14. 🔐 GDPR Compliance (Scripts)
**Tâches:**
- [ ] Script d'export de données utilisateur
- [ ] Script de suppression de données
- [ ] Script d'anonymisation
- [ ] Audit logs

**Fichiers à créer:**
- `backend/scripts/gdpr_export.py`
- `backend/scripts/gdpr_delete.py`
- `backend/scripts/gdpr_anonymize.py`

---

### 15. 🚀 Performance Optimization
**Tâches:**
- [ ] Database indexes optimisés
- [ ] Query optimization
- [ ] Connection pooling tuning
- [ ] Lazy loading
- [ ] Response compression (gzip)

---

### 16. 🔄 WebSocket Support (Optionnel)
**Tâches:**
- [ ] WebSocket endpoint pour chat temps réel
- [ ] Alternative au SSE pour meilleure UX
- [ ] Reconnection automatique

---

## 📝 Architecture Backend Cible

```
backend/
├── main.py                 # FastAPI app entry point
├── api/
│   ├── routes/
│   │   ├── review.py       # Code review endpoint
│   │   ├── health.py       # Health check
│   │   ├── sessions.py     # Session management
│   │   └── admin.py        # Admin endpoints
│   └── dependencies.py     # Shared dependencies
├── core/
│   ├── config.py           # Configuration (env vars)
│   ├── security.py         # Auth & security
│   ├── logging.py          # Logging setup
│   └── exceptions.py       # Custom exceptions
├── db/
│   ├── session.py          # Database session
│   └── base.py             # Base model
├── models/                 # SQLAlchemy models
│   ├── user.py
│   ├── session.py
│   ├── conversation.py
│   └── usage_log.py
├── schemas/                # Pydantic schemas
│   ├── review.py
│   ├── session.py
│   └── conversation.py
├── services/               # Business logic
│   ├── llm_service.py      # vLLM integration
│   ├── session_service.py
│   ├── conversation_service.py
│   └── quota_service.py
├── crud/                   # CRUD operations
│   ├── user.py
│   ├── conversation.py
│   └── usage_log.py
├── middleware/
│   ├── auth.py
│   ├── rate_limit.py
│   ├── logging_middleware.py
│   └── error_handler.py
├── scripts/
│   ├── init_db.py
│   ├── gdpr_export.py
│   ├── gdpr_delete.py
│   └── gdpr_anonymize.py
└── prompts.py              # Prompt templates (existing)
```

---

## 🔧 Stack Technique

### Backend Core
- **FastAPI** - Framework web async
- **uvicorn** - ASGI server
- **pydantic** - Validation & serialization
- **python-multipart** - File uploads

### Database
- **SQLAlchemy** - ORM
- **alembic** - Migrations
- **SQLite** - Dev database
- **PostgreSQL** - Production database (optionnel)

### AI/ML
- **vLLM** - Inférence optimisée
- **langchain** - Prompt management

### Async & Tasks
- **Celery** - Task queue (optionnel)
- **Redis** - Cache & message broker (optionnel)

### Testing
- **pytest** - Test framework
- **pytest-asyncio** - Async tests
- **httpx** - HTTP client pour tests

### Dev Tools
- **black** - Code formatter
- **isort** - Import sorter
- **flake8** - Linter
- **mypy** - Type checker

---

## 📊 Priorités Recommandées

### Sprint 1 (MVP - 1 semaine)
1. ✅ Backend FastAPI complet (`main.py`, routes, vLLM)
2. ✅ Docker & docker-compose
3. ✅ Database setup (SQLite pour commencer)
4. ✅ Tests basiques

### Sprint 2 (Robustesse - 3-5 jours)
1. Authentification & sessions
2. Rate limiting
3. Logging & monitoring
4. Error handling avancé

### Sprint 3 (Production Ready - 3-5 jours)
1. Tests complets (unit + integration)
2. Documentation API
3. GDPR scripts
4. CI/CD pipeline

---

## 🎯 Métriques de Succès

### Performance
- **Latence API:** < 100ms (hors LLM)
- **Time to first token (TTFT):** < 500ms
- **Throughput:** 10+ req/sec par worker
- **Uptime:** 99.9%

### Code Quality
- **Test coverage:** > 80%
- **Type coverage (mypy):** 100%
- **Linting:** 0 erreurs flake8

### Scalabilité
- Support 100+ utilisateurs concurrents
- Horizontal scaling possible
- Database connection pool optimisé

---

**Dernière mise à jour:** 27 Octobre 2025
