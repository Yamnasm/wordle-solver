import random

class wordle_game():
    def __init__(self):
        self.words = self.get_wordlist()
        self.goal_word = random.choice(self.words)

        self.guesses = 6
        self.alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

    def get_wordlist(self):
        wordlist = []
        with open("wordlist.txt", "r") as data:
            lines = data.readlines()
            for l in lines:
                wordlist.append(l.rstrip())
        return wordlist

    def make_guess(self):
        guess = self.is_guess_valid()
        self.check_guess(guess)

    def is_guess_valid(self):
        guess = input("Make a guess: ").lower()
        if len(guess) == 5:
            self.remove_letters(guess)
            return guess
        self.is_guess_valid()
    
    def check_guess(self, guess):
        if guess == self.goal_word:
            print("Correct word!")
            return
        result_dict = {}
        for i, letter in enumerate(guess):
            result_dict[i + 1] = {"letter": letter}
            if letter == self.goal_word[i]:
                result_dict[i + 1]["hard"] = True
            else:
                result_dict[i + 1]["hard"] = False
            if letter in self.goal_word:
                result_dict[i + 1]["soft"] = True
            else:
                result_dict[i + 1]["soft"] = False
        self.print_guess_result(result_dict)

    def print_guess_result(self, guess_dict):
        print("".join([l["letter"] for l in guess_dict.values()]))
        guess_string = ""
        for letter in guess_dict.values():
            if letter["hard"]:
                guess_string += "^"
            elif letter["soft"]:
                guess_string += "~"
            else:
                guess_string += "?"
        print(guess_string)

    def remove_letters(self, guess):
        for letter in guess:
            if letter in self.alphabet:
                self.alphabet.remove(letter)
        print("".join(self.alphabet))

    def start_game(self):
        print("?" * len(self.goal_word))
        while self.guesses > 0:
            self.make_guess()
            self.guesses -= 1
            print(f"guesses left: {self.guesses}")
        print(f"Failed. The word was {self.goal_word}")

def main():
    game = wordle_game()
    game.start_game()

if __name__ == "__main__":
    main()