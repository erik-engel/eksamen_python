def my_decorator(func):
    def wrapper():
        print("Something before the function is called")
        func()
        print("Something after the function is called")
    return wrapper

def greet():
    print('Hello')

greet = my_decorator(greet)
greet()

@my_decorator
def greeting():
    print('Hello')

greeting()