def my_first_class_function(func):
    # execute
    print(func())

    # or return
    return func

def greet():
    return 'hello'

my_first_class_function(greet)

