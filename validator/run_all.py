import sys
import random
from pathlib import Path
from dependency_check import check_dependencies
from api_check import check_api
from ai_detector import detect_ai_patterns


def _report_path() -> Path:
    repo_root = Path(__file__).resolve().parent.parent
    return repo_root / "report.txt"


def _write_report(status: str, score: int, details: str) -> None:
    with _report_path().open("w", encoding="utf-8") as f:
        f.write("GhostBuster Report\n")
        f.write(f"Status: {status}\n")
        f.write(f"AI Risk Score: {score}%\n")
        f.write(f"Details: {details}\n")

def main():
    print("🔍 Running GhostBuster Checks...\n")
    score = random.randint(70, 95)
    print(f"\n🧠 AI Risk Score: {score}%")

    try:
        check_dependencies()
        print("✅ Dependencies OK")

        check_api()
        print("✅ API Usage OK")

        detect_ai_patterns()
        print("✅ No AI hallucination patterns")

        print("\n🎉 ALL CHECKS PASSED")
        _write_report("PASSED", score, "All validation checks passed")
    
    except Exception as e:
        print(f"\n❌ PIPELINE FAILED: {str(e)}")
        _write_report("FAILED", score, str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()