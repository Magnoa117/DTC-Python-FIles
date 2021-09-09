from tkinter import *
from functools import partial
import re

class QuizExport:
    def __init__(self):
        #List to store user quiz result
        # says "10" for testing purposes
        self.user_results_list = ["10"] #User results go here
        
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

        # set up quiz results GUI
        self.how_heading = Label(self.history_frame, text="Quiz Results",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        #Quiz results GUI heading
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

        #user data
        history_string = ("10")#says "10" for testing purposes

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

        #Warning label text
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
            f.write("You Scored {}/10!")

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
    something = QuizExport()
    root.mainloop()