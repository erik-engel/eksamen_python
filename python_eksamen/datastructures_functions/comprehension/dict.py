# syntax
# dictionary = {key: value for vars in iterable}

square_dict = {}
for x in range(1,11):
    square_dict[x] = x*x
print(square_dict)

#er det samme som:

# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)