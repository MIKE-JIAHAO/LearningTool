
# Documentation: Interactive Python Learning Tool

## Project Overview

The **Interactive Python Learning Tool** is a desktop application designed to help users learn Python programming through structured chapters and corresponding quizzes. The application provides a seamless learning experience by combining educational content with interactive assessments.

## Features

* **Chapter-Based Learning** : Users can select from multiple chapters, each containing specific learning materials.
* **Interactive Quizzes** : After studying a chapter, users can take a quiz to test their understanding of the material.
* **Progress Tracking** : The application records quiz results, allowing users to track their learning progress over time.
* **User-Friendly Interface** : An intuitive GUI built with Tkinter ensures easy navigation between different sections of the application.

## Project Structure

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">markdown</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>复制代码</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-markdown">interactive_learning_tool/
│
├── main.py
├── ui/
│   ├── __init__.py
│   ├── home_page.py
│   ├── chapter_selection_page.py
│   ├── chapter_content_page.py
│   ├── quiz_selection_page.py
│   ├── quiz_page.py
│   └── progress_page.py
│
├── modules/
│   ├── __init__.py
│   ├── database.py
│   └── utilities.py
│
├── resources/
│   ├── quiz.json
│   └── chapters/
│       ├── chapter1.txt
│       ├── chapter2.txt
│       └── chapter3.txt
│
├── requirements.txt
└── README.md
</code></div></div></pre>

## Usage Guide

### Home Page

Upon launching the application, you are greeted with the Home Page, which provides navigation options:

* **Start Learning** : Navigate to the Chapter Selection Page.
* **Quiz** : Navigate to the Quiz Selection Page.
* **View Progress** : Navigate to the Progress Tracking Page.

### Chapter Selection and Learning

1. **Select a Chapter**
   * Click on **Start Learning** from the Home Page.
   * On the Chapter Selection Page, a list of available chapters is displayed.
   * Click on a chapter (e.g., "chapter1") to view its content.
2. **Read Chapter Content**
   * The Chapter Content Page displays the content of the selected chapter in a scrollable text area.
   * Read through the material at your own pace.
   * Click **Back to Chapters** to return to the Chapter Selection Page or **Back to Home** to return to the Home Page.

### Quiz Selection and Participation

1. **Select a Quiz**
   * Click on **Quiz** from the Home Page.
   * On the Quiz Selection Page, a list of available quizzes corresponding to each chapter is displayed.
   * Click on a quiz (e.g., "Chapter 1 Quiz") to start.
2. **Take the Quiz**
   * The Quiz Page presents one question at a time with multiple-choice options.
   * Select an answer and click **Submit Answer** to proceed to the next question.
   * After completing all questions, your score is displayed.
   * Click **Back to Quizzes** to return to the Quiz Selection Page or **Back to Home** to return to the Home Page.

### Progress Tracking

* Click on **View Progress** from the Home Page to see a record of your quiz results.
* The Progress Page displays quiz IDs, scores, and timestamps in a table format.
* Click **Refresh** to update the progress data after taking new quizzes.
* Click **Back to Home** to return to the Home Page.

## Adding New Chapters and Quizzes

### Adding a New Chapter

1. **Create a Chapter File**
   * Navigate to the `resources/chapters/` directory.
   * Create a new text file named `chapterX.txt` (replace `X` with the next chapter number).
   * Add your chapter content to this file.
2. **Update the Application**
   * The application automatically lists all `.txt` files in the `chapters` directory as available chapters.

### Adding a New Quiz

1. **Update `quiz.json`**
   * Open the `resources/quiz.json` file.
   * Add a new entry for your quiz in the following format:
     <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">json</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>复制代码</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-json">"chapterX": {
         "name": "Chapter X Quiz",
         "questions": [
             {
                 "question": "Your question here?",
                 "options": ["Option1", "Option2", "Option3", "Option4"],
                 "answer": "CorrectAnswer"
             },
             // Add more questions as needed
         ]
     }
     </code></div></div></pre>
2. **Ensure Consistency**
   * Make sure the `quiz_id` (e.g., "chapterX") matches the chapter name.
   * Each quiz must have a unique `quiz_id` and `name`.

## Contributing

Contributions are welcome! If you'd like to improve the application, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.
