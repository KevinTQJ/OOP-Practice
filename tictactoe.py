from random import randint, choice



class Game:
    def __init__(self, player1, player2):
        self.board = {['', '', ''], ['', '', ''], ['', '', '']}
        self.player1 = player1
        self.player2 = player2
        self.winStatus = False

    def decideFirst(self):
        self.currentPlayer = choice(self.player1, self.player2)
        return self.currentPlayer

    def setLocation(self):
        if Player.isValidStep():
            self.board[player.locationRow][player.locationColumn] = self.currentPlayer
        else:
            print('This spot has been taken, choose another one')

    def printBoard(self):
        for i in range(0, 3):
            print('\n')
            for j in range(0, 3):
                print(self.board[i][j], ' ')

    def getWinner(self):
        if self.winStatus:
            return self.currentPlayer

class Player():
    def __init__(self):
        self.locationColumn = int
        self.locationRow = int

    def askStep(self):
        self.locationRow = int(input('Choose a row'))
        self.locationColumn = int(input('Choose a column'))
  

    def isValidStep(self):
        if self.board[player.locationRow][player.locationColumn] is None:
            return True
        print('This spot has been taken, choose another one')
        return False


    def win(self):
        for i in range(0, 3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2]) or (self.board[0][i] == self.board[1][i] == self.board[2][i]):
                self.winStatus = True
                #horizontal and vertical
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) or (self.board[2][0] == self.board[1][1] == self.board[0][2]):
            self.winStatus = True
        #diagonal


 class Computer(Player):
    def __init__(self):
        super().__init__(locationRow, locationColumn)

    def askStep(self):
        self.locationRow = randint(0, 3)
        self.locationColumn = randint(0, 3)



def main():
    while True:
        try:
            gameType = int(input('''Choose game type:
            1 - Player vs. Player
            2 - Player vs. Computer
            '''))
            if gameType == 1 or gameType == 2:
                break
            else:
                print('\nPlease enter 1 or 2\n')
        except:
            print('\nInvalid Input, try again\n')

    if gameType == 1:
        pvp = Game(p1, p2)
    elif gameType == 2:
        pvc = Game(p1, c1)


main()
