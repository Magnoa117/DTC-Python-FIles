#Component 04_Quiz_ConstructedV4 - Generating functions of questions
#Takes GUI from 02_Quiz_GUIV3 and includes constructed and functional questions GUI

from tkinter import *
import random
from functools import partial
import sys
import os

#Variables are defined here
quiz_number = 0
quiz_score = 0

#List of Functions here
def Question1():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("Not sleeping consecutively for\nthree days spawns which unique mob?")
    quiz_Answers = ["Phantom", "Enderman", "Zombies", "Slimes"]
    quiz_Outcome = ["Correct", "Incorrect", "Incorrect", "Incorrect"]

def Question2():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("What is the rarest ore?")
    quiz_Answers = ["Redstone", "Diamonds", "Netherite", "Emerald"]
    quiz_Outcome = ["Incorrect", "Incorrect", "Incorrect", "Correct"]

def Question3():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("What color are creepers?")
    quiz_Answers = ["Blue", "Green", "Yellow", "Red"]
    quiz_Outcome = ["Incorrect", "Correct", "Incorrect", "Incorrect"]

def Question4():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("What mob can pick up blocks?")
    quiz_Answers = ["Enderman", "Zombie", "Creeper", "Villager"]
    quiz_Outcome = ["Correct", "Incorrect", "Incorrect", "Incorrect"]

def Question5():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("What mob sits on chests?")
    quiz_Answers = ["Wolf", "Spider", "Cats", "Villager"]
    quiz_Outcome = ["Incorrect", "Incorrect", "Correct", "Incorrect"]

def Question6():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("What mob can trade with you?")
    quiz_Answers = ["Witch", "Enderman", "Zombie", "Villager"]
    quiz_Outcome = ["Incorrect", "Incorrect", "Incorrect", "Correct"]

def Question7():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("What feature was\nremoved from the game?")
    quiz_Answers = ["Sword Blocking", "Hunger bars", "Multiplayer", "Creative mode"]
    quiz_Outcome = ["Correct", "Incorrect", "Incorrect", "Incorrect"]


def Question8():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("What is the strongest ore?")
    quiz_Answers = ["Diamonds", "Iron", "Netherite", "Gold"]
    quiz_Outcome = ["Incorrect", "Incorrect", "Correct", "Incorrect"]

def Question9():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("What ore can be used to\ncreate complex machines?")
    quiz_Answers = ["Iron", "Redstone", "Lapis Lazuli", "Emerald"]
    quiz_Outcome = ["Incorrect", "Correct", "Incorrect", "Incorrect"]

def Question10():
    global quiz_Heading
    global quiz_Answers
    global quiz_Outcome
    quiz_Heading = ("What block takes\nthe longest to break?")
    quiz_Answers = ["Iron Block", "Diamond Block", "Obsidian", "Anvil"]
    quiz_Outcome = ["Incorrect", "Incorrect", "Correct", "Incorrect"]

#List of function lists
question_prompt = [
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7,
    Question8,
    Question9,
    Question10
]

class Quiz_menu:
    def __init__(self):

    #Quiz menu GUI
        self.quiz_frame = Frame(width=100, height=100,
                                bg="dark blue",
                                pady=150, padx=80)
        self.quiz_frame.grid()

        self.quiz_menu=Frame(self.quiz_frame,
                             bg="dark blue")
        self.quiz_menu.grid()

        self.quiz_title = Label(self.quiz_frame,
                                text="Minecraft Quiz",
                                font=("Arial", "30", "bold"),
                                bg= "dark blue")
        self.quiz_title.grid(row=0)


        #Starts Quiz Questions
        self.start_button = Button(self.quiz_frame, text="Start Quiz",
                                   font=("Arial", "14"),
                                   padx=10, pady=10,
                                   command=self.Quiz_Questions_list)
        self.start_button.grid(row=1)

    #Quiz Questions start
    def Quiz_Questions_list(self):
        print("You started quiz") #Testing purposes
        Quiz_Questions_list(self)

