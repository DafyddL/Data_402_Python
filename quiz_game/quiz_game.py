"""
This is a quiz game written for the python practice on sparta global training

"""
import random
import quiz_questions as qq


def make_question_list(qs, number):
    random.shuffle(qs)
    return qs[:number]


def ask_question(question):
    typed = ""
    corr = False
    options = ['a', 'b', 'c', 'd']
    answers = question.get_answers()  #make list of all answers
    #print the question
    print("{0} \n\n\ta - {1}\n\tb - {2}\n\tc - {3}\n\td - {4}\n".format(question.get_question(),
                                                                        answers[0],
                                                                        answers[1],
                                                                        answers[2],
                                                                        answers[3]))
    type_not_correct = True
    while type_not_correct:
        typed = input("Please give an answer: ").lower()  ## ask for an answer
        if typed not in options:
            print("Invalid answer, please give answer a, b, c, or d")
        else:
            type_not_correct = False
    given_answer = answers[options.index(typed)]  #get full answer from option chosen
    if given_answer == question.get_correct_answer():
        #if the answer is correct, store that it was correct
        corr = True

    return corr, given_answer


def print_results(questions, results):
    for result in results:
        print("Question {0}:\n".format(result[0]))
        print(questions[result[0] - 1]["question"] + "\n")
        if result[1]:
            print("You answered {0}, which was correct! Congratulations!".format(result[2]))
        else:
            print("You answered {0}, which was incorrect! The correct answer was {1}.".format(result[2],
                                                                                              questions[result[0] - 1][
                                                                                                  "correct_answer"]))
    return


if __name__ == "__main__":
    playing = True
    while playing:
        input("Are you ready to begin? Please press enter")
        num_of_questions = 5
        questions_asked = 0
        results = []
        qus = make_question_list(qq.questions, num_of_questions)

        while questions_asked < num_of_questions:
            print("Question {0}:\n".format(questions_asked + 1))
            correct, g_answer = ask_question(qus[questions_asked])
            questions_asked += 1
            results.append([questions_asked, correct, g_answer])
        score = sum([result[1] for result in results])
        print("You scored {0}/{1}".format(score, num_of_questions))

        type_view_results = True
        while type_view_results:
            view_results = input("Would you like to review your results? ").lower()
            if view_results not in ["yes", "no"]:
                print("Please answer Yes or No")
            elif view_results == "yes":
                print_results(qus, results)
                type_view_results = False
            else:
                type_view_results = False

        type_play_again = True
        while type_play_again:
            play_again = input("Would you like to play again? ").lower()
            if play_again not in ["yes", "no"]:
                print("Please answer Yes or No")
            else:
                break
        if play_again == "no":
            playing = False
            print("Thanks for playing!")
            break
