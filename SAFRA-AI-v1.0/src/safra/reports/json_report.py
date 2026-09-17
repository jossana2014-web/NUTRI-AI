from pathlib import Path
import json, datetime
from ..config import ROOT

def save_analysis(payload, label="analise"):
    out = ROOT / "output" / "json"
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = out / f"{label}_{stamp}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path
