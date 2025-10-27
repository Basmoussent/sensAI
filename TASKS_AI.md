# 🤖 TASKS AI - Tâches IA & Machine Learning

Ce document liste toutes les tâches liées à l'IA, au ML, et aux prompts pour le projet sensAI.

## 🎯 Objectif
Créer un sensei IA qui utilise la méthode socratique pour enseigner la programmation de manière pédagogique et intelligente.

---

## 📋 BACKLOG - Priorité Haute

### 1. ✅ Amélioration du Système de Prompts
**Objectif:** Optimiser les prompts pour obtenir des réponses plus pédagogiques et adaptées

**Tâches:**
- [ ] Créer des prompts spécialisés par langage de programmation
  - Templates pour Python (focus sur pythonic code)
  - Templates pour JavaScript/TypeScript (focus sur patterns modernes)
  - Templates pour Java, C++, Go, Rust
- [ ] Implémenter un système de prompts multi-niveaux
  - Détection automatique du niveau du student (débutant/intermédiaire/avancé)
  - Adaptation du ton et de la complexité des explications
  - Questions socratiques adaptées au niveau
- [ ] Ajouter des exemples de code dans les prompts
  - Bonnes pratiques par langage
  - Anti-patterns communs à éviter
- [ ] Créer un prompt pour l'analyse de performance (Big O, optimisation)
- [ ] Prompt pour la sécurité (injection, XSS, CSRF selon le langage)

**Fichiers concernés:**
- `backend/prompts.py`
- Nouveau: `backend/prompts/language_specific/`

---

### 2. 🧠 Implémentation du Contexte Conversationnel Intelligent
**Objectif:** Le sensei doit se souvenir du contexte et progresser pédagogiquement

**Tâches:**
- [ ] Créer un système de mémoire conversationnelle
  - Tracking des concepts déjà expliqués
  - Détection des patterns d'erreurs répétées
  - Mémorisation du niveau de compréhension du student
- [ ] Implémentation d'un résumé intelligent de conversation
  - Condensation des échanges précédents pour économiser tokens
  - Extraction des points clés pédagogiques
- [ ] Système de questions de suivi intelligentes
  - Générer des questions basées sur les réponses précédentes
  - Guider progressivement vers la solution
- [ ] Détection de frustration ou blocage
  - Adapter le style pédagogique si le student est bloqué
  - Proposer des indices plus directs si nécessaire

**Fichiers concernés:**
- Nouveau: `backend/ai/conversation_memory.py`
- Nouveau: `backend/ai/context_manager.py`
- `backend/prompts.py`

---

### 3. 🔍 Analyse de Code Avancée avec IA
**Objectif:** Enrichir l'analyse avec détection automatique de patterns et problèmes

**Tâches:**
- [ ] Détection automatique du niveau de code (complexité)
  - Analyse syntaxique basique
  - Identification de patterns avancés (design patterns, SOLID)
- [ ] Analyse de la qualité du code
  - Détection de code smells
  - Suggestions de refactoring
  - Évaluation de la lisibilité
- [ ] Détection de bugs courants
  - Erreurs logiques fréquentes
  - Edge cases non gérés
  - Memory leaks ou problèmes de performance
- [ ] Génération de tests suggérés
  - Identifier les cas de test manquants
  - Proposer des scénarios de test

**Fichiers concernés:**
- Nouveau: `backend/ai/code_analyzer.py`
- Nouveau: `backend/ai/pattern_detector.py`

---

### 4. 🎓 Système de Progression Pédagogique
**Objectif:** Suivre la progression de l'étudiant et adapter l'enseignement

**Tâches:**
- [ ] Créer un modèle de compétences par langage
  - Syntaxe de base
  - Structures de contrôle
  - POO / Functional Programming
  - Patterns avancés
  - Performance et optimisation
- [ ] Système de tracking de progression
  - Quelles compétences ont été travaillées
  - Quels concepts ont été compris
  - Quels points restent à améliorer
- [ ] Recommandations intelligentes d'exercices
  - Suggérer des challenges adaptés au niveau
  - Progression graduelle de difficulté
- [ ] Génération de rapports de progression
  - Points forts identifiés
  - Axes d'amélioration
  - Prochaines étapes suggérées

**Fichiers concernés:**
- Nouveau: `backend/ai/skill_tracker.py`
- Nouveau: `backend/ai/recommendation_engine.py`
- Nouveau: `backend/models/student_progress.py`

---

## 📋 BACKLOG - Priorité Moyenne

### 5. 🎯 Fine-tuning du Modèle Mistral
**Objectif:** Adapter le modèle spécifiquement pour l'enseignement du code

