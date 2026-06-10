def hello():
    return "Hello, World!"

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def countdown(n):
    return list(range(n, 0, -1))

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print(hello())
