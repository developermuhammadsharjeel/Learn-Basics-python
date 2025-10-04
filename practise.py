def greet(fx):
    def hello(*args, **kwargs):
        print("hello friends")
        fx(*args, **kwargs)
        print("good bye")
    return hello
    

@greet
def add(a, b):
    print(a + b)
    
add(10,12)