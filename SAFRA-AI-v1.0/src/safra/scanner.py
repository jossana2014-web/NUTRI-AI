from pathlib import Path
import hashlib
import re
from .config import cardapios_dir, load_config

def sha256(path: Path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def guess_period(name: str):
    s = name.lower()
    months = {
        "janeiro":"01","fevereiro":"02","marco":"03","março":"03","abril":"04",
        "maio":"05","junho":"06","julho":"07","agosto":"08","setembro":"09",
        "outubro":"10","novembro":"11","dezembro":"12"
    }
    year = re.search(r"(20\d{2})", s)
    for m,n in months.items():
        if m in s:
            return f"{year.group(1) if year else '????'}-{n}"
    return None

def scan():
    cfg = load_config()
    folder = cardapios_dir()
    exts = set(cfg["workspace"]["accepted_extensions"])
    if not folder.exists():
        return {"folder": str(folder), "exists": False, "files": []}
    files = []
    for p in sorted(folder.iterdir()):
        if p.is_file() and p.suffix.lower() in exts:
            files.append({
                "name": p.name,
                "path": str(p),
                "extension": p.suffix.lower(),
                "period": guess_period(p.name),
                "sha256": sha256(p)
            })
    return {"folder": str(folder), "exists": True, "files": files}
