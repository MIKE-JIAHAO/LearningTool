# ui/chapter_selection_page.py
import tkinter as tk
import os

class ChapterSelectionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Select a Chapter to Learn", font=("Helvetica", 16))
        label.pack(pady=20)

        self.chapters = self.get_chapter_list()

        for chapter in self.chapters:
            btn = tk.Button(self, text=chapter, width=30,
                            command=lambda c=chapter: self.open_chapter(c))
            btn.pack(pady=5)

        btn_back = tk.Button(self, text="Back to Home", width=15,
                             command=lambda: controller.show_frame("HomePage"))
        btn_back.pack(pady=20)

    def get_chapter_list(self):
        chapters_dir = os.path.join('resources', 'chapters')
        chapters = [f for f in os.listdir(chapters_dir) if f.endswith('.txt')]
        chapters.sort()
        return [os.path.splitext(f)[0] for f in chapters]

    def open_chapter(self, chapter_name):
        chapter_page = self.controller.frames["ChapterContentPage"]
        chapter_page.load_chapter(chapter_name)
        self.controller.show_frame("ChapterContentPage")
