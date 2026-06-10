from hello import hello, greet, farewell, countdown, add, multiply, fibonacci, is_palindrome

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

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
    import pytest
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
