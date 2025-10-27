# 🤖 TASKS AI - Tâches IA & Machine Learning

Ce document liste toutes les tâches liées à l'IA, au ML, et aux prompts pour le projet sensAI.

## 🎯 Objectif
Créer un sensei IA qui utilise la méthode socratique pour enseigner la programmation de manière pédagogique et intelligente.

---

## 📋 SPRINT 1 - MVP Enrichi (Semaine 1)

### ✅ JOUR 1-2: Setup API + Code Analyzer

#### 1.1 Setup API Mistral (au lieu de vLLM local)
**Pourquoi:** Pas besoin de 13GB de RAM, focus sur l'architecture IA

**Tâches:**
- [ ] Créer compte Mistral AI et obtenir API key
- [ ] Setup configuration avec variables d'environnement
- [ ] Créer `backend/services/llm_service.py` basique
- [ ] Tester connection et premiers appels API
- [ ] Documenter les paramètres (temperature, top_p, max_tokens)

**Fichiers à créer:**
```
backend/
├── services/
│   └── llm_service.py          # Service principal LLM
├── core/
│   └── config.py               # Configuration (API keys)
└── .env.example                # Template variables d'env
```

**Code exemple:**
```python
# backend/services/llm_service.py
from mistralai.client import MistralClient
import os

class LLMService:
    def __init__(self):
        self.client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))

    def generate_response(self, messages, temperature=0.7):
        response = self.client.chat(
            model="mistral-small-latest",
            messages=messages,
            temperature=temperature,
            max_tokens=2048
        )
        return response.choices[0].message.content
```

---

#### 1.2 Code Analyzer avec AST (Compétence: Static Analysis)
**Objectif:** Analyser le code AVANT d'envoyer au LLM pour enrichir le contexte

**Tâches:**
- [ ] Créer `backend/ai/code_analyzer.py`
- [ ] Implémenter analyse AST pour Python
- [ ] Détecter complexité cyclomatique
- [ ] Identifier code smells (fonctions trop longues, trop de params, etc.)
- [ ] Scanner pour problèmes de sécurité (eval, exec, etc.)
- [ ] Extraire métadonnées (fonctions, imports, classes)

**Fichiers à créer:**
```
backend/
└── ai/
    ├── __init__.py
    ├── code_analyzer.py         # Analyse AST
    └── complexity.py            # Calcul complexité
```

**Code exemple:**
```python
import ast
from typing import Dict, List

class CodeAnalyzer:
    def analyze_python(self, code: str) -> Dict:
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return {'syntax_error': str(e)}

        return {
            'complexity': self._calculate_complexity(tree),
            'functions': self._extract_functions(tree),
            'code_smells': self._detect_smells(tree),
            'security_issues': self._security_scan(tree),
        }
```

**Tests:**
- [ ] Tester avec code simple
- [ ] Tester avec code complexe
- [ ] Tester avec code buggé
- [ ] Documenter les patterns détectés

---

### ✅ JOUR 2-3: RAG System + Prompt Orchestrator

#### 2.1 RAG (Retrieval Augmented Generation)
**Objectif:** Récupérer des exemples similaires pour enrichir les prompts

**Tâches:**
- [ ] Setup SentenceTransformers pour embeddings
- [ ] Setup ChromaDB (ou FAISS) pour vector store
- [ ] Créer base d'exemples de code (bon/mauvais)
- [ ] Implémenter recherche sémantique
- [ ] Intégrer dans le service LLM

**Fichiers à créer:**
```
backend/
└── ai/
    ├── rag_system.py            # RAG principal
    ├── embeddings.py            # Gestion embeddings
    └── examples/
        ├── python_examples.json
        ├── javascript_examples.json
        └── common_mistakes.json
```

**Code exemple:**
```python
from sentence_transformers import SentenceTransformer
import chromadb

class RAGSystem:
    def __init__(self):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.db = chromadb.Client()
        self.collection = self.db.create_collection("code_examples")

    def add_example(self, code: str, explanation: str, tags: List[str]):
        embedding = self.embedder.encode(code)
        self.collection.add(
            embeddings=[embedding.tolist()],
            documents=[code],
            metadatas=[{"explanation": explanation, "tags": tags}]
        )

    def retrieve_similar(self, code: str, top_k: int = 3):
        embedding = self.embedder.encode(code)
        results = self.collection.query(
            query_embeddings=[embedding.tolist()],
            n_results=top_k
        )
        return results
```

