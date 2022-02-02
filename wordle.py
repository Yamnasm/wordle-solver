import random
import pdb
#pdb.set_trace()

class WordleGame():
    def __init__(self):
        self.words = self.__get_wordlist()
        self.goal_word = random.choice(self.words)

        self.guess = ""
        self.guesslist = self.__get_guesslist()

        self.guesses = 6
        self.alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

    def __get_wordlist(self):
        wordlist = []
        with open("wordlist.txt", "r") as data:
            lines = data.readlines()
            for l in lines:
                wordlist.append(l.rstrip())
        return wordlist

    def __get_guesslist(self):
        guesslist = []
        with open("validguesses.txt", "r") as data:
            lines = data.readlines()
            for l in lines:
                guesslist.append(l.rstrip())
        return guesslist

    def __is_guess_valid(self):
        if self.guess in self.words or self.guess in self.guesslist:
            return True
        else:
            return False

    def __remove_letters(self):
        for letter in self.guess:
            if letter in self.alphabet:
                self.alphabet.remove(letter)
    
    def __guess_result_dict(self):
        result_dict = {}
        for i, letter in enumerate(self.guess):
            result_dict[i + 1] = {"letter": letter}
            if letter == self.goal_word[i]:
                result_dict[i + 1]["hard"] = True
            else:
                result_dict[i + 1]["hard"] = False
            if letter in self.goal_word:
                result_dict[i + 1]["soft"] = True
            else:
                result_dict[i + 1]["soft"] = False
        return result_dict

    def next_turn(self, userguess):
        self.guess = userguess
        if self.__is_guess_valid() == False:
            return None

        self.__remove_letters()
        self.guesses -= 1

        return self.__guess_result_dict()

def print_guess_result(guess_dict):
    guess_string = "".join([l["letter"] for l in guess_dict.values()])
    guess_string += "\n"
    for letter in guess_dict.values():
        if letter["hard"]:
            guess_string += "^"
        elif letter["soft"]:
            guess_string += "~"
        else:
            guess_string += "?"
    return guess_string

def main():
    game = WordleGame()
    while game.guesses > 0:
        user_guess = input("Make Guess: ").lower()
        result = game.next_turn(user_guess)
        if result == None:
            print("Invalid word.")
            continue
        print("".join(game.alphabet))
        if user_guess == game.goal_word:
            print("CORRECT WORD!")
            break
        print(print_guess_result(result))
    if game.guesses == 0:
        print("YOU LOSE")
        print(game.goal_word)

if __name__ == "__main__":
    main()