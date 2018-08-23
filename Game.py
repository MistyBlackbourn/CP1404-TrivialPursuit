from random import shuffle
from random import choice


def main():
    questions = load_questions()
    for i in range(10):
        category = get_random_category()
        question = get_question(category, questions)
        shuffled_options = get_shuffled_options(question)
        user_answer = ask_question(question, shuffled_options)
        is_correct_answer(question[1], user_answer)


def is_correct_answer(answer, user_answer):
    if user_answer != answer:
        print("Incorrect")
    else:
        print("Correct")


def ask_question(question, answers):
    print("{}?\nA){}\nB){}\nC){}".format(question, answers[0], answers[1], answers[2]))
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
