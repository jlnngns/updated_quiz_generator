import tkinter as tk

class CorrectAnswerEntry:
    def __init__(self, parent):
        self.label = tk.Label(parent, text="Correct answer (a/b/c/d):")
        self.label.pack()
        self.entry = tk.Entry(parent, width=5)
        self.entry.pack()

    def get(self):
        return self.entry.get().lower()

    def clear(self):
        self.entry.delete(0, tk.END)