---

#### 2.2 Prompt Orchestrator
**Objectif:** Composer intelligemment les prompts selon le contexte

**Tâches:**
- [ ] Utiliser les prompts existants de `backend/prompts/`
- [ ] Créer orchestrateur qui sélectionne les bons prompts
- [ ] Intégrer résultats du Code Analyzer
- [ ] Intégrer exemples du RAG
- [ ] Adapter selon niveau détecté de l'étudiant

**Fichiers à créer:**
```
backend/
└── services/
    └── prompt_orchestrator.py   # Orchestration intelligente
```

**Code exemple:**
```python
from backend.prompts import (
    SYSTEM_PROMPT, PYTHON_PROMPT,
    BEGINNER_FRIENDLY_PROMPT, ADVANCED_DEVELOPER_PROMPT
)

class PromptOrchestrator:
    def __init__(self, code_analyzer, rag_system):
        self.analyzer = code_analyzer
        self.rag = rag_system

    def build_review_prompt(self, code, language, student_level="intermediate"):
        # 1. Analyser le code
        analysis = self.analyzer.analyze_python(code)

        # 2. Récupérer exemples similaires
        examples = self.rag.retrieve_similar(code)

        # 3. Sélectionner les prompts appropriés
        system = SYSTEM_PROMPT
        if student_level == "beginner":
            system += "\n\n" + BEGINNER_FRIENDLY_PROMPT

        system += "\n\n" + PYTHON_PROMPT

        # 4. Composer le prompt enrichi
        user_prompt = f"""Code à reviewer:
```python
{code}
```

Analyse automatique détectée:
- Complexité: {analysis['complexity']}
- Code smells: {analysis['code_smells']}
- Issues de sécurité: {analysis['security_issues']}

Exemples similaires trouvés: {len(examples)} cas

En tant que sensei, guide l'étudiant avec la méthode socratique."""

        return system, user_prompt
```

---

### ✅ JOUR 3-4: Conversation Memory + Service Complet

#### 3.1 Conversation Memory
**Objectif:** Mémoriser le contexte de la conversation et la progression

**Tâches:**
- [ ] Créer système de mémoire court-terme (5 derniers messages)
- [ ] Créer système de mémoire long-terme (concepts expliqués)
- [ ] Profiler l'étudiant (niveau, erreurs récurrentes)
- [ ] Détecter patterns d'apprentissage

**Fichiers à créer:**
```
backend/
└── ai/
    ├── conversation_memory.py   # Mémoire conversationnelle
    └── student_profile.py       # Profil étudiant
```

**Code exemple:**
```python
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Message:
    role: str
    content: str
    timestamp: str

class ConversationMemory:
    def __init__(self):
        self.short_term: List[Message] = []  # 5 derniers
        self.long_term: Dict = {
            'explained_concepts': set(),
            'recurring_mistakes': [],
            'student_level': 'intermediate'
        }

    def add_message(self, role: str, content: str):
        msg = Message(role, content, datetime.now().isoformat())
        self.short_term.append(msg)

        # Garder seulement les 5 derniers
        if len(self.short_term) > 5:
            self.short_term.pop(0)

        # Extraire concepts et mettre à jour long-term
        self._update_long_term_memory(msg)

    def build_context_summary(self) -> str:
        """Résumé intelligent pour économiser tokens"""
        return f"""Contexte de la conversation:
- Niveau détecté: {self.long_term['student_level']}
- Concepts déjà expliqués: {', '.join(self.long_term['explained_concepts'])}
- Erreurs récurrentes: {len(self.long_term['recurring_mistakes'])}
"""
```

---

#### 3.2 LLM Service Complet avec Streaming
**Objectif:** Service final intégrant tous les composants

**Tâches:**
- [ ] Intégrer Code Analyzer, RAG, Memory, Orchestrator
- [ ] Implémenter streaming SSE (Server-Sent Events)
- [ ] Post-processing des réponses (markdown, highlighting)
- [ ] Gestion d'erreurs robuste
- [ ] Logging et monitoring

