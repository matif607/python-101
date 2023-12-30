from question_model import Quiz
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for questions in question_data:
    question_text = questions["question"]
    answer_text = questions["correct_answer"]
    new_question = Quiz(question_text, answer_text)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
