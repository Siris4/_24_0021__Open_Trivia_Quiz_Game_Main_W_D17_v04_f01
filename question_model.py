


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

#TODO 2: Create a Question class with __init__ method with 2 attributes: text and answer attribute

class Question():
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# new_q = Question("1st Random question to ask the player..", "False")
# print(new_q.text)
# print(new_q.answer)  #don't want this showing the player playing tho


# ques_1 = Question("Question #2 to ask player", "True")
# print(ques_1.text)
# print(ques_1.answer)