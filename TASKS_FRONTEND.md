# 🎨 TASKS FRONTEND - UI/UX & Streamlit

Ce document liste toutes les tâches frontend, UI/UX et améliorations Streamlit pour le projet sensAI.

## 🎯 Objectif
Créer une interface utilisateur moderne, intuitive et engageante pour l'apprentissage du code avec le sensei IA.

---

## 📋 BACKLOG - Priorité Haute

### 1. 🎨 Amélioration de l'Interface Chat
**Objectif:** UX optimale pour les conversations avec le sensei

**Tâches:**
- [ ] **Streaming en temps réel amélioré**
  - Affichage token par token (comme ChatGPT)
  - Animation de typing indicator
  - Smooth scrolling automatique

- [ ] **Markdown enrichi**
  - Syntax highlighting pour code blocks
  - Support des tableaux
  - Support des listes à puces/numérotées
  - Emojis et formatting

- [ ] **Code snippets interactifs**
  - Bouton "Copy to clipboard"
  - Numéros de ligne
  - Highlight des différences (avant/après)

- [ ] **Réactions et feedback**
  - Système de like/dislike par message
  - Feedback détaillé (formulaire)
  - Sauvegarde des feedbacks pour améliorer l'IA

- [ ] **Citations et références**
  - Relier les réponses aux questions précédentes
  - Visualiser le contexte d'une réponse

**Fichiers concernés:**
- `frontend/app.py`
- `frontend/components/ui.py`
- Nouveau: `frontend/components/chat_message.py`
- Nouveau: `frontend/components/code_block.py`

---

### 2. 📝 Éditeur de Code Intégré
**Objectif:** Meilleure expérience pour entrer et éditer du code

**Tâches:**
- [ ] **Code editor avec syntax highlighting**
  - Utiliser `streamlit-ace` ou composant custom
  - Support multi-langages
  - Auto-indentation
  - Line numbers

- [ ] **Features avancées**
  - Auto-completion basique
  - Bracket matching
  - Themes (dark/light)
  - Font size adjustable

- [ ] **Templates de code**
  - Snippets pré-remplis par langage
  - Exemples quick-start
  - Load/Save de fichiers locaux

- [ ] **Split view**
  - Vue côte à côte: code original vs code amélioré
  - Diff highlighting

**Fichiers concernés:**
- `frontend/components/code_input.py`
- Nouveau: `frontend/components/code_editor.py`

---

### 3. 🎯 Dashboard Amélioré
**Objectif:** Visualisation de progression claire et motivante

**Tâches:**
- [ ] **Statistiques enrichies**
  - Graphiques interactifs (Plotly)
  - Évolution temporelle (progression dans le temps)
  - Heatmap d'activité (style GitHub)
  - Comparaison avec moyennes

- [ ] **Compétences et badges**
  - Visualisation des compétences acquises
  - Système de badges/achievements
  - Progression par langage
  - Niveau estimé (débutant/intermédiaire/avancé)

- [ ] **Insights personnalisés**
  - Points forts détectés
  - Axes d'amélioration
  - Recommandations de sujets à étudier

- [ ] **Objectifs et challenges**
  - Définir des objectifs d'apprentissage
  - Suivre la complétion
  - Suggestions de challenges

**Fichiers concernés:**
- `frontend/pages/dashboard.py`
- Nouveau: `frontend/components/charts.py`
- Nouveau: `frontend/components/badges.py`

---

### 4. 📚 Historique et Recherche
**Objectif:** Retrouver facilement les conversations passées

**Tâches:**
- [ ] **Recherche avancée**
  - Full-text search dans les conversations
  - Filtres multiples (date, langage, tags)
  - Recherche par concepts (ex: "boucles", "POO")

- [ ] **Organisation**
  - Créer des collections/dossiers
  - Tagger les conversations
  - Favoris/bookmarks

- [ ] **Export et partage**
  - Export en Markdown
  - Export en PDF
  - Partage de conversation (lien unique)

- [ ] **Timeline visuelle**
  - Vue chronologique des apprentissages
  - Filtrer par période

**Fichiers concernés:**
- `frontend/pages/history.py`
- Nouveau: `frontend/components/search.py`
- Nouveau: `frontend/utils/export.py`

---

### 5. 🎨 Thème et Design System
**Objectif:** Interface moderne et cohérente

**Tâches:**
- [ ] **Design system complet**
  - Palette de couleurs définie
  - Typographie cohérente
  - Spacing system
  - Components library

- [ ] **Dark/Light mode**
  - Toggle theme
  - Sauvegarde de préférence
  - Transition smooth

