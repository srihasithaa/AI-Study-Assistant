
# AI Study Assistant

An AI-powered study assistant built with Python, Ollama, Gemma 3 4B, prompt engineering, structured JSON output, and SQLite.

The application allows students to enter an academic question, receive a structured explanation from an AI tutor, and automatically save each study session for later reference.

## Features

- Ask questions about technical and academic concepts
- AI-generated explanations using Gemma 3 4B
- Prompt engineering with:
  - Role prompting
  - Context
  - Constraints
  - Structured output instructions
- Structured JSON responses
- Provides:
  - Explanation
  - Example
  - Related concepts
  - Practice question
- Stores study sessions in SQLite
- Automatically records timestamps
- Retrieves previous study sessions
- Simple command-line interface

## Tech Stack

- Python 3.13
- Ollama
- Gemma 3 4B
- SQLite
- JSON
- Git & GitHub

## Project Structure

```text
AI Study Assistsant/
│
├── database/
│   └── study_assistant.db
│
├── prompts/
│   └── study_prompt.txt
│
├── src/
│   ├── main.py
│   └── database.py
│
├── .gitignore
└── ReadME.md
```

## How It Works

Student Question
       ↓
Prompt Template
       ↓
Gemma 3 4B
       ↓
Structured JSON
       ↓
Python JSON Parsing
       ↓
Display Study Response
       ↓
Save to SQLite
       ↓
Retrieve Previous Sessions

## Setup

### 1. Clone the repository

git clone https://github.com/srihasithaa/AI-Study-Assistant.git
cd AI-Study-Assistant

### 2. Create a virtual environment

python3 -m venv .venv

Activate it:

source .venv/bin/activate

### 3. Install dependencies

pip install ollama

### 4. Install and run Ollama

Make sure Ollama is installed and running.

Verify that Gemma 3 4B is available:

ollama list

If necessary:

ollama pull gemma3:4b

### 5. Run the application

From the project root:

python src/main.py

## Example

What do you want to study? Enter the question:
What is SQL window function?

The assistant generates:

Question:
What is SQL window function?

Topic:
SQL Window Functions

Explanation:
...

Example:
...

Related Concepts:
1. Partitioning
2. Aggregate Functions
3. GROUP BY

Practice Question:
...

The session is then stored in the SQLite database.

## Database

Study sessions are stored in the `study_sessions` table.

Each session contains:

| Field | Description |
|---|---|
| `id` | Unique session ID |
| `student_question` | Question entered by the student |
| `topic` | Identified topic |
| `explanation` | AI-generated explanation |
| `example` | Example related to the topic |
| `related_concepts` | Related concepts |
| `practice_question` | Practice question |
| `created_at` | Session timestamp |

## Learning Objectives

This project was built to practice:

- Python
- Prompt Engineering
- Role-based prompting
- Structured LLM output
- JSON parsing
- Ollama
- Local LLM usage
- SQLite
- SQL queries
- Python database integration
- Git and GitHub

## Future Improvements

Possible future extensions include:

- Search previous study sessions
- Add a command-line menu
- Filter sessions by topic
- Add difficulty levels
- Generate quizzes
- Track study progress
- Add a web interface

## Author

Sri Hasitha Gudipati

Built as part of an AI/ML learning roadmap and MS Computer Science preparation.