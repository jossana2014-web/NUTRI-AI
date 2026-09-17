from pypdf import PdfReader

def extract_pdf(path):
    reader = PdfReader(path)
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append({"page": i, "text": text})
    return {"pages": pages, "text": "\n".join(p["text"] for p in pages)}
