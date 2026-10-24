# 🛡️ Aegis-Agent: Autonomous LLM Red-Teaming & Guardrail Framework

An autonomous, multi-layer security guardrail and red-teaming pipeline designed to harden Large Language Models (LLMs) against prompt injections, roleplay jailbreaks, and syntax bypasses. Built entirely to run **locally and air-gapped** via Ollama and Llama 3.2.

---

## 🏗️ Architecture & Defense Pipeline

The system utilizes a **two-tier defense architecture** optimized for speed and semantic accuracy:

1. **Layer 1 (Deterministic Regex Filter):** 
   * Rapidly scans incoming text against compiled regular expressions to catch known attack vectors, instruction overrides, and direct system prompt extractions with zero latency.
2. **Layer 2 (Semantic Intent Classifier):** 
   * If a prompt passes Layer 1, it is evaluated by a local instance of **Llama 3.2** configured as a strict security classifier to detect abstract roleplay framing, indirect injections, and semantic jailbreaks.
3. **Autonomous Red-Team Agent (`red_team_agent.py`):** 
   * A generative testing agent that systematically generates syntax boundary-testing probes and adversarial test vectors to stress-test the guardrail pipeline.

---

## 📂 Project Structure

```text
llm-guardrail-validator/
│
├── guardrails.py           # Unified multi-layer validation pipeline (Layer 1 + Layer 2)
├── semantic_validator.py   # Llama 3.2 semantic intent classifier
├── red_team_agent.py       # Autonomous adversarial prompt generator & test runner
├── test_guardrails.py      # Comprehensive Pytest regression suite
└── README.md               # Project documentation