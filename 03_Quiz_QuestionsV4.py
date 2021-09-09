#Component 03_Quiz_QuestionsV4 - Creating random generated questions from list of functions

import random
from Question import Question

#Question list
question_prompts = [
    "Not sleeping consecutively for 3 days spawns which mob? (1)",
    "What is the rarest ore? (2)",
    "What color are Creepers? (3)",
    "What mob can pick up blocks? (4)",
    "What mob sits on chests? (5)",
    "What mob can trade with you? (6)",
    "What feature was removed from the game? (7)",
    "What is the strongest ore (8)",
    "What ore can be used for building complicated machines? (9)",
    "What block takes the longest to break? (10)"
]

#List of a function list
question_number_list = [
Question(question_prompts[0], "1"),
Question(question_prompts[1], "2"),
Question(question_prompts[2], "3"),
Question(question_prompts[3], "4"),
Question(question_prompts[4], "5"),
Question(question_prompts[5], "6"),
Question(question_prompts[6], "7"),
Question(question_prompts[7], "8"),
Question(question_prompts[8], "9"),
Question(question_prompts[9], "10"),
]

#Generates random order of the questions
random.shuffle(question_number_list)

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

#main routine
run_test(question_number_list)
    


