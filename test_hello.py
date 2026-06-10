from hello import hello, greet, farewell

def test_hello():
    assert hello() == "Hello, World!"

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("World") == "Hello, World!"

def test_farewell():
    assert farewell("Alice") == "Goodbye, Alice!"
    assert farewell("World") == "Goodbye, World!"
