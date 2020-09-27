# A simple program that functions as an elementary
# level math quiz that young students could tak online.


# import question class
from Question import Question


# String array of quiz questions. More can be added at any time.
quiz_questions = [
    "3x = 21. Find x.\n(a) 7\n(b) 6\n(c) 5\n(d) 4\n\n",
    "5x + 2 = 17. Find x.\n(a) 2\n(b) 3\n(c) 4\n(d) 5\n\n",
    "4x - 5 = 15. Find x.\n(a) 3\n(b) 4\n(c) 5\n(d) 6\n\n"
]
# Array of question objects for our quiz
questions = [
    Question(quiz_questions[0], "a"),
    Question(quiz_questions[1], "b"),
    Question(quiz_questions[2], "c")
]

# funtion to take the test
def take_test(questions):
    # set score
    score = 0
    # loop to ask questions
    for question in questions:
        answer = input(question.quest)
        if answer == question.ans:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions))
          + " questions correct!")

# run test
take_test(questions)