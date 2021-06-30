# # Alm funktion
# def square_numbers(nums):
#     result = []
#     for i in nums: 
#         result.append(i*i)
#     return result



# Generator funktion
# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])

# list print
# print(my_nums) #output = [1,4,9,16,25]

# # generator print
# print (next(my_nums)) #1
# print (next(my_nums)) #4
# print (next(my_nums)) #9
# print (next(my_nums)) #16
# print (next(my_nums)) #25
# print (next(my_nums)) # StopIteration Error, because generator only has 5 inputs, out of values

#generator for loop is possible

# for num in my_nums:
#     print(num)

# for loop nows to stop before StopIteration exception.

# Generator Comprehension

#listcomprehension
# my_nums = [x*x for x in [1,2,3,4,5]]
# print(my_nums)

#generatorcomprehension
my_nums = (x*x for x in [1,2,3,4,5])
print(next(my_nums))
for num in my_nums:
    print(num)
print(next(my_nums))