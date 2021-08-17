class QuizBrain:
    def __init__(self, question_list: list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.correct_answer_count = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, input_answer, correct_answer):
        if input_answer.lower() == correct_answer.lower():
            self.correct_answer_count += 1
            print("You got it right!")
        else:
            print("You got it Wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.correct_answer_count}/{self.question_number} ")
        print("\n")
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_name_input = input(f"Q.{self.question_number}: {current_question.text}. (True/False) ")
        self.check_answer(question_name_input, current_question.answer)