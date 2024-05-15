import random


class Question:

    def __init__(self, question, correct_answer, fake_answer_1, fake_answer_2, fake_answer_3):
        self._question = question
        self._correct_answer = correct_answer
        self._fake_answer_1 = fake_answer_1
        self._fake_answer_2 = fake_answer_2
        self._fake_answer_3 = fake_answer_3

    def get_question(self):
        return self._question

    def get_correct_answer(self):
        return self._correct_answer

    def get_answers(self):
        answers = [self._correct_answer, self._fake_answer_1, self._fake_answer_2, self._fake_answer_3]
        random.shuffle(answers)
        return answers



questions = [Question("What is the capital of Slovenia?",
              "Ljubljana", "Tirana", "Bogota", "Maribor"),
             Question("What element has the symbol Sn?",
              "Tin","Scandium", "Stone", "Arsenic"),
             Question("Which country does NOT border France?",
              "Austria",
              "Brazil", "Monaco", "Belgium"),
             Question("Who was the european to reach the Americas?",
              "Leif Erikson",
              "Christopher Columbus", "Ferdinand Magellan", "James Cook"),
             Question("How long does it take light to travel from the Sun to the Earth?",
              "About 8 minutes","It's instantaneous", "About 11 days","2 or 3 months, depending on the time of year"),
             Question("Which of these noble ranks is highest?",
              "Duke","Baron", "Earl", "Marquis"),
             Question("A triangle has one side with a length of 3 and another side with a length of 4. What is the length of th third side?",
              "Impossible to say","4", "5", "6"),
             Question("What letter is a protractor shaped like?",
              "D","F", "L", "V"),
             Question("What is the national animal of Scotland?",
              "Unicorn","Eagle", "Lion", "Stag"),
             Question("Who is the patron Saint of Wales?",
              "St. David", "St. George", "St. Andrew", "St. Patrick"),
             Question("Which of the following is a portmanteau?",
              "Brunch","A man, a plan, a canal. Panama!", "Jumbo Shrimp", "Flamingo dancing"),
             Question("Where would you find the Spanish Steps",
              "Rome","New York City", "Madrid", "Mars"),
             Question("Where would you be most likely to see an epitaph?",
              "On a tombstone","At the bottom of a page", "At a zoo", "On a boat")]