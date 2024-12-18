class QuizzBrain:
    def __init__(self, question_bak):
        self.questions = question_bak
        self.score = 0
        self.question_number = 0

    def get_user_answer(self):
        self.current = self.questions[self.question_number]
        self.question_number += 1
        answer = input(
            (f"Q.{self.question_number}: {self.current.text}. (True/False? )"))

        return answer

    def check_asnwer(self):
        answer = self.get_user_answer()
        correct_asnwer = self.current.answer
        if answer.capitalize() == correct_asnwer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print("The correct answer was: ", correct_asnwer,)

    def display_score(self):
        print(f"Your current score is: {self.score}/{self.question_number}")

    def is_still_question(self):
        return self.question_number < len(self.questions)
