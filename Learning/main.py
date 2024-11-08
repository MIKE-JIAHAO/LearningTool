# main.py
import tkinter as tk
from ui.home_page import HomePage
from ui.chapter_selection_page import ChapterSelectionPage
from ui.chapter_content_page import ChapterContentPage
from ui.quiz_selection_page import QuizSelectionPage
from ui.quiz_page import QuizPage
from ui.progress_page import ProgressPage
from modules.database import init_db

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interactive Learning Tool")
        self.geometry("800x600")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (HomePage, ChapterSelectionPage, ChapterContentPage,
                  QuizSelectionPage, QuizPage, ProgressPage):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def get_page(self, page_class):
        '''Return an instance of a page'''
        return self.frames[page_class]

if __name__ == "__main__":
    init_db()  # Initialize the database
    app = MainApplication()
    app.mainloop()
