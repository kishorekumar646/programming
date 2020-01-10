class TicTacToe:

    X,O,EMPTY = 1,-1,0
    board = [[0 for i in range(3)] for j in range(3)]
    player = X
    isEmpty = True

    #inserting the board positions
    def insert(self,x,y):   
        if (x<0) or (x>2) or (y<0) or (y>2):
            print("Invalid Board Position")
            return
        if self.board[x][y] != self.EMPTY:
            print("Board position occupied")
            return
        self.board[x][y] = self.player
        self.player = -self.player

    #Displaying the board
    def displayBoard(self):
        self.isEmpty=False
        print(self.board,"\n")
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 1:
                    print(" X ",end="")
                if self.board[i][j] == -1:
                    print(" O ",end="")
                if self.board[i][j] == self.EMPTY:
                    print("   ",end="")
                    self.isEmpty=True
                if j<2:
                    print("|",end="")
            if i<2:
                print("\n-----------")
        print("\n")

    #checking the winner
    def isWin(self,player):
        return (
            (self.board[0][0] + self.board[0][1] + self.board[0][2] == player*3) or
            (self.board[1][0] + self.board[1][1] + self.board[1][2] == player*3) or
            (self.board[2][0] + self.board[2][1] + self.board[2][2] == player*3) or
            (self.board[0][0] + self.board[1][0] + self.board[2][0] == player*3) or
            (self.board[0][1] + self.board[1][1] + self.board[2][1] == player*3) or
            (self.board[0][2] + self.board[1][2] + self.board[2][2] == player*3) or
            (self.board[0][0] + self.board[1][1] + self.board[2][2] == player*3) or
            (self.board[2][0] + self.board[1][1] + self.board[0][2] == player*3) 
        )

    #display the winner
    def displayWinner(self):
        if self.isWin(self.X):
            print("\n  X WINNER  \n")
            self.isEmpty=False
        elif self.isWin(self.O):
            print("\n  O WINNER  \n")
            self.isEmpty=False
        else:
            if (self.isEmpty == False):
                print ("\n  XO DRAW  \n")

# here start the game                
t = TicTacToe()
while t.isEmpty:
    print("Player X turn" if t.player == t.X else "Player O turn")
    print("Enter x and y places : ")
    x = int(input("x : "))
    y = int(input("y : "))
    t.insert(x,y)
    t.displayBoard()
    print("_________________________\n")
    t.displayWinner()