from random import shuffle

class Question:
    def __init__(self, question, answer, wrong_answer_1, wrong_answer_2, category):
        self.question = question
        self.answer = answer
        self.wrong_answer_1 = wrong_answer_1
        self.wrong_answer_2 = wrong_answer_2
        self.category = category

    def is_correct_answer(self, user_answer):
        if user_answer != self.answer:
            print("Incorrect")
            return 0
        else:
            print("Correct")
            return 1

    def ask_question(self):
        options = [self.answer, self.wrong_answer_1, self.wrong_answer_2]
        shuffle(options)
        print("{}?\nA){}\nB){}\nC){}".format(self.question, options[0], options[1], options[2]))
        user_answer = ""
        while user_answer != "A" and user_answer != "B" and user_answer != "C":
            user_answer = input(">>>>")
            user_answer = user_answer.upper()
        if user_answer == "A":
            return options[0]
        if user_answer == "B":
            return options[1]
        else:
            return options[2]

    def save_to_list(self):
        return [self.question, self.answer, self.wrong_answer_1, self.wrong_answer_2, self.category]
