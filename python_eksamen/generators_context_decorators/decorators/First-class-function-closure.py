def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function

# equals to inner_function waiting to be executed 
my_func = outer_function()

my_func()
my_func()

# this is what closure does. It my_func() remembers inner_function even though outer_function() has been executed
