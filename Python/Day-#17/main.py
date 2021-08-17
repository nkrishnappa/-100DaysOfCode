from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

q = QuizBrain(question_bank)
while q.still_has_questions():
    q.next_question()

print("You've completed the quiz")
print(f"Your final score is: {q.correct_answer_count}/{len(q.question_list)}")