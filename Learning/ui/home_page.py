# ui/home_page.py
import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome to the Interactive Learning Tool!", font=("Helvetica", 16))
        label.pack(pady=20)

        btn_learn = tk.Button(self, text="Start Learning", width=20,
                              command=lambda: controller.show_frame("ChapterSelectionPage"))
        btn_quiz = tk.Button(self, text="Quiz", width=20,
                             command=lambda: controller.show_frame("QuizSelectionPage"))
        btn_progress = tk.Button(self, text="View Progress", width=20,
                                 command=lambda: controller.show_frame("ProgressPage"))

        btn_learn.pack(pady=10)
        btn_quiz.pack(pady=10)
        btn_progress.pack(pady=10)
