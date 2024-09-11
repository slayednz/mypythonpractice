from hello import hello

def test_argument():
    for name in ["Harry", "Hermione", "Ron"]:
        assert hello(name) == f"hello, {name}"
    assert hello() == "hello, world"

def test_default():
    assert hello() == "hello, world"