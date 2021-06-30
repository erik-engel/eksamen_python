# class Car:
#     wheels = 4
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage

#     def __str__(self):
#         return f"The {self.color} car has {self.mileage:,} miles."

# car1 = Car("blue", 20000)
# car2 = Car("red", 30000)
# print(car1)
# print(car2)

class Car:
    def __init__(self, *args):
        self.make = args[0]
        self.model = args[1]
        self.bhp = args[2]
        self.mph = args[3]

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, make):
        self.__make = make

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def bhp(self):
        return self.__bhp
    
    @bhp.setter
    def bhp(self, bhp):
        self.__bhp = bhp

    @property
    def mph(self):
        return self.__mph

    @mph.setter
    def mph(self, mph):
        self.__mph = mph