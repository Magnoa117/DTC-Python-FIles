#Component 01_Quiz_FrameworkV2 - Creating GUI framework design (for Questions)

from tkinter import *
from functools import partial

class Quiz:
    def __init__(self):
        print("testing")

        #Background design

        background_color = "light blue"

        #Question frame
        self.quiz_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=80, padx=80)
        self.quiz_frame.grid()

        #Frame Heading (row 0)
        self.temp_quiz_label = Label(self.quiz_frame,
                                          text="Question One:",
                                          font=("", "18", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_quiz_label.grid(row=0)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Minecraft quiz")
    something = Quiz()
    root.mainloop()