**Tâches:**
- [ ] Créer un dataset d'entraînement
  - Collecter des exemples de code avec review pédagogique
  - Annoter avec niveau de difficulté
  - Inclure des dialogues socratiques de qualité
- [ ] Préparer l'infrastructure de fine-tuning
  - Setup environnement de training
  - Scripts de preprocessing des données
- [ ] Expérimenter avec différents hyperparamètres
  - Learning rate
  - Nombre d'epochs
  - Batch size
- [ ] Évaluation du modèle fine-tuné
  - Métriques de qualité pédagogique
  - Comparaison avec modèle de base
- [ ] Déploiement du modèle amélioré

**Fichiers concernés:**
- Nouveau: `backend/ai/training/`
- Nouveau: `backend/ai/evaluation/`

---

### 6. 💬 Génération d'Exemples et Contre-exemples
**Objectif:** Le sensei génère automatiquement des exemples pour illustrer

**Tâches:**
- [ ] Génération d'exemples de code corrects
  - À partir d'un concept expliqué
  - Différents niveaux de complexité
- [ ] Génération de contre-exemples (anti-patterns)
  - Montrer ce qu'il ne faut pas faire
  - Expliquer pourquoi c'est problématique
- [ ] Génération de variations d'un même code
  - Différentes approches pour résoudre le même problème
  - Comparaison des avantages/inconvénients
- [ ] Création d'exercices interactifs
  - "Trouve l'erreur dans ce code"
  - "Améliore ce code"

**Fichiers concernés:**
- Nouveau: `backend/ai/code_generator.py`
- Nouveau: `backend/ai/example_generator.py`

---

### 7. 🌍 Support Multi-langues (Langue naturelle)
**Objectif:** Support français/anglais pour les explications

**Tâches:**
- [ ] Détection automatique de la langue de l'utilisateur
- [ ] Adaptation des prompts système en français
- [ ] Génération de réponses bilingues
- [ ] Support de l'alternance code-switching (franglais technique)

**Fichiers concernés:**
- `backend/prompts.py`
- Nouveau: `backend/ai/language_detector.py`

---

## 📋 BACKLOG - Améliorations Futures

### 8. 🤝 Système de Comparaison de Code
**Objectif:** Comparer différentes solutions à un même problème

**Tâches:**
- [ ] Analyse comparative de plusieurs solutions
- [ ] Évaluation automatique (lisibilité, performance, maintenabilité)
- [ ] Génération de recommandations contextuelles

---

### 9. 📊 Analytics IA sur les Patterns d'Apprentissage
**Objectif:** Identifier les difficultés communes des étudiants

**Tâches:**
- [ ] Clustering des erreurs fréquentes par langage
- [ ] Identification de patterns d'apprentissage
- [ ] Génération de contenus pédagogiques ciblés

---

### 10. 🎮 Gamification avec IA
**Objectif:** Rendre l'apprentissage plus engageant

**Tâches:**
- [ ] Système de défis générés par IA
- [ ] Adaptation dynamique de la difficulté
- [ ] Recommandations personnalisées de parcours

---

## 📝 Notes Techniques

### Configuration Mistral-7B-Instruct-v0.3
- **Modèle actuel:** `mistralai/Mistral-7B-Instruct-v0.3`
- **Framework:** vLLM pour l'inférence
- **Context window:** 8192 tokens
- **Température recommandée:** 0.7-0.8 (balance créativité/précision)
- **Top-p:** 0.9
- **Max tokens:** 2048 pour les réponses

### Best Practices Prompting
1. **Structure claire:** Instructions → Contexte → Question → Format attendu
2. **Few-shot learning:** Inclure 2-3 exemples dans les prompts critiques
3. **Chain of thought:** Demander au modèle d'expliquer son raisonnement
4. **Constraints explicites:** Définir clairement le style pédagogique attendu

### Métriques de Qualité à Suivre
- **Pertinence pédagogique:** Les explications aident-elles vraiment ?
- **Qualité socratique:** Les questions guident-elles vers la solution ?
- **Adaptation au niveau:** Le ton est-il approprié ?
- **Complétude:** Tous les aspects du code sont-ils couverts ?
- **Clarté:** Les explications sont-elles compréhensibles ?

---

## 🔗 Liens et Ressources

- [Mistral AI Documentation](https://docs.mistral.ai/)
- [vLLM Documentation](https://docs.vllm.ai/)
- [LangChain Prompting Guide](https://python.langchain.com/docs/modules/model_io/prompts/)
- [Socratic Teaching Methods](https://en.wikipedia.org/wiki/Socratic_method)

---

**Dernière mise à jour:** 27 Octobre 2025
