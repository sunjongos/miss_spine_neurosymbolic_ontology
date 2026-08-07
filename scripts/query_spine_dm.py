import sqlite3
import os
import sys

def query_spine_db(keyword):
    db_file = os.path.join(os.path.dirname(__file__), 'spine_miss_knowledge.db')
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    
    print(f"==================================================")
    print(f" LUCA SPINE MISS DOMAIN MODEL SEARCH: '{keyword}'")
    print(f"==================================================")
    
    cur.execute('''
        SELECT chapter_number, title, part_name, md_filepath, pdf_filepath 
        FROM chapters 
        WHERE title LIKE ? OR summary LIKE ? OR indications LIKE ? OR technique LIKE ?
        ORDER BY chapter_number ASC
    ''', (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    
    chapters = cur.fetchall()
    print(f"\nMatching Chapters ({len(chapters)} found):")
    for c in chapters:
        title_clean = str(c[1]).encode('ascii', errors='ignore').decode('ascii')
        print(f"  * Ch {c[0]:02d}: {title_clean}")
        print(f"    - MD Path : {c[3]}")
        print(f"    - PDF Path: {c[4]}")
        
    cur.execute('''
        SELECT node_name, filepath 
        FROM wiki_nodes 
        WHERE node_name LIKE ? OR content LIKE ?
    ''', (f'%{keyword}%', f'%{keyword}%'))
    
    nodes = cur.fetchall()
    print(f"\nMatching LLM-Wiki Graph Nodes ({len(nodes)} found):")
    for n in nodes:
        print(f"  * [[{n[0]}]] -> {n[1]}")
        
    conn.close()

if __name__ == '__main__':
    kw = sys.argv[1] if len(sys.argv) > 1 else "UBE"
    query_spine_db(kw)
