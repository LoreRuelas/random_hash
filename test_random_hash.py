import random_hash

def test_find00_in1000Attempts_returns_bool():
    """Test that find00_in1000Attempts always returns a boolean."""
    result = random_hash.find00_in1000Attempts()
    assert isinstance(result, bool), "La función debe devolver True o False"
