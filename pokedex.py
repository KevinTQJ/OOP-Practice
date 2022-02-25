import sqlite3
from random import choice

class Pokemon():
    def __init__(self, ID = ' ', species = ' ', height = ' ', mass =' '):
        self.ID = ID
        self.height = height
        self.mass = mass
        self.species = species
        self.name = ' '

    def setName(self, name):
        self.name = name

    def speak(self):
        return self.name, self.species

    def move(self, moveList):
        return choice(moveList)

    def getStats(self):
        print(f'Name: {self.name:<10} ID: {self.ID:<5} Type: {self.pokeType:<10} Species: {self.species:<10} Height: {self.height} in.   Mass: {self.mass} lbs\n')



class Grass(Pokemon):
    def __init__(self, ID = ' ', species = ' ', height = ' ', mass =' ', pokeType = 'Grass'):
        super(Grass, self).__init__(ID, species, height, mass)
        self.pokeType = pokeType
        self.moveList = ['Vine Whip', 'Razor Leaf', 'Cut']

    def move(self):
        return super(Grass,self).move(self.moveList)



class Fire(Pokemon):
    def __init__(self, ID = ' ', species = ' ', height = ' ', mass =' ', pokeType = 'Fire'):
        super(Fire, self).__init__(ID, species, height, mass)
        self.pokeType = pokeType
        self.moveList = ['Flare', 'Ember', 'Flamethrower']

    def move(self):
        return super(Fire,self).move(self.moveList)



class Water(Pokemon):
    def __init__(self, ID = ' ', species = ' ', height = ' ', mass =' ', pokeType = 'Water'):
        super(Water, self).__init__(ID, species, height, mass)
        self.pokeType = pokeType
        self.moveList = ['Bubble', 'Water Gun', 'Splash']

    def move(self):
        return super(Water,self).move(self.moveList)



class Electric(Pokemon):
    def __init__(self, ID = ' ', species = ' ', height = ' ', mass =' ', pokeType = 'Electric'):
        super(Electric, self).__init__(ID, species, height, mass)
        self.pokeType = pokeType
        self.moveList = ['Electro Ball', 'Thunderbolt', 'Shock']

    def move(self):
        return super(Electric,self).move(self.moveList)



def insertPokemon(c):
    insertTuple = ('ID', 'species', 'pokeType', 'height', 'mass')
    lis = []
    while True:
        try:
            for i in range(len(insertTuple)):
                lis.append(input(f'Please enter new Pokemon\'s {insertTuple[i]}: '))
            valueInsert = (int(lis[0]), lis[1], lis[2], int(lis[3]), float(lis[4]))
            break
        except:
            lis.clear()
            print('Invalid input for one or more stat(s), try again')

    c.execute(f'INSERT INTO SPECIES VALUES {valueInsert};')
    print('New Pokemon Inserted successfully')


def killSwitch():
    while True:
        check = input('\nDo you want to insert a new species of Pokemon?(Y/N)').lower()
        if check == 'y':
            return True
        elif check == 'n':
            return False
        else:
            print('Invalid Input.')


def main():
    conn = sqlite3.connect('pokedex.db')
    c = conn.cursor()
    cursor = c.execute('SELECT * from SPECIES WHERE ID = 1 OR ID = 4 OR ID = 7 OR ID = 25;') # only display the original pokemons as instruction requires
    pokeList = []

    for row in cursor:
        ID = row[0]
        species = row[1]
        pokeType = row[2]
        height = row[3]
        mass = row[4]

        if pokeType =='Grass':
            Daniel = Grass(ID, species, height, mass, pokeType)
            Daniel.setName('Daniel')
            Abubakr = Grass(ID, species, height, mass, pokeType)
            Abubakr.setName('Abubakr')
        elif pokeType == 'Fire':
            Mitchell = Fire(ID, species, height, mass, pokeType)
            Mitchell.setName('Mitchell')
            Marco = Fire(ID, species, height, mass, pokeType)
            Marco.setName('Marco')
        elif pokeType == 'Water':
            Theresa = Water(ID, species, height, mass, pokeType)
            Theresa.setName('Theresa')
            Irene = Water(ID, species, height, mass, pokeType)
            Irene.setName('Irene')
        elif pokeType == 'Electric':
            Harry = Electric(ID, species, height, mass, pokeType)
            Harry.setName('Harry')
            Lyndesy = Electric(ID, species, height, mass, pokeType)
            Lyndesy.setName('Lyndesy')

    pokeList = (Daniel, Abubakr, Mitchell, Marco, Theresa, Irene, Harry, Lyndesy)
    for i in pokeList:
        name, species = i.speak()
        print(f'I am {name}, a(n){species}!')
        print(f'{i.move()}!!!')
        i.getStats()

    ask = killSwitch()
    if ask:
        insertPokemon(c)
        conn.commit()
    else:
        pass

    print('End of Kevin Wu\'s Pokedex\nExited the program')
    
    conn.close()


main()
