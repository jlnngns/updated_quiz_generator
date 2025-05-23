import tkinter as tk

class AnswerEntry:
    def __init__(self, parent, label_text):
        self.label = tk.Label(parent, text=label_text)
        self.label.pack()
        self.entry = tk.Entry(parent, width=60)
        self.entry.pack()

    def get(self):
        return self.entry.get()

    def clear(self):
        self.entry.delete(0, tk.END)
