from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.question_remaining(): #if the quiz has questions remaining
    quiz.next_question()

print("Quiz complete!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")