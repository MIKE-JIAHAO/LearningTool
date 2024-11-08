# ui/quiz_page.py
import tkinter as tk
from tkinter import messagebox
from modules.database import add_quiz_result, load_quiz_data

class QuizPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.quiz_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.quiz_label.pack(pady=10)

        self.question_label = tk.Label(self, text="", wraplength=600, font=("Helvetica", 14))
        self.question_label.pack(pady=10)

        self.var = tk.StringVar()
        self.options = []
        for _ in range(4):
            rb = tk.Radiobutton(self, text="", variable=self.var, value="", wraplength=600)
            rb.pack(anchor='w')
            self.options.append(rb)

        self.submit_button = tk.Button(self, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        btn_back = tk.Button(self, text="Back to Quizzes", width=15,
                             command=lambda: controller.show_frame("QuizSelectionPage"))
        btn_back.pack(pady=10)

    def load_quiz(self, quiz_id):
        self.quiz_id = quiz_id
        quiz_data = load_quiz_data(quiz_id)
        self.quiz_name = quiz_data['name']
        self.questions = quiz_data['questions']
        self.current_question = 0
        self.score = 0
        self.user_answers = {}
        self.quiz_label.config(text=self.quiz_name)
        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=f"Q{self.current_question + 1}: {q['question']}")
            self.var.set(None)
            for i, option in enumerate(q['options']):
                self.options[i].config(text=option, value=option)
                self.options[i].pack(anchor='w')
            for i in range(len(q['options']), 4):
                self.options[i].pack_forget()
        else:
            self.show_result()

    def submit_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option before submitting.")
            return
        correct = self.questions[self.current_question]['answer']
        if selected == correct:
            self.score += 1
        self.user_answers[self.current_question] = selected
        self.current_question += 1
        self.load_question()

    def show_result(self):
        messagebox.showinfo("Result", f"Your score is {self.score}/{len(self.questions)}")
        # Save the result
        add_quiz_result(user_id=1, quiz_id=self.quiz_id, score=self.score)  # Assuming user_id is 1
        # Reset the quiz
        self.controller.show_frame("QuizSelectionPage")
