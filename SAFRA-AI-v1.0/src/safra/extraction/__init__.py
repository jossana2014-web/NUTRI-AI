from pathlib import Path
from .pdf import extract_pdf

def extract(path):
    p = Path(path)
    if p.suffix.lower() == ".pdf":
        return extract_pdf(p)
    return {
        "pages": [],
        "text": "",
        "warning": "Formato reconhecido pelo scanner, mas extração ainda não implementada nesta versão."
    }