**Fichiers à créer:**
```
backend/
└── services/
    └── llm_service.py           # Service complet
```

**Code exemple:**
```python
from typing import AsyncGenerator
from mistralai.models.chat_completion import ChatMessage

class EnhancedLLMService:
    def __init__(self):
        self.client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))
        self.analyzer = CodeAnalyzer()
        self.rag = RAGSystem()
        self.orchestrator = PromptOrchestrator(self.analyzer, self.rag)
        self.memory = ConversationMemory()

    async def review_code_stream(
        self,
        code: str,
        language: str,
        student_id: str
    ) -> AsyncGenerator[str, None]:
        # 1. Construire prompt enrichi
        system_prompt, user_prompt = self.orchestrator.build_review_prompt(
            code, language, self.memory.long_term['student_level']
        )

        # 2. Ajouter contexte conversationnel
        context = self.memory.build_context_summary()

        # 3. Composer messages
        messages = [
            ChatMessage(role="system", content=system_prompt),
            ChatMessage(role="user", content=context + "\n" + user_prompt)
        ]

        # 4. Streaming
        response = self.client.chat_stream(
            model="mistral-small-latest",
            messages=messages,
            temperature=0.7
        )

        full_response = ""
        for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                full_response += delta
                yield delta

        # 5. Mettre à jour mémoire
        self.memory.add_message("user", user_prompt)
        self.memory.add_message("assistant", full_response)
```

---

### ✅ JOUR 4-5: Évaluation + Tests + Documentation

#### 4.1 Framework d'Évaluation de Prompts
**Objectif:** Mesurer et améliorer la qualité des réponses

**Tâches:**
- [ ] Créer dataset de test (codes + réponses attendues)
- [ ] Métriques de qualité (questions socratiques, précision, etc.)
- [ ] A/B testing de différents prompts
- [ ] Benchmarking des performances

**Fichiers à créer:**
```
backend/
└── ai/
    ├── prompt_evaluator.py      # Évaluation
    └── metrics.py               # Métriques personnalisées
```

**Code exemple:**
```python
class PromptEvaluator:
    def __init__(self):
        self.test_cases = self._load_test_cases()

    def evaluate_prompt(self, prompt_template) -> Dict:
        scores = []
        for test_case in self.test_cases:
            response = self.llm.generate(prompt_template.format(**test_case))

            score = {
                'has_questions': self._count_questions(response),
                'no_direct_solution': not self._contains_solution(response),
                'identifies_issue': self._checks_issue_found(response),
                'socratic_score': self._socratic_score(response)
            }
            scores.append(score)

        return self._aggregate_metrics(scores)
```

---

#### 4.2 Tests Unitaires
**Tâches:**
- [ ] Tests pour Code Analyzer
- [ ] Tests pour RAG System
- [ ] Tests pour Conversation Memory
- [ ] Tests d'intégration du service complet

**Fichiers à créer:**
```
tests/
├── test_code_analyzer.py
├── test_rag_system.py
├── test_conversation_memory.py
├── test_prompt_orchestrator.py
└── test_llm_service.py
```

---

#### 4.3 Documentation Technique
**Tâches:**
- [ ] README pour backend/ai/
- [ ] Documentation des prompts
- [ ] Guide d'utilisation du service
- [ ] Benchmarks et métriques
- [ ] Exemples d'utilisation

---

## 📦 LIVRABLES SPRINT 1

À la fin de la semaine 1, tu auras:

✅ **Code Analyzer** avec AST (analyse statique)
✅ **RAG System** avec embeddings et vector search
✅ **Conversation Memory** avec profiling étudiant
✅ **Prompt Orchestrator** intelligent
✅ **LLM Service** complet avec streaming
✅ **Framework d'évaluation** avec métriques
✅ **Tests unitaires** > 70% coverage
✅ **Documentation** complète

---

## 📋 BACKLOG - Priorité Moyenne (Sprint 2+)

### 2. ✅ Amélioration Continue des Prompts
**Objectif:** Itérer sur les prompts basés sur les métriques

**Tâches:**
- [ ] A/B testing systématique
- [ ] Fine-tuning des températures par type de question
- [ ] Optimisation basée sur feedback utilisateur
- [ ] Few-shot learning dynamique

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
