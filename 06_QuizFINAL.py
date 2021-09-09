from tkinter import *
import random
from functools import partial
import sys
import os
import re

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
                                pady=45, padx=20)
        self.quiz_frame.grid()

        self.quiz_menu = Frame(self.quiz_frame,
                               bg="dark blue")
        self.quiz_menu.grid()

        self.quiz_title = Label(self.quiz_frame,
                                text="Minecraft Quiz",
                                font=("Arial", "30", "bold"),
                                bg="dark blue")
        self.quiz_title.grid(row=0)

        #Starts Quiz Questions
        self.start_button = Button(self.quiz_frame, text="Start Quiz",
                                   font=("Arial", "14"),
                                   padx=10, pady=10,
                                   command=self.Quiz_Questions_list)
        self.start_button.grid(row=1)

        #Quit Button
        self.quiz_quit_button = Button(self.quiz_frame, text="Quit",
                                       font=("Arial", "14"),
                                       padx=10, pady=10,
                                       command=self.quiz_quit)
        self.quiz_quit_button.grid(row=2)

    #Terminates root (quits main menu GUI)
    def quiz_quit(self):
        root.destroy()

    # Quiz Questions start
    def Quiz_Questions_list(self):
        print("You started quiz")
        Quiz_Questions_list(self)


class Quiz_Questions_list:

    def __init__(self, partner):
        #Function will update the GUI for the given questions
        def quiz_continue():
            global quiz_number
            if quiz_number < 9:
                quiz_number += 1
                question_prompt[quiz_number]()
                self.question_title.configure(text=quiz_Heading)
                self.question_heading.configure(text="Minecraft Quiz")
                self.quiz_answer_btn1.configure(text=quiz_Answers[0])
                self.quiz_answer_btn2.configure(text=quiz_Answers[1])
                self.quiz_answer_btn3.configure(text=quiz_Answers[2])
                self.quiz_answer_btn4.configure(text=quiz_Answers[3])
                self.quiz_answer_btn1["state"] = NORMAL
                self.quiz_answer_btn2["state"] = NORMAL
                self.quiz_answer_btn3["state"] = NORMAL
                self.quiz_answer_btn4["state"] = NORMAL
                self.quiz_answer_btn1.configure()
                self.quiz_answer_btn2.configure()
                self.quiz_answer_btn3.configure()
                self.quiz_answer_btn4.configure()
                self.quiz_continue_button.grid_forget()
            # Terminates the quiz and opens results window
            elif quiz_number >= 9:
                QuizExport()
                # Closes Minecraft Quiz
                self.start_box.destroy()

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
        self.user_results_list = [] #User results go here

        self.start_box = Toplevel(width=300, height=300,
                                  bg="light blue", pady=10)
        self.start_box.grid()

        self.start_box.protocol('WM_DELETE_WINDOW', partial(self.close_start,
                                                            partner))
        partner.start_button.config(state=DISABLED)

        #Quiz Heading
        self.question_title = Label(self.start_box,
                                    text=quiz_Heading,
                                    font=("Arial", "20", "italic"),
                                    bg="light blue",
                                    pady=10, padx=10)
        self.question_title.grid(row=1, sticky='N')

        self.question_heading = Label(self.start_box,
                                      text="Minecraft Quiz",
                                      font=("Arial", "30", "bold"),
                                      bg="light blue",
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
                                           font=("Arial", "15"),
                                           bg="white", command=quiz_continue)
        self.quiz_continue_button.grid(row=8)

        self.dismiss_btn = Button(self.start_box, text="Exit",
                                  width=10, bg="orange", font=("Arial", "10", "bold"),
                                  command=partial(self.close_start, partner))
        self.dismiss_btn.grid(row=9, sticky="W",
                              pady=10,
                              padx=10)

        #Continue button is locked until it is needed again
        self.quiz_continue_button.grid_forget()


    def close_start(self, partner):
        ##Restarts the quiz
        partner.start_button.config(state=NORMAL)
        self.start_box.destroy()
        python = sys.executable
        os.execl(python, python, *sys.argv)
        print("You closed the quiz")
        

