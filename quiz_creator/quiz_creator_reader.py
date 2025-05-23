import tkinter as tk
from tkinter import messagebox
from question_entry import QuestionEntry
from answer_entry import AnswerEntry
from correct_answer_entry import CorrectAnswerEntry

class QuizCreatorReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Creator")

        self.question_entry = QuestionEntry(self.root)
        self.answer_a_entry = AnswerEntry(self.root, "Answer a:")
        self.answer_b_entry = AnswerEntry(self.root, "Answer b:")
        self.answer_c_entry = AnswerEntry(self.root, "Answer c:")
        self.answer_d_entry = AnswerEntry(self.root, "Answer d:")
        self.correct_answer_entry = CorrectAnswerEntry(self.root)

        tk.Button(self.root, text="Save Question", command=self.save_question).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.exit_program).pack()

    def clear_all_entries(self):
        self.question_entry.clear()
        self.answer_a_entry.clear()
        self.answer_b_entry.clear()
        self.answer_c_entry.clear()
        self.answer_d_entry.clear()
        self.correct_answer_entry.clear()

    def save_question(self):
        question_text = self.question_entry.get()
        answer_a = self.answer_a_entry.get()
        answer_b = self.answer_b_entry.get()
        answer_c = self.answer_c_entry.get()
        answer_d = self.answer_d_entry.get()
        correct_answer = self.correct_answer_entry.get()

        if not all([question_text, answer_a, answer_b, answer_c, answer_d]) or correct_answer not in ['a', 'b', 'c', 'd']:
            messagebox.showwarning("Input Error", "Please fill in all fields and ensure correct answer is a, b, c, or d.")
            return

        with open("questions.txt", "a", encoding="utf-8") as file:
            file.write(f"Question: {question_text}\n")
            file.write(f"a. {answer_a}\n")
            file.write(f"b. {answer_b}\n")
            file.write(f"c. {answer_c}\n")
            file.write(f"d. {answer_d}\n")
            file.write(f"Correct answer: {correct_answer}\n\n")

        self.clear_all_entries()
        messagebox.showinfo("Saved", "Question saved successfully!")

    def exit_program(self):
        self.root.destroy()
