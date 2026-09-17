from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]

def load_config():
    with open(ROOT / "safra.config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def workspace_root():
    cfg = load_config()
    return (ROOT / cfg.get("workspace", {}).get("root_dir", "..")).resolve()

def cardapios_dir():
    cfg = load_config()
    ws = cfg.get("workspace", {})
    configured = (ROOT / ws.get("cardapios_dir", "../Cardápios")).resolve()
    if configured.exists():
        return configured
    if ws.get("auto_discovery", True):
        parent = workspace_root()
        for name in ws.get("accepted_directory_names", []):
            candidate = parent / name
            if candidate.exists() and candidate.is_dir():
                return candidate.resolve()
    return configured
