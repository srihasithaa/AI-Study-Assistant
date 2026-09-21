import sqlite3

connection = sqlite3.connect("./database/study_assistant.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS study_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_question TEXT NOT NULL,
    topic TEXT NOT NULL,
    explanation TEXT NOT NULL,
    example TEXT,
    related_concepts TEXT,
    practice_question TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()

connection.close()

print("Study sessions table created successfully!")