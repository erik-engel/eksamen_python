class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,10)

# for num in nums:
#     print(num)

#Vil fejle, fordi iter af nums allerede har kaldet next på alle dens værdier i for loopet
# print(next(nums))

# Generator function

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# nums1 = my_range(1,10)

# for num in nums1:
#     print(num)

# #Vil fejle, fordi iter af nums allerede har kaldet next på alle dens værdier i for loopet
# print(next(nums1))

def my_range(start):
    current = start
    while True:
        yield current
        current += 1

nums1 = my_range(1)

for num in nums1:
    print(num)

