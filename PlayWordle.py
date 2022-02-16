from tkinter import Tk, Label
import tkinter.font as tkFont
import wordle

class WordleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle")
        self.master.geometry("200x200")
        self.master.bind("<Key>", self.keypress)
        self.label = []
        self.letter_num = 0
        self.word_size = 5
        self.wordle_game = wordle.WordleGame()
        self.current_word = ""

        i = 0
        for r in range(6):
            for c in range(5):
                self.label.append(Label(master))
                self.label[i].grid(row=r, column=c, sticky = "NSEW")
                i += 1
        master.columnconfigure(tuple(range(5)), weight=1)
        master.rowconfigure(tuple(range(6)), weight=1)
    
    def valid_key(self, keycode):
        if keycode >= 65 and keycode <= 90:
            return True
        elif keycode == 13 or keycode == 8:
            return True
        return False

    def keypress(self, event):
        if self.letter_num == len(self.label):
            return
        if self.valid_key(event.keycode) == False:
            return

        if event.keycode == 13: #ENTER
            print(f"Submitted: {self.current_word}")
            self.current_word = ""
            return
        elif event.keycode == 8: #BACKSPACE
            if len(self.current_word) == 0:
                return
            self.current_word = self.current_word[:-1]
            self.letter_num -= 1
            self.label[self.letter_num]["text"] = ""
            print(f"Current word: {self.current_word}.")
            return
        else:
            key_pressed = event.char

        if len(self.current_word) == 5:
            return
        
        self.current_word += key_pressed
        self.label[self.letter_num]["text"] = key_pressed.upper()
        self.letter_num += 1
        
        #print(f"Pressed {kp}: {event.keycode}.")
        print(f"Current word: {self.current_word}.")

    def hit_enter():
        pass

def main():
    root = Tk()
    WordleGame = WordleGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()