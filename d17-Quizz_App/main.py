from question_model import Question
from quiz_brain import QuizzBrain
from data import question_data

questions = []
for question in question_data:
    questions.append(Question(question["text"], question["answer"]))

my_quizz = QuizzBrain(questions)

while my_quizz.is_still_question():
    my_quizz.check_asnwer()
    my_quizz.display_score()
