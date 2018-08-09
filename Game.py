def main():
    question_file = open("Questions", "r")

    questions = []

    for line in question_file:
        question = line.strip("\n").split(",")
        questions.append(question)

    print(questions)


main()
