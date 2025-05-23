import tkinter as tk
from question_loader import QuestionLoader
from quiz_manager import QuizManager
from quiz_gui import QuizGui

def main():
    root_window = tk.Tk()
    root_window.title("Quiz Creator")

    questions = QuestionLoader.load_questions_from_file()
    quiz_manager_instance = QuizManager(questions)
    QuizGui(root_window, quiz_manager_instance)

    root_window.mainloop()

if __name__ == "__main__":
    main()
