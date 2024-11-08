# modules/database.py
import sqlite3
import os
import json

DB_NAME = 'learning_tool.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    ''')
    
    # Create quiz_results table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            quiz_id TEXT,
            score INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    # Check if a sample user exists; if not, create one
    cursor.execute('SELECT id FROM users WHERE username = ?', ('sample_user',))
    user = cursor.fetchone()
    if not user:
        cursor.execute('INSERT INTO users (username) VALUES (?)', ('sample_user',))
        conn.commit()

    conn.close()

def add_quiz_result(user_id, quiz_id, score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO quiz_results (user_id, quiz_id, score)
        VALUES (?, ?, ?)
    ''', (user_id, quiz_id, score))
    conn.commit()
    conn.close()

def get_user_progress(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT quiz_id, score, timestamp FROM quiz_results
        WHERE user_id = ?
        ORDER BY timestamp DESC
    ''', (user_id,))
    results = cursor.fetchall()
    conn.close()
    return results

def load_quiz_data(quiz_id):
    with open(os.path.join('resources', 'quiz.json'), 'r', encoding='utf-8') as f:
        quizzes = json.load(f)
    return quizzes.get(quiz_id, {})
