import random

class Bird:
    def __init__(self, start, dir):
        self.pos = start
        self.dir = dir

        self.methods = {'f':self.move_forward, 'l':self.turn_left, 'r': self.turn_right}


    def move_forward(self):
        if self.dir == 1:
            self.pos[1] = self.pos[1] + 1
        elif self.dir == 2:
            self.pos[0] = self.pos[0] + 1
        elif self.dir == 3:
            self.pos[1] = self.pos[1] - 1
        else:
            self.pos[0] = self.pos[0] - 1

    def turn_left(self):
        if self.dir == 1:
            self.dir = 4
        else:
            self.dir -= 1

    def turn_right(self):
        if self.dir == 4:
            self.dir = 1
        else:
            self.dir += 1
    
    def loose(self):
        return 'The bird has lost the game'

    def __repr__(self):
        return f'{self.__dict__}'


class Pig:
    def __init__(self, pos):
        self.pos = pos
        self.is_alive = True
    
    def die(self):
        self.is_alive = False
        return "the pig is dead"

class Board:
    def __init__(self, bpos, bdir, ppos):
        self.bird = Bird(bpos, bdir)
        #self.c = Bird.__dict__
        self.pig = Pig(ppos)

    def run(self, cmd):
        for i in cmd:
            self.bird.methods[i]()

    def display(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i,j) == tuple(self.bird.pos) and self.bird.dir==1:
                    print('B>', end = ' ')
                elif(i,j) == tuple(self.bird.pos) and self.bird.dir==2:
                    print('B\u2228', end = ' ')
                elif(i,j) == tuple(self.bird.pos) and self.bird.dir==3:
                    print('B<', end = ' ')
                elif(i,j) == tuple(self.bird.pos) and self.bird.dir==4:
                    print('B\u2227', end = ' ')
                elif(i,j) == tuple(self.pig.pos):
                    print('P', end = '  ')
                else:
                    print('*', end = '  ')
            print()


class Workspace:
    def __init__(self):
        self.moves = None

    def display(self):
        print('\nWhat steps do you want to perform?')
        print('Options: move forward (f), turn left (l), turn right (r)')
        print('Type "q" when finished')

    def commands(self):
        l = []
        q = True
        while q:
            x = input('Move: ')
            if x == 'q':
                q = False
            else:
                l.append(x)
        
        return l

class Game:
    
    def main(self, bpos, bdir, ppos):
        b = Board(bpos,bdir,ppos)
        b.display()

        w = Workspace()
        w.display()

        l = w.commands()
        b.run(l)

        print(self.win(b))
        print(f'Birds position: {b.bird.pos}')
        print(f'Pigs position: {b.pig.pos}')

    def win(self, b):
        if b.bird.pos == b.pig.pos:
            return b.pig.die()
        else:
            return b.bird.loose()

dir=[1,2,3,4]
pos=[1,2,3,4,5,6,7,8,9,10]

g = Game()
g.main([random.choice(pos),random.choice(pos)], random.choice(dir), [random.choice(pos),random.choice(pos)])

