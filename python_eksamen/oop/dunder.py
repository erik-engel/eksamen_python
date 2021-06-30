class S:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__dict__}'
    def __str__(self):
        return f'Name: {self.name}'
    def __add__(self, other):
        return S(f'{self.name} {other.name}')

s = S('erik')
s1 = S('claus')
print(s + s1)


class Deck:
    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    def __getitem__(self, key):
        return self.cards[key]

    def __repr__(self):
        return f'{self.__dict__}'

    def __len__(self):
        return len(self.cards)
