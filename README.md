# 🩺 Minimally Invasive Spine Surgery (MISS) Neurosymbolic AI Agent Skill Container

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Architecture: Neurosymbolic AI](https://img.shields.io/badge/Architecture-Neurosymbolic%20AI-emerald.svg)]()
[![Fact DB: 0--Dependency SQLite](https://img.shields.io/badge/Fact%20DB-0--Dependency%20SQLite-purple.svg)]()
[![Textbook: Springer 2026](https://img.shields.io/badge/Textbook-Springer%202026-orange.svg)]()

> **World-Class Autonomous Skill Container** built for **Dr. Choi (최선종 원장님 - World Authority in Biportal Endoscopic Spine Surgery & MISS)**, packaging 2026 *Textbook of Minimally Invasive Spine Surgery: Concepts and Surgical Techniques* (Springer Nature) by Yoshihisa Kotani, Jin-Sung Kim (가톨릭대 서울성모병원), and Frank M. Phillips.

---

## 🏛️ 4-Tier AGI Container Architecture

1. **Left-Brain Fact Verification (0-Dependency SQLite Database)**
   - `data/spine_miss_knowledge.db`: 70 Chapters, 18 Parts, clinical indications, step-by-step techniques, and pearls & pitfalls.
2. **LLM-Wiki Knowledge Topology (`llm_wiki/`)**
   - 12 Karpathy-style `[[Wikilink]]` nodes (`Kambin_Triangle.md`, `Uniportal_vs_Biportal_UBE.md`, `MIS_TLIF_and_CBT.md`, `OLIF_LLIF_ALIF_OLIF51.md`, etc.).
3. **Dual-Inference Neurosymbolic Engine (`scripts/miss_spine_neurosymbolic_engine.py`)**
   - Combines Left-Brain fact indexing with Right-Brain LLM medical reasoning.
4. **Instant 1-Second Portable Skill Container**
   - Packaged for GitHub, Antigravity Agent, Claude Code, and Firebase hosting.

---

## 🚀 Installation & Portable Deployment

Clone this container directly into your agent's `.agents/skills/` root:

```bash
git clone https://github.com/sunjongos/miss_spine_neurosymbolic_ontology.git .agents/skills/miss_spine_neurosymbolic_ontology
```

---

## 💻 CLI Usage

### Fact Database Search
```bash
python scripts/query_spine_dm.py UBE
```

### Neurosymbolic Inference Query
```bash
python scripts/run_miss_spine_agent.py "UBE-TLIF 수술 시 endplate prep 노하우와 dural tear 방지법은?"
```

---

## 📄 License
MIT License - Designed for Namyangju Baek Hospital (NDB) & Doctor Choi's AI Research Systems.
