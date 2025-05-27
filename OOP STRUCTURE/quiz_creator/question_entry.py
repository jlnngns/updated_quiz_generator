import tkinter as tk

class QuestionEntry:
    def __init__(self, parent):
        self.label = tk.Label(parent, text="Enter Question:")
        self.label.pack()
        self.entry = tk.Entry(parent, width=60)
        self.entry.pack()

    def get(self):
        return self.entry.get()

    def clear(self):
        self.entry.delete(0, tk.END)