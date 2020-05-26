# tic tac toe class
class tic_tac_toe:
    #init function
    def __init__(self): 
        #global variable is the game over
        self.global_var=False
        # board can use matrix or normal list
        self.board=["-","-","-",
                    "-","-","-",
                    "-","-","-"]
        # Winner variable
        self.winner='none'
        #player
        self.player="X"


    # display board
    def display (self):
        print(self.board[0]+" | "+self.board[1]+" | "+self.board[2])
        print(self.board[3]+" | "+self.board[4]+" | "+self.board[5])
        print(self.board[6]+" | "+self.board[7]+" | "+self.board[8])

                
    # checking who won
    def check_win(self):
        #check rows
        if self.check_rows() == True:
            return True
        #check columns
        elif self.check_columns()== True:
            return True
        #check diagonals
        elif self.check_diag()== True:
            return True
        else:
            return False

    #checking if the game is a tie
    def check_tie(self):
        for i in range(9):
            if self.board[i]=="-":
                return False
                break
        return True
    
    #check rows function
    def check_rows(self):
        #difining a variable like this gives a boolean
        row0= self.board[0]==self.board[1]==self.board[2]!="-"
        row1= self.board[3]==self.board[4]==self.board[5]!="-"
        row2= self.board[6]==self.board[7]==self.board[8]!="-" 
        if row0 or row2 or row1 == True:
            return True 
        else:
            return False     
    #check columns function
    def check_columns(self):
        #difining a variable like this gives a boolean
        column0= self.board[0]==self.board[3]==self.board[6]!="-"
        column1= self.board[1]==self.board[4]==self.board[7]!="-"
        column2= self.board[2]==self.board[5]==self.board[8]!="-" 
        if column0 or column2 or column1 == True:
            return True 
        else:
            return False     
    #check diagonals
    def check_diag(self):
        #difining a variable like this gives a boolean
        diag0= self.board[0]==self.board[4]==self.board[8]!="-"
        diag1= self.board[2]==self.board[4]==self.board[6]!="-"
        if diag0 or diag1 == True:
            return True 
        else:
            return False   

    # placing pieces
    def place_piece(self):
        while True:
            position = int(input("choose position: "))
            if position>=1 and position<=9:
                if self.board[position-1]!="-":
                    print("Position already taken choose again")
                    continue
                break
            else:
                print("plese type between 1-9")
                continue
        self.board[position-1]= self.player
        self.display()
        
    # flipping player
    def flip_player(self):
        if self.player=="X":
            self.player="O"
        elif self.player=="O":
            self.player="X"
        else :
            return

    #declare winer and end game
    def game_state(self):
        if self.check_win()==True:
            self.winner=self.player + " is the winner"
            return True
        elif self.check_tie()== True:
            self.winner="TIE"
            return True
        else:
            return False

    # run game
    def run_game(self):
        print(" x plays first ")
        self.display()
        while self.global_var==False:
            self.place_piece()
            self.global_var= self.game_state()
            if self.global_var==True:
                break
            self.flip_player()
        print(self.winner)

game = tic_tac_toe()
game.run_game()