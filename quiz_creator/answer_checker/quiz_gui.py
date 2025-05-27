import tkinter as tk
from tkinter import messagebox

class QuizGui:
    def __init__(self, root_window, quiz_manager_instance):
        self.root = root_window
        self.quiz_manager = quiz_manager_instance
        self.answer_variable = tk.StringVar()
        self.current_question = None

        self.question_label = tk.Label(self.root, text="Question will appear here", wraplength=500, justify="left", font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.radio_buttons = {}
        for option in ['a', 'b', 'c', 'd']:
            self.radio_buttons[option] = tk.Radiobutton(self.root, text="", variable=self.answer_variable, value=option, wraplength=500, justify="left")
            self.radio_buttons[option].pack(anchor="w")

        self.next_button = tk.Button(self.root, text="Submit Answer", command=self.check_user_answer)
        self.next_button.pack(pady=10)

        self.display_next_question()

    def display_next_question(self):
        self.current_question = self.quiz_manager.get_next_question()
        if not self.current_question:
            messagebox.showinfo("Quiz Complete", f"You answered {self.quiz_manager.correct_answers_count} out of {self.quiz_manager.total_questions} questions correctly.")
            self.root.quit()
            return

        self.question_label.config(text=self.current_question["question"])
        for key, button in self.radio_buttons.items():
            button.config(text=f"{key}. {self.current_question['options'][key]}")
        self.answer_variable.set(None)

    def check_user_answer(self):
        selected_answer = self.answer_variable.get()
        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        if self.quiz_manager.is_correct_answer(selected_answer, self.current_question["answer"]):
            self.quiz_manager.correct_answers_count += 1
            messagebox.showinfo("Correct", "That's the correct answer!")
        else:
            correct_option_text = self.current_question["options"][self.current_question["answer"]]
            messagebox.showinfo("Incorrect", f"Wrong! The correct answer is {self.current_question['answer']}. {correct_option_text}")

        self.display_next_question()