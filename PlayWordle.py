from tkinter import Tk, Canvas, messagebox
import wordle

GREY = "#787C7E"
YELLOW = "#C9B458"
GREEN = "#6AAA64"

class WordleGUI:
    def __init__(self):

        #window init
        self.window = Tk()
        self.window.title("Wordle")
        self.window.resizable(False, False)
        self.window.bind("<Key>", self.keypress)
        self.win_size = 400

        # canvas init
        self.canvas = Canvas(
            self.window,
            width=self.win_size,
            height=self.win_size
        )
        self.canvas.pack()
        self.letter_bg_obj = []
        self.create_letter_background()
        self.create_grid_lines()
        self.letter_text_obj = []
        
        # wordle objects / variables
        self.wordle_game = wordle.WordleGame()
        self.current_word = ""
        self.letter_num = 0

    def play(self):
        self.window.mainloop()

    def create_grid_lines(self):
        for i in range(4): # vertical
            self.canvas.create_line((i + 1) * self.win_size / 5, 0, (i + 1) * self.win_size / 5, self.win_size)
        for i in range(4): # horizontal
            self.canvas.create_line(0, (i + 1) * self.win_size / 5, self.win_size, (i + 1) * self.win_size / 5)

    def create_letter_background(self):
        for i in range(25):
            x0 = 0 + (80 * (i % 5))
            y0 = 0 + (80 * (i // 5))
            x1 = 80 + (80 * (i % 5))
            y1 = 80 + (80 * (i // 5))
            self.letter_bg_obj.append(
                self.canvas.create_rectangle(
                    x0, y0, x1, y1, fill="white"
                )
            )

    def valid_key(self, keycode):
        if keycode >= 65 and keycode <= 90:
            return True
        elif keycode == 13 or keycode == 8: #enter or backspace
            return True
        return False

    def keypress(self, event):

        if self.valid_key(event.keycode) == False:
            return

        if event.keycode == 13: #ENTER
            if len(self.current_word) != 5:
                return
            print(f"Submitted: {self.current_word}")

            result = self.wordle_game.next_turn(self.current_word)
            self.current_word = ""
            if result == None:
                print("Invalid Word.")
                messagebox.showerror(title="Invalid Word", message="Invalid Word")
                for _ in range(5):
                    self.letter_num -= 1
                    self.canvas.delete(self.letter_text_obj[self.letter_num])
                    del self.letter_text_obj[-1]
                return
            self.display_results(result)
            return
        elif event.keycode == 8: #BACKSPACE
            if len(self.current_word) == 0:
                return
            self.current_word = self.current_word[:-1]
            self.letter_num -= 1
            self.canvas.delete(self.letter_text_obj[self.letter_num])
            del self.letter_text_obj[-1]
            return
        elif self.letter_num >= 25: # max letters
            return

        else: #all other (legal) letters
            key_pressed = event.char

        if len(self.current_word) == 5:
            return
        
        self.current_word += key_pressed
        self.letter_text_obj.append(self.show_letter_on_canvas(key_pressed))
        self.letter_num += 1

    def show_letter_on_canvas(self, letter):
        text_top_offset = 40 + (80 * (self.letter_num % 5))
        text_left_offset = 40 + (80 * (self.letter_num // 5))
        return self.canvas.create_text(
            text_top_offset,
            text_left_offset,
            text=letter.upper(),
            fill="black",
            font=('Helvetica 50 bold'))

    def display_results(self, results_dict):
        cell = self.letter_num - 5        
        for letter in results_dict.values():
            if letter["hard"]:
                self.canvas.itemconfig(self.letter_bg_obj[cell], fill=GREEN)
            elif letter["soft"]:
                self.canvas.itemconfig(self.letter_bg_obj[cell], fill=YELLOW)
            else:
                self.canvas.itemconfig(self.letter_bg_obj[cell], fill=GREY)
            cell += 1

def main():
    game = WordleGUI()
    game.play()

if __name__ == '__main__':
    main()