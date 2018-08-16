from random import shuffle


def main():
    questions = load_questions()
    for question in questions:
        shuffled_options = get_shuffled_options(question)
        ask_question(question[0], shuffled_options)


def ask_question(question, answers):
    print("{}?\nA){}\nB){}\nC){}".format(question, answers[0], answers[1], answers[2]))
    user_answer = ""
    while user_answer != "A" and user_answer != "B" and user_answer != "C":
        user_answer = input(">>>>")
        user_answer = user_answer.upper()

    return user_answer


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


main()
