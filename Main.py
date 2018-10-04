from Question import Question
from Game import Game
from random import shuffle
from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class TrivialPursuitApp(App):
    question = StringProperty()
    answer_a = StringProperty()
    answer_b = StringProperty()
    answer_c = StringProperty()

    def __init__(self):
        super(TrivialPursuitApp, self).__init__()
        questions = load_questions()
        self.game = Game(questions, ["The Dark Arts", "Magical People", "Magical Objects", "Hogwarts",
                                     "Animals & Magical Creatures",
                                     "Magical Spells & Potions"])

    def build(self):
        self.title = "Harry Potter Trivial Pursuit"
        self.root = Builder.load_file('trivial_pursuit.kv')
        return self.root

    def handle_category_press(self):
        category = self.game.get_random_category()
        self.root.ids.category_label.text = "Cateogory: {}".format(category)
        random_question = self.game.get_question(category)
        self.question = random_question.question + "?"
        options = [random_question.answer, random_question.wrong_answer_1, random_question.wrong_answer_2]
        shuffle(options)
        self.answer_a = options[0]
        self.answer_b = options[1]
        self.answer_c = options[2]

    def handle_answer_press(self, answer_text):
        pass


# def add_question(questions):
#     new_question = []
#     print("Wizard what is your question?")
#     user_question = input(">>> ")
#     while user_question == "":
#         print("Don't be shy, what is your question?")
#         user_question = input(">>> ")
#     new_question.append(user_question)
#
#     print("Wizard, what is the truth of your question?")
#     three_answers = 0
#     while three_answers < 3:
#         user_answer = input(">>> ")
#         while user_answer == "":
#             print("I NEED ANSWERS!!!!")
#             user_answer = input(">>> ")
#         three_answers += 1
#         if three_answers < 3:
#             print("What is the #{} lie of your question?".format(three_answers))
#         new_question.append(user_answer)
#
#     print("Wizard what is your category?")
#     user_category = input(">>> ")
#     while user_category == "":
#         print("Don't be shy, what is your category?")
#         user_category = input(">>> ")
#     new_question.append(user_category)
#
#     question = Question(new_question[0], new_question[1], new_question[2], new_question[3], new_question[4])
#     questions.append(question)
#
#
# def save_questions(questions):
#     question_file = open("Questions", mode="w")
#     for question in questions:
#         question_line = ",".join(question.save_to_list())
#         question_file.write(question_line + "\n")
#     question_file.close()
#
#
def load_questions():
    questions = []
    question_file = open("Questions", "r")
    for line in question_file:
        question = line.strip("\n").split(",")
        questions.append(Question(question[0], question[1], question[2], question[3], question[4]))
    question_file.close()
    return questions


TrivialPursuitApp().run()
