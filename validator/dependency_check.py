from pathlib import Path


def _target_file() -> Path:
    repo_root = Path(__file__).resolve().parent.parent
    return repo_root / "sample_code" / "main.py"


def check_dependencies():
    code = _target_file().read_text(encoding="utf-8")

    if "fake_library" in code:
        raise Exception("Dependency 'fake_library' does not exist")