import sqlite3


DATABASE_PATH = "./database/study_assistant.db"


def create_table():
    connection = sqlite3.connect(DATABASE_PATH)
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


def save_session(answer_data):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO study_sessions (
        student_question,
        topic,
        explanation,
        example,
        related_concepts,
        practice_question
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        answer_data["student_question"],
        answer_data["topic"],
        answer_data["explanation"],
        answer_data["example"],
        ", ".join(answer_data["related_concepts"]),
        answer_data["practice_question"]
    ))

    connection.commit()
    connection.close()


def get_previous_sessions():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT id, student_question, topic, created_at
    FROM study_sessions
    ORDER BY id
    """)

    sessions = cursor.fetchall()

    connection.close()

    return sessions