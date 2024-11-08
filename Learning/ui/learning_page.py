# ui/learning_page.py
import tkinter as tk
from modules.code_editor import CodeEditor

class LearningPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Learning Content", font=("Helvetica", 16))
        label.pack(pady=20)

        self.editor = CodeEditor(self)
        self.editor.pack(fill="both", expand=True, padx=20, pady=10)

        btn_back = tk.Button(self, text="Back to Home", width=15,
                             command=lambda: controller.show_frame("HomePage"))
        btn_back.pack(pady=10)