#Quiz Question GUI starts here:
class Quiz_Questions_list:
    def __init__(self, partner):
        #Function will update the GUI for the given questions
        def quiz_continue():
            global quiz_number
            if quiz_number < 9:
                quiz_number += 1
                #Printing the user's correct results for testing
                print(quiz_score)
                print("You pressed the next question")
                question_prompt[quiz_number]()
                self.question_title.configure(text=quiz_Heading)
                self.question_heading.configure(text="Minecraft Quiz")
                self.quiz_answer_btn1.configure(text=quiz_Answers[0])
                self.quiz_answer_btn2.configure(text=quiz_Answers[1])
                self.quiz_answer_btn3.configure(text=quiz_Answers[2])
                self.quiz_answer_btn4.configure(text=quiz_Answers[3])
                self.quiz_answer_btn1["state"]=NORMAL
                self.quiz_answer_btn2["state"]=NORMAL
                self.quiz_answer_btn3["state"]=NORMAL
                self.quiz_answer_btn4["state"]=NORMAL
                self.quiz_answer_btn1.configure()
                self.quiz_answer_btn2.configure()
                self.quiz_answer_btn3.configure()
                self.quiz_answer_btn4.configure()
                self.quiz_continue_button.grid_forget()
            #Stops updating questions after 10th questions
            #print user results after 10 questions
            elif quiz_number >= 9:
                print("you scored:",quiz_score,"/ 10") #Replace with class

        #Functions for quiz buttons
        #When clicked, the buttons respond
        def answer_btn1():
            if quiz_Outcome[0] == "Correct":
                global quiz_score
                quiz_score += 1
            button_feedback()

        def answer_btn2():
            if quiz_Outcome[1] == "Correct":
                global quiz_score
                quiz_score += 1
            button_feedback()

        def answer_btn3():
            if quiz_Outcome[2] == "Correct":
                global quiz_score
                quiz_score += 1
            button_feedback()

        def answer_btn4():
            if quiz_Outcome[3] == "Correct":
                global quiz_score
                quiz_score += 1
            button_feedback()

        #Function to disable buttons
        def button_feedback():
            #Buttons become disabled after user clicks a button
            self.quiz_answer_btn1["state"] = DISABLED
            self.quiz_answer_btn2["state"] = DISABLED
            self.quiz_answer_btn3["state"] = DISABLED
            self.quiz_answer_btn4["state"] = DISABLED

            #Continue button is unlocked
            self.quiz_continue_button.grid()

        #Quiz GUI
        self.start_box = Toplevel(width=300, height=300,
                                  bg="light blue", pady=10)
        self.start_box.grid()

        self.start_box.protocol('WM_DELETE_WINDOW',partial(self.close_start,
                                                           partner))
        partner.start_button.config(state=DISABLED)



        #Quiz Heading
        self.question_title = Label(self.start_box,
                                            text=quiz_Heading,
                                            font=("Arial", "20", "italic"),
                                            bg="light blue",
                                            pady=10, padx=10)
        self.question_title.grid(row=1,sticky='N')

        self.question_heading = Label(self.start_box,
                                      text="Minecraft Quiz",
                                      font=("Arial", "30", "bold"),
                                      bg ="light blue",
                                      pady=10, padx=10)
        self.question_heading.grid(row=0)


        #Buttons GUI
        self.quiz_answer_btn1 = Button(self.start_box, text=quiz_Answers[0],
                                      font=("Arial", "20"),
                                      bg="white",
                                      width=15, command=answer_btn1, disabledforeground="black")
        self.quiz_answer_btn1.grid(row=4)

        self.quiz_answer_btn2 = Button(self.start_box, text=quiz_Answers[1],
                                      font=("Arial", "20"),
                                      bg="white",
                                      width=15, command=answer_btn2, disabledforeground="black")
        self.quiz_answer_btn2.grid(row=5)

        self.quiz_answer_btn3 = Button(self.start_box, text=quiz_Answers[2],
                                      font=("Arial", "20"),
                                      bg="white",
                                      width=15, command=answer_btn3, disabledforeground="black")
        self.quiz_answer_btn3.grid(row=6)

        self.quiz_answer_btn4 = Button(self.start_box, text=quiz_Answers[3],
                                      font=("Arial", "20"),
                                      bg="white",
                                      width=15, command=answer_btn4, disabledforeground="black")
        self.quiz_answer_btn4.grid(row=7)

        #Continue button to proceed to next question
        self.quiz_continue_button = Button(self.start_box, text="Continue",
                                            font=("Arial","15"),
                                            bg="white", command=quiz_continue)
        self.quiz_continue_button.grid(row=8)

        self.dismiss_btn = Button(self.start_box, text="Close Quiz",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_start, partner))
        self.dismiss_btn.grid(row=9, sticky= "W",
                              pady =10,
                              padx = 10)


        #Continue button is locked until it is needed again
        self.quiz_continue_button.grid_forget()

    def close_start(self, partner):
        #Restarts the quiz
        partner.start_button.config(state=NORMAL)
        self.start_box.destroy()
        python = sys.executable
        os.execl(python, python, * sys.argv)
        print("You closed the quiz")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Minecraft quiz")
    something = Quiz_menu()
    random.shuffle(question_prompt)
    question_prompt[quiz_number]()
    root.mainloop()