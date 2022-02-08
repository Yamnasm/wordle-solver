from tkinter import Tk, Label
import tkinter.font as tkFont


class WordleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle")
        self.master.geometry("200x200")
        self.master.bind("<Configure>", self.font_resize)
        self.font = tkFont.Font(family="Helvetica")
        self.label = []

        i = 0
        for r in range(6):
            for c in range(5):
                self.label.append(Label(master, text=i + 1))
                self.label[i].grid(row=r, column=c, sticky = "NSEW")
                i += 1
        master.columnconfigure(tuple(range(5)), weight=1)
        master.rowconfigure(tuple(range(6)), weight=1)

    def font_resize(self, event=None):
        for lbl in self.label:
            x = lbl.winfo_width()
            y = lbl.winfo_height()
            if x < y:
                lbl.config(self.font.configure(size = x-10))
            else:
                lbl.config(self.font.configure(size = y-10))

def main():
    root = Tk()
    WordleGame = WordleGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()