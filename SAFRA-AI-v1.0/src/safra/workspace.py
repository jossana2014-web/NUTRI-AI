from pathlib import Path
from .config import cardapios_dir, ROOT

def diagnostic():
    folder = cardapios_dir()
    checks = {
        "safra_root": str(ROOT),
        "cardapios_path": str(folder),
        "cardapios_exists": folder.exists(),
        "agents_exists": (ROOT / "agents").exists(),
        "skills_exists": (ROOT / "skills").exists(),
        "specs_exists": (ROOT / "specs").exists(),
        "rules_exists": (ROOT / "rules").exists(),
        "knowledge_exists": (ROOT / "knowledge").exists(),
        "data_exists": (ROOT / "data").exists()
    }
    return checks
