#quiz_brain module:

counter = 0

class QuizBrain:
    def __init__(self, q_list, score=0):   # IF YOU ASSIGN A DEFAULT NUMBER AS AN ASSIGNMENT JUST BELOW THIS DEFINITION LINE, WE CAN SKIP PLACING IT AS A PARAMETER HERE! (question_number)
        self.question_number = 0
        self.question_list = q_list  #this will be passed into the parameter above
        self.score = score

    def still_has_questions(self):
        if self.question_number < len(self.question_list): #(these 4 lines of code, or just the one above, which evaluates to True or False directly anyhow, as it is)
            return self.question_number < len(self.question_list)
            # return True

        # OR
        # else:
        #     print("The quiz is finished!")
        #     print(f"Your final score is: {self.score}/{self.question_number}")
        #     False
        # return self.question_number < len(self.question_list)
        # else:
        #     if self.question_number < len(self.question_list) == False:
        #         print("The quiz is finished!")
        #         print(f"Your final score is: {checkscore}/{question_number}.\n")

        #if self.question_number < len(self.question_list): (these 4 lines of code, or just the one above, which evaluates to True or False directly anyhow, as it is)
            # return True
        # else:
        #     False


        # Method: next_question:    Retrieve the item at the current question_number from the question_list, then use input() to show the user the Question text, and ask for user's answer.
    #
    def next_question(self):
        current_question = self.question_list[self.question_number]
        # print(current_question.text)
        self.question_number += 1
        user_answer = input(f"Question #{self.question_number}: {current_question.text} ('True' or 'False'): ").lower()
        # correct_answer = current_question.answer
        self.check_answer(user_answer, current_question.answer) #we can pass over these 2 parameters, and we can receive it in the def check_answer() block below:



    def check_answer(self, user_answer, correct_answer):  # current_question.answer gets passed into the 2nd param, becoming that variable.
        # print(f"user_answer.lower()) is: {user_answer.lower()}")
        # print(f"correct_answer.lower() is: {correct_answer.lower()}")
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"Your current score is {self.score}/{self.question_number}.\n")
        else:
            print(f"Womp. That is incorrect. The correct answer is {correct_answer}.")
            print(f"Your current score is {self.score}/{self.question_number}.\n")



##########################3
# quiz_brain.py module:
# class QuizBrain:
#     def __init__(self, q_list):
#         self.question_number = 0
#         self.question_list = q_list
#
#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         print(current_question.text)
#         user_answer = input(f"Question#{self.question_number + 1}: {current_question.text} (T or F) for True/False: ").upper()
#         self.question_number += 1  # Increment the question number

# You don't need to call this function at this point.
# quiz = QuizBrain(question_bank)
# quiz.next_question()