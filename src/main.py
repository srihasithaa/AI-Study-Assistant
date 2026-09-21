import ollama
import json
import sqlite3

question=input("What do you want to study? Enter the question: ")

with open("./prompts/study_prompt.txt", "r") as prompt_file:
    prompt=prompt_file.read()

response=ollama.chat(
    model="gemma3:4b",
    messages=[
        {
            "role":"user",
            "content":f"""{prompt}
            Question: {question}"""
        }
    ]
)
answer=response["message"]["content"]
answer = answer.replace("```json", "").replace("```", "").strip()

answer_data=json.loads(answer)

# print("\n" + "=" * 60)
# print("                 AI STUDY ASSISTANT")
# print("=" * 60)

# print(f"\nQuestion:")
# print(answer_data["student_question"])

# print(f"\nTopic:")
# print(answer_data["topic"])

# print(f"\nExplanation:")
# print(answer_data["explanation"])

# print(f"\nExample:")
# print(answer_data["example"])

# print(f"\nRelated Concepts:")
# for i, concept in enumerate(answer_data["related_concepts"], start=1):
#     print(f"  {i}. {concept}")

# print(f"\nPractice Question:")
# print(answer_data["practice_question"])

# print("\n" + "=" * 60)

connection = sqlite3.connect("./database/study_assistant.db")
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

print("\nStudy session saved successfully!")