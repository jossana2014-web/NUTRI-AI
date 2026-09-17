import argparse
import json
from pathlib import Path
from .scanner import scan
from .workspace import diagnostic
from .extraction import extract
from .classification import fruit_mentions
from .reports import save_analysis

def cmd_diagnostico():
    d = diagnostic()
    print("SAFRA-AI — DIAGNÓSTICO")
    for k,v in d.items():
        if isinstance(v, bool):
            print(f"[{'OK' if v else 'ERRO'}] {k}: {v}")
        else:
            print(f"      {k}: {v}")

def cmd_listar():
    s = scan()
    if not s["exists"]:
        print("ERRO: pasta de cardápios não encontrada.")
        print("Esperado:", s["folder"])
        return
    print(f"Pasta: {s['folder']}")
    print(f"Arquivos encontrados: {len(s['files'])}")
    for i,f in enumerate(s["files"], start=1):
        print(f"{i:02d}. {f['name']} | período={f['period']} | {f['extension']}")

def select_files(period=None):
    s = scan()
    if not s["exists"]:
        return []
    files = s["files"]
    if period:
        files = [f for f in files if f.get("period") == period]
    return files

def cmd_analisar(period=None):
    files = select_files(period)
    if not files:
        print("Nenhum cardápio encontrado para o filtro informado.")
        return
    results = []
    for f in files:
        data = extract(f["path"])
        counts, evidences = fruit_mentions(data.get("text",""))
        result = {
            "arquivo": f["name"],
            "periodo_inferido": f.get("period"),
            "sha256": f["sha256"],
            "frutas_ocorrencias_textuais": counts,
            "evidencias": evidences,
            "avisos": []
        }
        if data.get("warning"):
            result["avisos"].append(data["warning"])
        if not data.get("text"):
            result["avisos"].append("Não houve texto extraível; poderá ser necessário OCR em versão futura.")
        results.append(result)
        print(f"\nARQUIVO: {f['name']}")
        if counts:
            for fruit, n in sorted(counts.items(), key=lambda x:(-x[1], x[0])):
                print(f"  {fruit}: {n}")
        else:
            print("  Nenhuma fruta reconhecida automaticamente.")
    payload = {
        "tipo": "analise_experimental",
        "periodo_filtro": period,
        "resultados": results,
        "observacao": "Contagens desta versão são ocorrências textuais e não equivalem automaticamente a dias de oferta."
    }
    path = save_analysis(payload, "analise")
    print("\nJSON salvo em:", path)

def cmd_comparar(p1, p2):
    payload = {}
    for p in [p1,p2]:
        aggregate = {}
        for f in select_files(p):
            data = extract(f["path"])
            counts,_ = fruit_mentions(data.get("text",""))
            for fruit,n in counts.items():
                aggregate[fruit] = aggregate.get(fruit,0)+n
        payload[p] = aggregate
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    path = save_analysis({"tipo":"comparacao_experimental","periodos":[p1,p2],"dados":payload}, "comparacao")
    print("JSON salvo em:", path)

def main():
    parser = argparse.ArgumentParser(prog="safra")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("diagnostico")
    sub.add_parser("listar")

    pa = sub.add_parser("analisar")
    pa.add_argument("--periodo", help="Ex.: 2025-04")

    pc = sub.add_parser("comparar")
    pc.add_argument("periodo1")
    pc.add_argument("periodo2")

    args = parser.parse_args()
    if args.cmd == "diagnostico":
        cmd_diagnostico()
    elif args.cmd == "listar":
        cmd_listar()
    elif args.cmd == "analisar":
        cmd_analisar(args.periodo)
    elif args.cmd == "comparar":
        cmd_comparar(args.periodo1, args.periodo2)
