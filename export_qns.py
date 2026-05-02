import json
import csv
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILES = ["js/exam1.json", "js/exam2.json"]
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "questions_export.csv")

rows = []

for json_path in JSON_FILES:
    full_path = os.path.join(SCRIPT_DIR, json_path)
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    exam = data["metadata"]["exam"]
    source = os.path.basename(json_path)

    for q in data["questions"]:
        options = "\n".join(f'{opt["id"]}) {opt["text"]}' for opt in q["options"])
        correct = ", ".join(q["correctAnswers"])
        rows.append([
            exam,
            q["topic"],
            q["difficulty"],
            q["question"],
            options,
            correct,
            q["explanation"],
            source,
        ])

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Exam", "Topic", "Difficulty", "Question", "Options", "Correct Answers", "Explanation", "Source"])
    writer.writerows(rows)

print(f"Exported {len(rows)} questions to {OUTPUT_FILE}")
