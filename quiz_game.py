"""
This is a quiz game written for the python practice on sparta global training

"""
import random

questions = [{"question": "What is the capital of Slovenia?",
              "correct_answer": "Ljubljana",
              "fake_answers": ["Tirana", "Bogota", "Maribor"]},
             {"question": "What element has the symbol Sn?",
              "correct_answer": "Tin",
              "fake_answers": ["Scandium", "Stone", "Arsenic"]},
             {"question": "Which country does NOT border France?",
              "correct_answer": "Austria",
              "fake_answers": ["Brazil", "Monaco", "Belgium"]},
             {"question": "Who was the european to reach the Americas?",
              "correct_answer": "Leif Erikson",
              "fake_answers": ["Christopher Columbus", "Ferdinand Magellan", "James Cook"]},
             {"question": "How long does it take light to travel from the Sun to the Earth?",
              "correct_answer": "About 8 minutes",
              "fake_answers": ["It's instantaneous", "About 11 days","2 or 3 months, depending on the time of year"]},
             {"question": "Which of these noble ranks is highest?",
              "correct_answer": "Duke",
              "fake_answers": ["Baron", "Earl", "Marquis"]},
             {"question": "A triangle has one side with a length of 3 and another side with a length of 4. What is the length of th third side?",
              "correct_answer": "Impossible to say",
              "fake_answers": ["4", "5", "6"]},
             {"question": "What letter is a protractor shaped like?",
              "correct_answer": "D",
              "fake_answers": ["F", "L", "V"]},
             {"question": "What is the national animal of Scotland?",
              "correct_answer": "Unicorn",
              "fake_answers": ["Eagle", "Lion", "Stag"]},
             {"question": "Who is the patron Saint of Wales?",
              "correct_answer": "St. David",
              "fake_answers": ["St. George", "St. Andrew", "St. Patrick"]},
             {"question": "Which of the following is a portmanteau?",
              "correct_answer": "Brunch",
              "fake_answers": ["A man, a plan, a canal. Panama!", "Jumbo Shrimp", "Flamingo dancing"]},
             {"question": "Where would you find the Spanish Steps",
              "correct_answer": "Rome",
              "fake_answers": ["New York City", "Madrid", "Mars"]},
             {"question": "Where would you be most likely to see an epitaph?",
              "correct_answer": "On a tombstone",
              "fake_answers": ["At the bottom of a page", "At a zoo", "On a boat"]}]


def make_question_list(qs, number):
    random.shuffle(qs)
    return qs[:number]


def ask_question(question):
    typed = ""
    corr = False
    options = ['a', 'b', 'c', 'd']
    answer = []
    answers = question["fake_answers"]
    answers.append(question["correct_answer"])  #make list of all answers
    random.shuffle(answers)  #shuffle the order of the answers
    #print the question
    print("{0} \n\n\ta - {1}\n\tb - {2}\n\tc - {3}\n\td - {4}\n".format(question["question"],
                                                                        answers[0],
                                                                        answers[1],
                                                                        answers[2],
                                                                        answers[3]))
    """if answers[4]:
        print(answers[4])
        """
    type_not_correct = True
    while type_not_correct:
        typed = input("Please give an answer: ").lower()  ## ask for an answer
        if typed not in options:
            print("Invalid answer, please give answer a, b, c, or d")
        else:
            type_not_correct = False
    given_answer = answers[options.index(typed)]  #get full answer from option chosen
    if given_answer == question["correct_answer"]:
        #if the answer is correct, store that it was correct
        corr = True

    return corr, given_answer

def print_results(questions, results):
    for result in results:
        print("Question {0}:\n".format(result[0]))
        print(questions[result[0]-1]["question"]+"\n")
        if result[1]:
            print("You answered {0}, which was correct! Congratulations!".format(result[2]))
        else:
            print("You answered {0}, which was incorrect! The correct answer was {1}.".format(result[2], questions[result[0]-1]["correct_answer"]))
    return


if __name__ == "__main__":
    playing = True
    while playing:
        input("Are you ready to begin? Please press enter")
        num_of_questions = 5
        questions_asked = 0
        results = []
        qus = make_question_list(questions, num_of_questions)

        while questions_asked < num_of_questions:
            print("Question {0}:\n".format(questions_asked+1))
            correct, g_answer = ask_question(qus[questions_asked])
            questions_asked += 1
            results.append([questions_asked,correct, g_answer])
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
