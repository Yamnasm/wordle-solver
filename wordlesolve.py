import re

def import_wordlist():
    wordlist = []
    with open("wordlist.txt", "r") as data:
        lines = data.readlines()
        for l in lines:
            wordlist.append(l.rstrip())
    return wordlist

def listsearch(wordlist):
    r = re.compile("n.[^w]l.")
    newlist = list(filter(r.match, wordlist))
    return newlist

def main():
    wordlist = import_wordlist()
    print(listsearch(wordlist))

if __name__ == "__main__":
    main()