# ui/progress_page.py
import tkinter as tk
from tkinter import ttk
from modules.database import get_user_progress

class ProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Learning Progress", font=("Helvetica", 16))
        label.pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("Quiz ID", "Score", "Timestamp"), show='headings')
        self.tree.heading("Quiz ID", text="Quiz ID")
        self.tree.heading("Score", text="Score")
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        btn_refresh = tk.Button(self, text="Refresh", command=self.load_progress)
        btn_refresh.pack(pady=5)

        btn_back = tk.Button(self, text="Back to Home", width=15,
                             command=lambda: controller.show_frame("HomePage"))
        btn_back.pack(pady=10)

        self.load_progress()

    def load_progress(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        results = get_user_progress(user_id=1)  # Assuming user_id is 1
        for row in results:
            self.tree.insert("", tk.END, values=row)
