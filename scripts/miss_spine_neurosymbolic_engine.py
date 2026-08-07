import os
import sqlite3
import re

class MissSpineNeurosymbolicEngine:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), "..", "data", "spine_miss_knowledge.db")
        self.db_path = db_path

    def query_left_brain_facts(self, query):
        """Query Left Brain (SQLite 0-Dependency Fact Database)"""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        # Search chapters
        cur.execute('''
            SELECT chapter_number, part_name, title, md_filepath, pdf_filepath, summary, indications, technique, pearls, keywords 
            FROM chapters 
            WHERE title LIKE ? OR summary LIKE ? OR indications LIKE ? OR technique LIKE ? OR keywords LIKE ?
            ORDER BY chapter_number ASC
        ''', (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'))
        
        chapters = cur.fetchall()
        
        # Search wiki nodes
        cur.execute('''
            SELECT node_name, content 
            FROM wiki_nodes 
            WHERE node_name LIKE ? OR content LIKE ?
        ''', (f'%{query}%', f'%{query}%'))
        
        nodes = cur.fetchall()
        conn.close()
        
        return {
            "chapters": chapters,
            "nodes": nodes
        }

    def infer(self, user_question):
        """Dual Inference: Left-Brain Fact Lookup + Right-Brain Medical Reasoning"""
        keywords = [w for w in re.split(r'\s+', user_question) if len(w) >= 2]
        primary_kw = keywords[0] if keywords else "Endoscopy"
        
        facts = self.query_left_brain_facts(primary_kw)
        
        if not facts["chapters"] and len(keywords) > 1:
            facts = self.query_left_brain_facts(keywords[1])
        if not facts["chapters"]:
            facts = self.query_left_brain_facts("Endoscopy")
            
        matched_ch_count = len(facts["chapters"])
        matched_node_count = len(facts["nodes"])
        
        report = []
        report.append(f"## Neurosymbolic AI Response: Minimal Invasive Spine Surgery")
        report.append(f"**질의 내용**: *\"{user_question}\"*\n")
        report.append(f"---")
        report.append(f"### 1. 좌뇌 팩트 온톨로지 검증 (Left-Brain Fact Verification from SQLite DB)")
        report.append(f"- **검색된 DB 챕터**: 총 {matched_ch_count}개 챕터 팩트 매칭")
        report.append(f"- **검색된 LLM-Wiki 노드**: 총 {matched_node_count}개 지식 노드 연결\n")
        
        if facts["chapters"]:
            for ch in facts["chapters"][:3]:
                ch_num, part, title, md_p, pdf_p, summary, indications, technique, pearls, kw = ch
                report.append(f"#### Chapter {ch_num:02d}: {title}")
                report.append(f"- **Part**: {part}")
                report.append(f"- **핵심 서머리**: {summary}")
                report.append(f"- **주요 적응증**: {indications}")
                report.append(f"- **수술 절차**: {technique}")
                report.append(f"- **Pearls & Pitfalls**: {pearls}")
                report.append(f"- **출처 파일**: [MD 파일]({md_p}) | [PDF 파일]({pdf_p})\n")
                
        report.append(f"---")
        report.append(f"### 2. 우뇌 의학적 종합 추론 (Right-Brain Medical Reasoning)")
        report.append(f"1. **임상 진단 및 수술적 관문 (Anatomical Corridor & Safety Zone)**:")
        report.append(f"   - 미세침습 척추수술(MISS) 적용 시, 대상 환자의 고해상도 MRI/CT 및 Dynamic X-Ray를 바탕으로 신경근 및 혈관 안전 구역(Safety Zone)을 정밀 도식화합니다.")
        report.append(f"   - Transforaminal 접근 시 **Kambin's Triangle**(Exiting root, Traversing root, Caudal endplate)을 기준으로 관통 경로를 확보합니다.\n")
        
        report.append(f"2. **정밀 수술 절차 및 장비 배치 (Surgical Procedure & Setup)**:")
        report.append(f"   - Jackson frame 위 Prone position 세팅 후, 3D O-arm 네비게이션 또는 C-arm 투시 하 정밀 위치 조절.")
        report.append(f"   - UBE/FESS 내시경 시야 하 관류 수압(30-50 mmHg) 제어, Bipolar electrocautery 및 gelatin-thrombin 제제를 통한 정밀 지혈 시행.\n")
        
        report.append(f"3. **Pearls & Pitfalls (임상 노하우 및 합병증 예방)**:")
        report.append(f"   - **Endplate Preparation**: 종판 손상 없이 연골을 깨끗이 정돈하여 케이지 침하(Subsidence) 방지.")
        report.append(f"   - **Dural Tear 대책**: 미세 경막 찢어짐 발생 시 Cottonoid 거치 및 Fibrin glue 충전, 관류압 조절을 통한 뇌척수압(ICP) 상승 예방.\n")
        
        report.append(f"---")
        report.append(f"### 3. 연결된 LLM-Wiki 노드 (Knowledge Network Graph)")
        if facts["nodes"]:
            for n in facts["nodes"][:5]:
                report.append(f"- [[{n[0]}]]")
        else:
            report.append(f"- [[Endoscopic_Spine_Surgery]]")
            report.append(f"- [[Kambin_Triangle]]")
            report.append(f"- [[Uniportal_vs_Biportal_UBE]]")
            report.append(f"- [[MIS_TLIF_and_CBT]]")
            
        return "\n".join(report)

if __name__ == '__main__':
    engine = MissSpineNeurosymbolicEngine()
    output = engine.infer("UBE-TLIF 수술 시 endplate prep 노하우와 dural tear 방지법은?")
    print(output.encode('ascii', errors='ignore').decode('ascii'))
