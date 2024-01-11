
import time

# q_text = ""

#TODO 1: Create a Model for a question in our Quiz
'''
Question object:
Attributes: text for the question itself.
            answer
These 2 attributes should be initialized with a value when a new question object is created from the Class.
ex: new_q = Question("2+3=5", "True")
new_q object
it will be added to text = "2+3=5"
                   answer = "True"


'''

# in order for us get the list of Questions objects from the List of Dictionaries from the question_model Module:
# we already know we can create a new question object by constructing one from the question, and giving it the required inputs.
# but in order for us to do this in the main.py file (here)



#Create the question bank: It should contain a List of question objects, each being intialized with a question and an answer:
#example:

# question_bank = [
#     Question(q1, a1),
#     Question(q2, a2),
#     Question(q3, a3),
#     ...
# ]

# my_question_databank = [    # create an empty List []
#     Question(each_singular_question['text'], each_singular_question['answer'])
#     for each_singular_question in question_data
# ]

# ORRRRRR

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []  #this will be a LIST of empty Question Objects
for question in question_data:
    question_text = question['text']   #question_text is a Variable. the text will come from those Question dictionaries, so if we wanna tap into a Dictionary, use 'text' Key!
    question_answer = question['answer']  #question_answer is a Variable. the answer will come from those Question dictionaries, so if we wanna tap into a Dictionary, use 'answer' Key! Yes it's a Key, since the Value pair is the True/False values, being stored.
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_answer[0])   #T for True; # 1 would be r
# QuizBrain(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("The quiz is finished! Your Final score is ... (drum roll, please):")
time.sleep(2)
print(f"{quiz.score}/{quiz.question_number}.")