- [ ] **Responsive design**
  - Adaptation mobile/tablet
  - Touch-friendly sur mobile

- [ ] **Animations et transitions**
  - Micro-interactions
  - Loading states agréables
  - Page transitions

**Fichiers concernés:**
- `frontend/components/ui.py`
- Nouveau: `frontend/styles/theme.py`
- Nouveau: `frontend/styles/animations.py`

---

## 📋 BACKLOG - Priorité Moyenne

### 6. 🎮 Mode Interactif et Exercices
**Objectif:** Apprendre en pratiquant directement dans l'interface

**Tâches:**
- [ ] **Mode "Quiz"**
  - Questions générées par l'IA
  - Validation automatique des réponses
  - Score et progression

- [ ] **Mode "Debug Challenge"**
  - Code avec bugs à trouver
  - Hints progressifs
  - Solution guidée étape par étape

- [ ] **Mode "Code Golf"**
  - Optimiser un code (moins de lignes, meilleur perf)
  - Comparaison avec autres solutions

- [ ] **Sandbox interactif**
  - Exécution de code in-browser (Python, JS)
  - Voir le résultat en temps réel
  - Tests automatiques

**Fichiers à créer:**
- `frontend/pages/exercises.py`
- `frontend/components/quiz.py`
- `frontend/components/sandbox.py`

---

### 7. 👥 Fonctionnalités Sociales (Future)
**Objectif:** Communauté et collaboration

**Tâches:**
- [ ] **Profil utilisateur**
  - Avatar
  - Bio
  - Statistiques publiques

- [ ] **Partage de code**
  - Publier ses solutions
  - Commenter les solutions d'autres

- [ ] **Leaderboard**
  - Classement par activité
  - Classement par progression

- [ ] **Mentorship**
  - Connecter étudiants avancés avec débutants

**Fichiers à créer:**
- `frontend/pages/profile.py`
- `frontend/pages/community.py`

---

### 8. 📱 Progressive Web App (PWA)
**Objectif:** Utilisation offline et installation

**Tâches:**
- [ ] Service Worker pour cache
- [ ] Manifest.json
- [ ] Icônes PWA
- [ ] Offline fallback
- [ ] Installation prompt

---

### 9. ♿ Accessibilité (A11y)
**Objectif:** Accessible à tous

**Tâches:**
- [ ] ARIA labels
- [ ] Keyboard navigation
- [ ] Screen reader support
- [ ] Contrast ratios WCAG AA
- [ ] Focus indicators

---

### 10. 🌍 Internationalisation (i18n)
**Objectif:** Support multi-langues

**Tâches:**
- [ ] Français/Anglais pour l'UI
- [ ] Détection automatique de langue
- [ ] Fichiers de traduction
- [ ] Switch de langue

**Fichiers à créer:**
- `frontend/locales/fr.json`
- `frontend/locales/en.json`
- `frontend/utils/i18n.py`

---

## 📋 BACKLOG - Améliorations Futures

### 11. 🎥 Tutoriels Intégrés
**Tâches:**
- [ ] Onboarding interactif (première utilisation)
- [ ] Tooltips contextuels
- [ ] Vidéos explicatives
- [ ] Documentation in-app

---

### 12. 🔔 Notifications et Rappels
**Tâches:**
- [ ] Notifications de progression
- [ ] Rappels d'apprentissage quotidien
- [ ] Célébration de milestones

---

### 13. 📊 Analytics UI
**Tâches:**
- [ ] Tracking des interactions utilisateur
- [ ] Heatmaps de clics
- [ ] Funnels de conversion
- [ ] A/B testing infrastructure

---

### 14. 🎨 Customisation de l'Interface
**Tâches:**
- [ ] Personnalisation de l'avatar du sensei
- [ ] Choix de theme colors
- [ ] Layout preferences
- [ ] Font size ajustable

---

### 15. 🚀 Performance Frontend
**Tâches:**
- [ ] Lazy loading des composants lourds
- [ ] Image optimization
- [ ] Code splitting
- [ ] Caching stratégique
- [ ] Minification

---

## 📝 Structure Frontend Cible

