from pathlib import Path
import json
import re
from ..normalization import fold

ROOT = Path(__file__).resolve().parents[3]

def load_fruits():
    with open(ROOT / "data" / "frutas.json", "r", encoding="utf-8") as f:
        return json.load(f)

def fruit_mentions(text):
    normalized = fold(text)
    counts = {}
    evidences = []
    for item in load_fruits():
        names = [item["nome"], *item.get("sinonimos", [])]
        total = 0
        for name in names:
            n = fold(name)
            matches = re.findall(rf"\b{re.escape(n)}\b", normalized)
            total += len(matches)
        if total:
            counts[item["nome"]] = total
            evidences.append({"fruta": item["nome"], "ocorrencias_textuais": total})
    return counts, evidences
