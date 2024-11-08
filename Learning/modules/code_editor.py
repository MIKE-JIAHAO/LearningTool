# modules/code_editor.py
import tkinter as tk
from tkinter import scrolledtext
from modules.error_feedback import analyze_code, run_code

class CodeEditor(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Code editor area
        self.text = scrolledtext.ScrolledText(self, wrap="none", height=15, width=80, font=("Consolas", 12))
        self.text.pack(pady=10, fill="both", expand=True)

        # Run button
        self.run_button = tk.Button(self, text="Run Code", command=self.execute_code)
        self.run_button.pack(pady=5)

        # Output display area
        self.output = scrolledtext.ScrolledText(self, wrap="none", height=10, width=80, bg="#f0f0f0", font=("Consolas", 12))
        self.output.pack(pady=10, fill="both", expand=True)

    def execute_code(self):
        code = self.text.get("1.0", tk.END)
        analysis = analyze_code(code)
        if analysis['status'] == "success":
            result = run_code(code)
        else:
            result = analysis['message']
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, result)
