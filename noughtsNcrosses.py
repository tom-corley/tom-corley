from random import randrange



class XOXOException(Exception):
    pass



class XOXO: 
    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        print("Lets Play!")
        print("Computer Makes First Move: ")
        self.board[1][1] = "X"
        print(self.__str__())
        users_turn = True
        while self.victory_for("X") == False and self.victory_for("O") == False:
            if (len(self.make_list_of_free_fields()) == 0):
                print("Stalemate !")
                break
            if users_turn:
                self.enter_move()
                print(self)
                users_turn = False
            else:
                self.draw_move()
                print(self)
                users_turn = True
        if self.victory_for("O"):
            print("Congrats, you win!")
        elif self.victory_for("X"):
            print("Better luck next time, the computer bested you.")

    def __str__(self):
        stringer = "+-------+-------+-------+\n|\t|\t|\t|\n" +\
            "|   "+self.board[0][0]+"   |   "+self.board[0][1]+"   |   "+self.board[0][2]+\
            "   |\n"+ "|\t|\t|\t|\n"+\
            "+-------+-------+-------+\n|\t|\t|\t|\n"+\
            "|   "+self.board[1][0]+"   |   "+self.board[1][1]+"   |   "+self.board[1][2]+"   |\n"+\
            "|\t|\t|\t|\n"+\
            "+-------+-------+-------+\n|\t|\t|\t|\n"+\
            "|   "+self.board[2][0]+"   |   "+self.board[2][1]+"   |   "+self.board[2][2]+"   |\n"+\
            "|\t|\t|\t|\n"+"+-------+-------+-------+"
        return stringer
        # The function accepts one parameter containing the self.board's current status
        # and prints it out to the console.

    def make_list_of_free_fields(self):
        free_squares = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    free_squares.append((i,j))
        return free_squares
        # The function browses the self.board and builds a list of all the free squares; 
        # the list consists of tuples, while each tuple is a pair of row and column numbers.

    def enter_move(self):
        while True:
            print("Time to make your move: ")
            try:
                user_row = int(input("Enter a row: ")) - 1
                user_column = int(input("Enter a column: ")) - 1
                if user_row > 3 or user_column > 3 :
                    raise Exception
                if (user_row,user_column) in self.make_list_of_free_fields():
                    self.board[user_row][user_column] = "O"
                    break
                else:
                    print("Space already occupied, try again")
            except:
                print("row and column must be an integer between 1 and 3")
        # The function accepts the self.board current status, asks the user about their move, 
        # checks the input and updates the self.board according to the user's decision.


    def victory_for(self, sign):
        # checking diagonals
        if self.board[0][0] == self.board [1][1] and self.board[1][1] == self.board[2][2] \
            and self.board[2][2] == sign:
            return True
        if self.board[0][2] == self.board [1][1] and self.board[1][1] == self.board[2][0] \
            and self.board[2][0] == sign:
            return True
        # checking rows
        if self.board[0][0] == self.board [0][1] and self.board[0][1] == self.board[0][2] \
            and self.board[0][2] == sign:
            return True
        if self.board[1][0] == self.board [1][1] and self.board[1][1] == self.board[1][2] \
            and self.board[1][2] == sign:
            return True
        if self.board[2][0] == self.board [2][1] and self.board[2][1] == self.board[2][2] \
            and self.board[2][2] == sign:
            return True
        # checking columns
        if self.board[0][0] == self.board [1][0] and self.board[1][0] == self.board[2][0] \
            and self.board[2][0] == sign:
            return True
        if self.board[0][1] == self.board [1][1] and self.board[1][1] == self.board[2][1] \
            and self.board[2][1] == sign:
            return True
        if self.board[0][2] == self.board [1][2] and self.board[1][2] == self.board[2][2] \
            and self.board[2][2] == sign:
            return True
        else:
            return False
        # The function analyzes the self.board status in order to check if 
        # the player using 'O's or 'X's has won the game


    def draw_move(self):
        print("Computer's Move.")
        moveset = self.make_list_of_free_fields()
        while True:
            rand_row = randrange(0,3,1)
            rand_col = randrange(0,3,1)
            move = (rand_row,rand_col)
            if move in moveset:
                self.board[move[0]][move[1]] = "X"
                break
            else:
                continue
        # The function draws the computer's move and updates the self.board.