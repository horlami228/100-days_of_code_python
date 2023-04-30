from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

"""create a list of Question objects with data from our question_data"""
Question_bank = []
for i in range(len(question_data)):
    Question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

questions = QuizBrain(Question_bank)
while questions.still_has_question():
    questions.next_question()
print("You have completed the Quiz")
print("Your final score is: {}/{}".format(questions.score, questions.quiz_no))
