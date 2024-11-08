# ui/quiz_selection_page.py
import tkinter as tk
import json
import os

class QuizSelectionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Select a Quiz", font=("Helvetica", 16))
        label.pack(pady=20)

        self.quizzes = self.get_quiz_list()

        for quiz_id, quiz_name in self.quizzes.items():
            btn = tk.Button(self, text=quiz_name, width=30,
                            command=lambda q=quiz_id: self.start_quiz(q))
            btn.pack(pady=5)

        btn_back = tk.Button(self, text="Back to Home", width=15,
                             command=lambda: controller.show_frame("HomePage"))
        btn_back.pack(pady=20)

    def get_quiz_list(self):
        with open(os.path.join('resources', 'quiz.json'), 'r', encoding='utf-8') as f:
            quizzes = json.load(f)
        return {quiz_id: quiz_info['name'] for quiz_id, quiz_info in quizzes.items()}

    def start_quiz(self, quiz_id):
        quiz_page = self.controller.frames["QuizPage"]
        quiz_page.load_quiz(quiz_id)
        self.controller.show_frame("QuizPage")
