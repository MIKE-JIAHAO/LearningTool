# ui/chapter_content_page.py
import tkinter as tk
from tkinter import scrolledtext
import os

class ChapterContentPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.chapter_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.chapter_label.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(self, wrap='word', font=("Helvetica", 12))
        self.text_area.pack(expand=True, fill='both', padx=20, pady=10)
        self.text_area.config(state='disabled')

        btn_back = tk.Button(self, text="Back to Chapters", width=15,
                             command=lambda: controller.show_frame("ChapterSelectionPage"))
        btn_back.pack(pady=10)

    def load_chapter(self, chapter_name):
        self.chapter_label.config(text=chapter_name)
        chapters_dir = os.path.join('resources', 'chapters')
        chapter_file = os.path.join(chapters_dir, f"{chapter_name}.txt")
        with open(chapter_file, 'r', encoding='utf-8') as file:
            content = file.read()
        self.text_area.config(state='normal')
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, content)
        self.text_area.config(state='disabled')
