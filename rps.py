from random import randrange
from time import sleep

class RPS():
    def __init__(self):
        self.choices = ['r','s','p']
        self.score = [0,0]
        while True:  
            try:
                self.rounds = int(input("How many rounds do you wish to play: "))
                break
            except:
                print("number of rounds must be an integer, retry")
        for i in range(self.rounds):
            j = True
            while j:
                temp = self.score.copy()
                "type r, p or s into the command line in ..."
                sleep(1)
                print(3)
                sleep(1)
                print(2)
                sleep(1)
                print(1)
                k = True
                while k:
                    user_choice = (input("nowww  !!!!: "))
                    if user_choice in self.choices:
                        k = False
                    else:
                        print("input must be 'r', 'p', or 's'")
                computer_choice = self.choices[randrange(0,3)]
                self.winner(user_choice, computer_choice)
                if self.score == temp:
                    print("Draw, retry")
                    continue
                print("score is now: ",self.score[0],"-",self.score[1])
                j = False
    def winner(self, user, computer):
            for i in range(3):
                if user == self.choices[i] and computer == self.choices[(i+1) % 3]:
                    print("User Wins Round")
                    self.score[0] += 1
                elif computer == self.choices[i] and user == self.choices[(i+1) % 3]:
                    print("Computer Wins Round")
                    self.score[1] += 1

        


