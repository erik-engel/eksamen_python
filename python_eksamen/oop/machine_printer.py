class Machine: 
    
    def __init__(self):
        self.turned_on = False

    def turn_on(self):
        self.turned_on = True
        print("You have turned on the machine")

    def turn_off(self):
        self.turned_on = False
        print("You have shut off the machine")

    def state(self):
        if self.turned_on == True:
            return "The machine is ON"
        else:
            return "The machine is OFF"

class Printer(Machine):
    
    def __init__(self):
        self.turned_on = False
        self.tray = Papertray()

    def turn_on(self):
        return super().turn_on()
    
    def turn_off(self):
        return super().turn_off()

    def state(self):
        return super().state()

    def print(self, text):
        if self.turned_on == False:
            print(f"{self.state()}, please turn it on before you print!")
        else:
            if self.tray.is_paper == True:
                print("Printing ...")
                print(f"Printed text: {text}")
                self.tray.use_paper()
            elif self.tray.is_paper == False:
                self.tray.use_paper()

    def load_tray(self):
        print("How much many pieces would you like to load?")
        x = input("Amount: ")
        self.tray.add_paper(int(x))

class Papertray:

    def __init__(self):
        self.paper = 0
        self.is_paper = False

    def add_paper(self, paper):
        self.paper += paper
        if self.is_paper == False:
            self.is_paper = True

    def use_paper(self):
        if self.paper > 0:
            self.paper -= 1
            if self.paper > 0:
                print(f"There is {self.paper} pieces of paper left in the tray")
            elif self.paper == 0:
                print("You've used the last piece, please reload tray")
                self.is_paper = False
        elif self.paper == 0:
            print("The papertray is empty, please load in new paper")
            #self.is_paper = False



# Claus løsning med properties 

# class Machine:
#     """ takes care of turning on and off  """

#     def __init__(self):
#         self._is_on = False  # one _ = protected (to be used only in subclasses) 
    
#     def power(self):
#         self._is_on = not self._is_on

# class Printer(Machine):
#     def __init__(self):
#         Machine.__init__(self)
#         self.__pt = Papertray()

#     def print(self, text):
#         if self.__pt.paper == 0:
#             print('Papertray is empty')
#         else:
#             if self._is_on:
#                 print(text)
#                 self.__pt.paper = self.__pt.paper - 1
#             else:
#                 print('Printer is off')

#     @property
#     def load(self):
#         return self.__pt.paper

#     @load.setter
#     def load(self, no):
#         self.__pt.paper = no

# class Papertray:
#     def __init__(self):
#         self.paper = 2

#     @property
#     def paper(self):
#         return self.__paper

#     @paper.setter
#     def paper(self, paper):
#         self.__paper = paper
