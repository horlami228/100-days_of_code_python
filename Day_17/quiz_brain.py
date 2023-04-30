"""create a new quiz brain class"""


class QuizBrain:
    """initialize a new Quiz brain object"""

    def __init__(self, quiz_list):
        self.quiz_no = 0
        self.quiz_list = quiz_list
        self.score = 0

    def still_has_question(self):
        if len(self.quiz_list) > self.quiz_no:
            return True
        else:
            return False

    def check_answer(self, answer, current_answer):
        if answer.lower() == current_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"Your current answer is: {current_answer}")
        else:
            print("That's wrong")
            print(f"The correct answer was: {current_answer}")
        print("\n")

    def next_question(self):
        current_question = self.quiz_list[self.quiz_no]
        self.quiz_no += 1
        answer = input("Q.{}: {} (True/False)?: ".format(self.quiz_no, current_question.text))
        self.check_answer(answer, current_question.answer)
