import random
from tkinter import messagebox

class QuizManager:
    def __init__(self, questions_list):
        self.all_questions = questions_list
        self.remaining_questions = questions_list.copy()
        random.shuffle(self.remaining_questions)
        self.total_questions = len(questions_list)
        self.correct_answers_count = 0

    def get_next_question(self):
        if not self.remaining_questions:
            return None
        current_question_data = self.remaining_questions.pop()
        return current_question_data

    def is_correct_answer(self, selected_answer, correct_answer):
        return selected_answer == correct_answer