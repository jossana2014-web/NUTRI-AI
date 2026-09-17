from pathlib import Path
from safra.config import ROOT

def test_structure():
    for name in ["agents","skills","specs","rules","knowledge","data"]:
        assert (ROOT / name).exists()