```
frontend/
├── app.py                      # Main Streamlit app (existing)
├── pages/
│   ├── dashboard.py            # Dashboard amélioré
│   ├── history.py              # Historique avec recherche
│   ├── exercises.py            # Mode exercices interactifs
│   ├── profile.py              # Profil utilisateur (future)
│   └── settings.py             # Paramètres
├── components/
│   ├── ui.py                   # Composants UI génériques (existing)
│   ├── code_input.py           # Sélecteur de langage (existing)
│   ├── code_editor.py          # Éditeur de code avancé
│   ├── code_block.py           # Affichage de code enrichi
│   ├── chat_message.py         # Message de chat stylisé
│   ├── charts.py               # Graphiques Plotly
│   ├── badges.py               # Système de badges
│   ├── search.py               # Composant de recherche
│   ├── quiz.py                 # Composant quiz interactif
│   └── sandbox.py              # Sandbox d'exécution
├── services/
│   ├── api_client.py           # Client API (existing)
│   └── storage_client.py       # Local/Session storage
├── utils/
│   ├── helpers.py              # Helpers généraux (existing)
│   ├── export.py               # Export Markdown/PDF
│   ├── i18n.py                 # Internationalisation
│   └── analytics.py            # Analytics tracking
├── styles/
│   ├── theme.py                # Design system
│   ├── animations.py           # CSS animations
│   └── custom.css              # CSS custom
├── locales/
│   ├── en.json                 # Traductions anglais
│   └── fr.json                 # Traductions français
└── assets/
    ├── images/
    ├── icons/
    └── fonts/
```

---

## 🎨 Design Guidelines

### Couleurs Principales
- **Primary:** `#667eea` (Bleu/Violet)
- **Secondary:** `#764ba2` (Violet foncé)
- **Success:** `#10b981` (Vert)
- **Warning:** `#f59e0b` (Orange)
- **Error:** `#ef4444` (Rouge)
- **Text:** `#1f2937` (Gris foncé)
- **Background:** `#ffffff` (Blanc) / `#0f172a` (Dark mode)

### Typographie
- **Headings:** Inter, Poppins ou Montserrat
- **Body:** System fonts (optimal performance)
- **Code:** JetBrains Mono, Fira Code

### Spacing Scale
- `xs`: 0.25rem (4px)
- `sm`: 0.5rem (8px)
- `md`: 1rem (16px)
- `lg`: 1.5rem (24px)
- `xl`: 2rem (32px)
- `2xl`: 3rem (48px)

### Border Radius
- `sm`: 4px
- `md`: 8px
- `lg`: 12px
- `xl`: 16px

---

## 🎯 Priorités Recommandées

### Phase 1 - Core UX (1 semaine)
1. ✅ Amélioration du chat (streaming, markdown, code blocks)
2. ✅ Éditeur de code avec syntax highlighting
3. ✅ Système de feedback sur les messages
4. ✅ Design system et thème cohérent

### Phase 2 - Engagement (3-5 jours)
1. Dashboard enrichi avec graphiques
2. Historique avec recherche avancée
3. Mode exercices interactifs
4. Badges et gamification

### Phase 3 - Polish (3-5 jours)
1. Dark mode
2. Responsive design
3. Animations et micro-interactions
4. Accessibilité (A11y)

---

## 🎯 Métriques de Succès

### Performance
- **First Contentful Paint (FCP):** < 1.5s
- **Time to Interactive (TTI):** < 3s
- **Cumulative Layout Shift (CLS):** < 0.1

### UX
- **Navigation intuitive:** 90%+ utilisateurs trouvent les features sans aide
- **Temps moyen de session:** > 10 minutes
- **Taux de rétention:** > 60% (retour après première utilisation)

### Accessibilité
- **WCAG AA compliance:** 100%
- **Lighthouse Accessibility Score:** > 90

---

## 🔧 Stack Technique Frontend

### Core
- **Streamlit** - Framework principal
- **htbuilder** - HTML/CSS custom (existing)

### Visualisation
- **Plotly** - Graphiques interactifs
- **Altair** - Charts déclaratifs (alternative)

### Code Editor
- **streamlit-ace** - Ace editor intégré
- **streamlit-monaco** - Monaco editor (VS Code)

### Styling
- **CSS custom** via `st.markdown(..., unsafe_allow_html=True)`
- **CSS-in-Python** via htbuilder

### Utils
- **pandas** - Manipulation de données pour viz
- **Pillow** - Traitement d'images
- **python-markdown** - Markdown processing

---

## 📚 Références et Inspiration

### Design
- [Dribbble - Educational Apps](https://dribbble.com/tags/educational-app)
- [Behance - Learning Platforms](https://www.behance.net/search/projects?search=learning%20platform)

### Streamlit
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Components](https://streamlit.io/components)

### Code Editors
- [Monaco Editor](https://microsoft.github.io/monaco-editor/)
- [Ace Editor](https://ace.c9.io/)

---

**Dernière mise à jour:** 27 Octobre 2025
