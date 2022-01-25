import re

class Wordle_Solver:
    def __init__(self):
        self.alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

    def import_wordlist(self):
        wordlist = []
        with open("wordlist.txt", "r") as data:
            lines = data.readlines()
            for l in lines:
                wordlist.append(l.rstrip())
        return wordlist

def regexbuilder(allowed_letters, soft_letters, hard_letters):
    #fuck me I guess: why do I make things so hard for myself
    pass

def listsearch(wordlist):
    r = re.compile("n.[^w]l.")
    newlist = list(filter(r.match, wordlist))
    return newlist

def main():
    solver = Wordle_Solver()
    print(solver.alphabet)

    wordlist = solver.import_wordlist()
    print(listsearch(wordlist))

if __name__ == "__main__":
    main()
