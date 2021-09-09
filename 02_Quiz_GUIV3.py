#Component 02_Quiz_GUIV3 - GUI constructed from 01_Quiz_Framework.

from tkinter import *
from functools import partial

class Quiz:
    def __init__(self):
        print("testing")

        #Background color

        background_color = "dark blue"

        #Quiz Main Screen GUI
        self.quiz_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=80, padx = 80)
        self.quiz_frame.grid()

        # Minecraft Heading (row 0)
        self.temp_quiz_label = Label(self.quiz_frame,
                                          text="Minecraft quiz",
                                          font=("", "24", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_quiz_label.grid(row=0)

        # Start quiz button (row 1)
        self.start_button = Button(self.quiz_frame, text="Start Quiz",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                  command=self.start)
        self.start_button.grid(row=1)

    def start(self):
        print("You started the quiz")
        get_start = start(self)
        get_start.start_text.configure(text="First Question Here")


class start:
    def __init__(self, partner):
        background = "light blue"

        #disable start button
        partner.start_button.config(state=DISABLED)

        # sets up new window (Question window)
        self.start_box = Toplevel()

        #when user exits frame unlocks the start button
        self.start_box.protocol('WM_DELETE_WINDOW', partial(self.close_start,
                                                           partner))

        # set up GUI frame
        self.start_frame = Frame(self.start_box, width=300, bg=background)
        self.start_frame.grid()

        # set up start heading (row 0)
        self.how_heading = Label(self.start_frame, text="Question One",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # start text (label, row 1)
        self.start_text = Label(self.start_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.start_text.grid(row=1)

        #Dismiss button (row 2)
        self.dismiss_btn = Button(self.start_frame, text="Close Quiz",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_start, partner))

        self.dismiss_btn.grid(row=2, pady=10)

    def close_start(self, partner):
        #puts start button back to normal state
        partner.start_button.config(state=NORMAL)
        self.start_box.destroy()
        print("You closed the quiz")



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Minecraft quiz")
    something = Quiz()
    root.mainloop()