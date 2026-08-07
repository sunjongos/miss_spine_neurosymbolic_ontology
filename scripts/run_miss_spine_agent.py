import sys
import os

# Add scripts dir to path
sys.path.append(os.path.dirname(__file__))

from miss_spine_neurosymbolic_engine import MissSpineNeurosymbolicEngine

def main():
    query = sys.argv[1] if len(sys.argv) > 1 else "Kambin triangle 및 UBE 수술 기법"
    engine = MissSpineNeurosymbolicEngine()
    result = engine.infer(query)
    
    # Save test result to scratch
    out_file = r"c:\Users\USER\Desktop\luca연구에이전트\scratch\miss_agent_response.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(result)
        
    print(f"Executed MISS Spine Neurosymbolic Agent query for: '{query}'")
    print(f"Saved response to '{out_file}'")

if __name__ == '__main__':
    main()
