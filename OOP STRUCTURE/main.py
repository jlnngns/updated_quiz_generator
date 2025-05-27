import tkinter as tk
from quiz_creator.quiz_creator_reader import QuizCreatorReader

def main():
    root = tk.Tk()
    app = QuizCreatorReader(root)
    root.mainloop()

if __name__ == "__main__":
    main()