from random import shuffle
from random import choice


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
        shuffled_options = get_shuffled_options(question)
        user_answer = ask_question(question, shuffled_options)
        points += is_correct_answer(question[1], user_answer)


def is_correct_answer(answer, user_answer):
    if user_answer != answer:
        print("Incorrect")
        return 0
    else:
        print("Correct")
        return 1


def ask_question(question, answers):
    print("{}?\nA){}\nB){}\nC){}".format(question[0], answers[0], answers[1], answers[2]))
    user_answer = ""
    while user_answer != "A" and user_answer != "B" and user_answer != "C":
        user_answer = input(">>>>")
        user_answer = user_answer.upper()

    if user_answer == "A":
        return answers[0]
    if user_answer == "B":
        return answers[1]
    else:
        return answers[2]


def get_shuffled_options(question_row):
    options = []
    for i in range(1, 4):
        options.append(question_row[i])
    shuffle(options)
    return options


def load_questions():
    questions = []
    question_file = open("Questions", "r")
    for line in question_file:
        question = line.strip("\n").split(",")
        questions.append(question)
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
        if category == question[4]:
            category_questions.append(question)
    chosen_question = choice(category_questions)
    return chosen_question


main()
