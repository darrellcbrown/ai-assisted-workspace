from hello import hello, greet, farewell, countdown

def test_hello():
    assert hello() == "Hello, World!"

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("World") == "Hello, World!"

def test_farewell():
    assert farewell("Alice") == "Goodbye, Alice!"
    assert farewell("World") == "Goodbye, World!"

def test_countdown():
    assert countdown(5) == [5, 4, 3, 2, 1]
    assert countdown(1) == [1]
    assert countdown(0) == []
