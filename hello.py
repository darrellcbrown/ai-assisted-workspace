def hello():
    return "Hello, World!"

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def countdown(n):
    return list(range(n, 0, -1))

if __name__ == "__main__":
    print(hello())
