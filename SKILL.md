---
name: miss_spine_neurosymbolic_ontology
description: 미세침습 척추수술(MISS) 전담 Neurosymbolic AI Agent 스킬. 0-Dependency SQLite 팩트 온톨로지 DB(spine_miss_knowledge.db - 70개 챕터, 18개 Part)와 우뇌 의학 추론 엔진을 결합하여 환자 증상/수술 질의에 대해 무결점 팩트 추론 및 수술 가이던스를 제공합니다.
---

# Minimally Invasive Spine Surgery (MISS) Neurosymbolic AI Skill Container

본 스킬은 지난 7년간 BESS(양방향 척추 내시경 수술) 수술 집도 건수 전 세계 1위(World No. 1)이신 최선종 대표원장님의 임상 지혜와 2026년 최신 **《Textbook of Minimally Invasive Spine Surgery: Concepts and Surgical Techniques (Springer)》** 835페이지, 18개 Part, 70개 Chapter 및 12개 Karpathy-style LLM-Wiki 지식망을 기반으로 구동되는 **독자적 Neurosymbolic 척추수술 전담 AI 에이전트 스킬**입니다.

## 📌 주요 기능 (Core Capabilities)

1. **좌뇌 팩트 검증 (SQLite 0-Dependency Fact Database)**
   - `spine_miss_knowledge.db` 데이터베이스 조회를 통해 70개 챕터의 인디케이션, 접근로, 수술 기법 및 Pearls & Pitfalls 팩트 100% 매칭
   - 출처 핀포인트 [MD 파일] 및 [PDF 파일] 경로 자동 제공

2. **우뇌 의학적 종합 추론 (Dual Inference Engine)**
   - **Anatomical Corridor & Safety Zone**: Kambin's Triangle, Wiltse approach, Retroperitoneal anterior/oblique psoas 안전 진입 구역 추론
   - **Step-by-Step Surgical Technique**: C-arm/O-arm 네비게이션, 관류 수압 제어(30-50 mmHg), Endplate prep 및 케이지/나사 고정 프로토콜
   - **Pearls & Pitfalls**: 경막 찢어짐(Dural tear), 신경근 열손상, 관류 수압 상승(ICP) 및 혈관 손상 예방 대책

3. **LLM-Wiki 지식 네트워크 연결 (`[[Wikilink]]`)**
   - [[Endoscopic_Spine_Surgery]], [[Kambin_Triangle]], [[Uniportal_vs_Biportal_UBE]], [[MIS_TLIF_and_CBT]], [[OLIF_LLIF_ALIF_OLIF51]], [[Spine_Navigation_and_Robotics]] 지식 그래프 1:1 토폴로지 연결

---

## 🛠️ 실행 및 사용법 (Execution Instructions)

### 1. 파이썬 추론 엔진 단독 구동
```bash
python .agents/skills/miss_spine_neurosymbolic_ontology/scripts/miss_spine_neurosymbolic_engine.py
```

### 2. 에이전트 대화형 호출
대표님께서 척추 수술 기법, 적응증, 합병증 방지법을 질의하시면 본 스킬이 자동으로 가동되어 **[좌뇌 팩트 DB 검증 ➔ 우뇌 의학 추론 ➔ 핀포인트 출처 ➔ LLM-Wiki 연결]** 4단계 파이프라인으로 무결점 답변을 출력합니다.
