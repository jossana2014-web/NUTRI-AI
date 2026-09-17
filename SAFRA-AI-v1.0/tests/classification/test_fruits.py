from safra.classification import fruit_mentions

def test_recognize_banana():
    counts, _ = fruit_mentions("BANANA banana")
    assert counts["banana"] == 2

def test_not_create_unknown():
    counts, _ = fruit_mentions("arroz feijão")
    assert "banana" not in counts
