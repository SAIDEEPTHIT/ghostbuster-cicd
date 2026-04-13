from pathlib import Path


def _target_file() -> Path:
    repo_root = Path(__file__).resolve().parent.parent
    return repo_root / "sample_code" / "main.py"


def check_api():
    code = _target_file().read_text(encoding="utf-8")

    if "non_existent_function(" in code:
        raise Exception("Invalid API usage detected")