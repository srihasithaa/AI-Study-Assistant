import json
import ollama
from database import create_table, save_session, get_previous_sessions


# Create database table
create_table()

# Get student's question
question = input("What do you want to study? Enter the question: ")

# Load study prompt
with open("./prompts/study_prompt.txt", "r") as prompt_file:
    prompt = prompt_file.read()

# Send question to Gemma
response = ollama.chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": f"""{prompt}
Question: {question}"""
        }
    ]
)

# Get model response
answer = response["message"]["content"]

# Remove Markdown code fences if returned by the model
answer = answer.replace("```json", "").replace("```", "").strip()


# Convert JSON response into Python dictionary
answer_data = json.loads(answer)

# Display AI response
print("\n" + "=" * 60)
print("                 AI STUDY ASSISTANT")
print("=" * 60)

print("\nQuestion:")
print(answer_data["student_question"])

print("\nTopic:")
print(answer_data["topic"])

print("\nExplanation:")
print(answer_data["explanation"])

print("\nExample:")
print(answer_data["example"])

print("\nRelated Concepts:")

for i, concept in enumerate(answer_data["related_concepts"], start=1):
    print(f"  {i}. {concept}")

print("\nPractice Question:")
print(answer_data["practice_question"])

print("\n" + "=" * 60)

# Save study session
save_session(answer_data)

print("\nStudy session saved successfully!")

# Display previous study sessions
sessions = get_previous_sessions()

print("\nPrevious Study Sessions")
print("=" * 60)

for session in sessions:
    print(f"\n{session[0]}. {session[2]}")
    print(f"   Question: {session[1]}")
    print(f"   Date: {session[3]}")

print()