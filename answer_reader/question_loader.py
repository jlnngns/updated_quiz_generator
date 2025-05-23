from tkinter import messagebox

class QuestionLoader:
    @staticmethod
    def load_questions_from_file(filename="questions.txt"):
        questions_list = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read().strip().split("\n\n")
                for question_block in content:
                    lines = question_block.strip().split("\n")
                    if len(lines) == 6:
                        question_text = lines[0].replace("Question: ", "").strip()
                        option_a = lines[1].replace("a. ", "").strip()
                        option_b = lines[2].replace("b. ", "").strip()
                        option_c = lines[3].replace("c. ", "").strip()
                        option_d = lines[4].replace("d. ", "").strip()
                        correct_choice = lines[5].replace("Correct answer: ", "").strip().lower()
                        questions_list.append({
                            "question": question_text,
                            "options": {
                                "a": option_a,
                                "b": option_b,
                                "c": option_c,
                                "d": option_d
                            },
                            "answer": correct_choice
                        })
        except FileNotFoundError:
            messagebox.showerror("Error", "The questions file was not found.")
        return questions_list
