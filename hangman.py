from random import randrange

reader = open("C:\\Users\\tomco\\Documents\\PythonWork\\Games\\words.txt","rt")
words = []
for word in reader.readlines():
    words.append(word.lower().strip())
reader.close()

hangmen =["  +---+  \n  |   |  \n  O   |  \n /|\  |  \n / \  |  \n      |  \n=========", \
        "  +---+  \n  |   |  \n  O   |  \n /|\  |  \n /    |  \n      |  \n=========", \
        "  +---+  \n  |   |  \n  O   |  \n /|\  |  \n      |  \n      |  \n=========", \
        "  +---+  \n  |   |  \n  O   |  \n /|   |  \n      |  \n      |  \n=========", \
        "  +---+  \n  |   |  \n  O   |  \n  |   |  \n      |  \n      |  \n=========", \
        "  +---+  \n  |   |  \n  O   |  \n      |  \n      |  \n      |  \n=========", \
        "  +---+  \n  |   |  \n      |  \n      |  \n      |  \n      |  \n=========", \
        "  +---+  \n      |  \n      |  \n      |  \n      |  \n      |  \n=========", \
        "         \n      |  \n      |  \n      |  \n      |  \n      |  \n=========", \
        "         \n         \n      |  \n      |  \n      |  \n      |  \n=========", \
        "         \n         \n         \n      |  \n      |  \n      |  \n=========", \
        "         \n         \n         \n         \n      |  \n      |  \n=========", \
        "         \n         \n         \n         \n         \n      |  \n=========", \
        "         \n         \n         \n         \n         \n         \n========="]




class GameOver(Exception):
    pass



class HangError(Exception):
    pass



class HangmanGame():
    def __init__(self, rounds = 1):
        try: 
            try:
                self.rounds = int(rounds)
            except:
                print("enter an integer number of rounds")
            for r in range(self.rounds):
                print("round ",str(r+1),"/",self.rounds,sep = '')
                round = HangmanRound()
                print(round)
                while '_' in round.display:
                    round.turn()
                    if round.mistake_count >= len(hangmen) - 1:
                        raise GameOver
                print("word guessed, congrats")
            print("Game Finished :)")
        except GameOver:
            retry = input("Game Over: press enter to try again")
            if retry == '':
                self.__init__(self.rounds)
            else:
                print("Very Well, have a nice day :)")



class HangmanRound():
    wordbank = ["a"]
    def __init__(self):
        self.word = words[randrange(0,854)]
        self.guesses = []
        self.display ='_'
        self.wrong_guesses = []
        self.mistake_count = 0
    def __str__(self):
        string = self.word.split()
        display = ''
        lengths = "("
        for i in string:
            for j in i:
                if j in self.guesses:
                    display += j
                else:
                    display += '_'
            display += ' '
            lengths += str(len(i))
            if i != string[len(string)-1]:
                lengths += ","
        lengths += ")"
        hanger_index = len(hangmen) - self.mistake_count - 1
        hanger = hangmen[hanger_index]
        self.display = display
        return display +'   '+lengths+"\n"+hanger
    def guess(self):
        while True:
            try:
                char = (input("guess a letter: ")).lower()
                if len(char) != 1:
                    raise HangError("not a single character, retry")
                elif ord(char) < 97 or ord(char) > 122:
                    raise HangError("not a letter retry")
                if char in self.word:
                    if char not in self.guesses:
                        self.guesses.append(char)
                    else:
                        print("this letter was already guessed")
                if char not in self.word:
                    if char not in self.wrong_guesses:
                        self.wrong_guesses.append(char)
                        self.mistake_count += 1
                    else:
                        print("this letter was already guessed")
                break
            except HangError as e:
                print(e)
    def turn(self):
        self.guess()
        print(self)

