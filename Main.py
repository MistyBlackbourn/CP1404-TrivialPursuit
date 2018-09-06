from random import choice
from Question import Question


def main():
    questions = load_questions()

    user_choice = ""
    while user_choice != "Q":
        print("P - Play Game",
              "A - Add Question",
              "Q - Quit",
              sep="\n"
              )
        user_choice = input(">>> ").upper()
        if user_choice == "P":
            play_game(questions)
        elif user_choice == "A":
            add_question(questions)
            pass
        elif user_choice == "Q":
            save_questions(questions)
            print("Farewell wizard")
        else:
            print("WRONG MENU CHOICE")


def add_question(questions):
    new_question = []

    print("Wizard what is your question?")
    user_question = input(">>> ")
    while user_question == "":
        print("Don't be shy, what is your question?")
        user_question = input(">>> ")
    new_question.append(user_question)

    print("Wizard, what is the truth of your question?")
    three_answers = 0
    while three_answers < 3:
        user_answer = input(">>> ")
        while user_answer == "":
            print("I NEED ANSWERS!!!!")
            user_answer = input(">>> ")
        three_answers += 1
        if three_answers < 3:
            print("What is the #{} lie of your question?".format(three_answers))
        new_question.append(user_answer)

    print("Wizard what is your category?")
    user_category = input(">>> ")
    while user_category == "":
        print("Don't be shy, what is your category?")
        user_category = input(">>> ")
    new_question.append(user_category)

    questions.append(new_question)


def save_questions(questions):
    question_file = open("Questions", mode="w")
    for question in questions:
        question_line = ",".join(question)
        question_file.write(question_line + "\n")
    question_file.close()


def play_game(questions):
    points = 0
    while points < 10:
        category = get_random_category()
        question = get_question(category, questions)
        user_answer = question.ask_question()
        question.is_correct_answer(user_answer)

        # shuffled_options = get_shuffled_options(question)
        # user_answer = ask_question(question, shuffled_options)
        # points += is_correct_answer(question[1], user_answer)



def load_questions():
    questions = []
    question_file = open("Questions", "r")
    for line in question_file:
        question = line.strip("\n").split(",")
        questions.append(Question(question[0], question[1], question[2], question[3], question[4]))
    question_file.close()
    return questions


def get_random_category():
    categories = ["The Dark Arts", "Magical People", "Magical Objects", "Hogwarts", "Animals & Magical Creatures",
                  "Magical Spells & Potions"]
    chosen_cetegory = choice(categories)
    return chosen_cetegory


# Function get_question(category, questions):
def get_question(category, questions):
    category_questions = []
    for question in questions:
        if category == question.category:
            category_questions.append(question)
    chosen_question = choice(category_questions)
    return chosen_question


main()