class QuizExport:
    def __init__(self):
        #List to store user quiz result
        self.user_results_list = [quiz_score] #User results go here
        
        #Results main screen gui
        self.QuizExport_frame = Toplevel(width=300, height=300,
                                      bg="light blue", pady=10)
        self.QuizExport_frame.grid()

        #Minecraft Quiz results heading
        self.temp_QuizExport_label = Label(self.QuizExport_frame,
                                           text="Minecraft Quiz Results",
                                           font=("Arial", "16", "bold"),
                                           bg="light blue",
                                           padx=10, pady=10)
        self.temp_QuizExport_label.grid(row=0)

        #Quick description of window
        self.export_desc = Label(self.QuizExport_frame,
                                 text="You have finished the quiz\n"
                                      "click (View Results) to\n"
                                      "see your overall results!",
                                 font=("Arial", "16"),
                                 bg="light blue",
                                 padx=10, pady=10)
        self.export_desc.grid(row=1)

        #View results button
        self.history_button = Button(self.QuizExport_frame, text="View Results",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     command=lambda: self.history("you scored{}/10".format(self.user_results_list)))
        self.history_button.grid(row=2)

    def history(self, quiz_history):
        History(self, quiz_history)


class History:
    def __init__(self, partner, quiz_history):
        background = "#a9ef99"  # pale green

        #locks view results button
        partner.history_button.config(state=DISABLED)

        #sets up child window
        self.history_box = Toplevel()

        #unlocks history button when locked
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,
                                                              partner))

        # set up GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        #Quiz results Label
        self.how_heading = Label(self.history_frame, text="Quiz Results",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        #Quiz text label
        self.history_text = Label(self.history_frame,
                                  text="Here are your Minecraft Quiz "
                                       "results. You can click on the "
                                       "export button to save this "
                                       "data to a text file if "
                                       "desired.",
                                  font="arial 10 italic", wrap=250,
                                  justify=LEFT,
                                  bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        #quiz score results stored here
        history_string = (quiz_score)

        self.history_text.config(text="Here are your Minecraft Quiz "
                                      "results. You can click on the "
                                      "export button to save this "
                                      "data to a text file if "
                                      "desired.\n"
                                      "\nYour Final Result Was:")

            #Label to display quiz result to user
        self.quiz_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.quiz_label.grid(row=2)

        # Export / Dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)
        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="arial 12 bold",
                                    command=lambda: self.export(quiz_history))
        self.export_button.grid(row=0, column=0)
        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_history,
                                                     partner))

        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        #Unlocks view results button
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, quiz_history):
        Export(self, quiz_history)


class Export:
    def __init__(self, partner, quiz_history):
        self.quiz_history = quiz_history
        background = "#a9ef99"  # pale green

        #Locks the export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes help and releases help button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export/Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename in the box below "
                                      "and press the Save button to save "
                                      "your quiz results to a text "
                                      "file", justify=LEFT,
                                 width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # warning text (label, row 2)
        self.export_text = Label(self.export_frame,
                                 text="If a filename you enter below "
                                      "already exists, its contents will "
                                      "be replaced with your quiz "
                                      "results", justify=LEFT,
                                 bg="#ffafaf",  # pink
                                 fg="maroon", font="Arial 10 italic",
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error message labels (row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / cancel frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=4, pady=10)

        # Save / cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(
                                      partner)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export,
                                                    partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner):
        # Regular expressoin to check file name can be Upper or lower case letters,
        global problem
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":  # describ problem
            # display error message
            self.save_error_label.config(text="\n\n\nInvalid filename - {}"
                                         .format(problem))
            #turns background red
            self.filename_entry.config(bg="red")

        else:
            # if there are no errors, generate text file and the close
            # if dialogue add .txt suffix!

            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new Line at end of each item
            f.write("You Scored {}/10!".format(quiz_score))


            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # puts help button back to normal state
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Minecraft quiz")
    something = Quiz_menu()
    random.shuffle(question_prompt)
    question_prompt[quiz_number]()
    root.mainloop()