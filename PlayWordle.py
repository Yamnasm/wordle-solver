from tkinter import Tk, Label
import tkinter.font as tkFont
import wordle

class WordleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle")
        self.master.geometry("200x200")
        self.master.bind("<Key>", self.keypress)
        self.font = tkFont.Font(family="Helvetica")
        self.label = []
        self.letter_num = 0
        self.word_size = 5

        i = 0
        for r in range(6):
            for c in range(5):
                self.label.append(Label(master, text=i + 1))
                self.label[i].grid(row=r, column=c, sticky = "NSEW")
                i += 1
        master.columnconfigure(tuple(range(5)), weight=1)
        master.rowconfigure(tuple(range(6)), weight=1)

    def trigger(self, event):
        print("something happened")
    
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

        if event.keycode == 13:
            kp = "ENTER"
        elif event.keycode == 8:
            kp = "BACKSPACE"
        else:
            kp = event.char

        self.label[self.letter_num]["text"] = kp
        self.letter_num += 1
        
        print(f"Pressed {kp}: {event.keycode}.")

def main():
    root = Tk()
    WordleGame = WordleGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()