#Component 01_Quiz FrameworkV1 - Creating GUI framework design

from tkinter import *
from functools import partial

class Quiz:
    def __init__(self):
        print("testing")
 
        #Background design

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

        # Start Quiz button(row 1)
        self.help_button = Button(self.quiz_frame, text="Start Quiz",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,)
        self.help_button.grid(row=1)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Minecraft quiz")
    something = Quiz()
    root.mainloop()