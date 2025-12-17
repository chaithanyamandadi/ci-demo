from app import add

def test_add():
    result = add(2, 3)
    print("Result from app.py:", result)
    assert result == 5