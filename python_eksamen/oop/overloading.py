def __init__(self, *args):
    if len(args) == 1:
        self.name = args[0]
    elif len(args) == 2:
        self.name = args[0]
        self.sirn = args[1]
    else:
        raise NotImplemented

def __init__(self, name=None, age=None):
    if name != None:
        self.name = name
    if age != None:
        self.age = age