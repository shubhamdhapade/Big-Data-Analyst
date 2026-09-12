'''
    Structured CSV & JSON Data Processor
    Scenario
    An academic registrar stores student course registrations in a CSV file. You need to read this file, compute overall 
    statistics, and export a summarized JSON report.

    Problem Description
    Create a function process_student_records(input_csv_path, output_json_path):
    Reads an input_csv_path containing columns: student_id, name, course, score.
    Uses csv.DictReader inside a context manager to parse all rows.
    Computes:
    total_students: Total number of students processed.
    average_score: Arithmetic mean of all student scores (rounded to 2 decimal places).
    top_scorer: The dictionary {"name": <name>, "score": <score>} of the highest scoring student.
    course_counts: A dictionary mapping each course name to the count of enrolled students.
    Writes the summary dictionary into output_json_path formatted with an indentation of 4 spaces using json.dump().
    Example Walkthrough
    # Given input CSV:
    # student_id,name,course,score
    # 101,Arham,AI,88.5
    # 102,Lisa,BDA,94.0
    # 103,Vinod,AI,96.5

    process_student_records("students.csv", "summary.json")

    # Expected summary.json output:
    # {
    #     "total_students": 3,
    #     "average_score": 93.0,
    #     "top_scorer": {
    #         "name": "Vinod",
    #         "score": 96.5
    #     },
    #     "course_counts": {
    #         "AI": 2,
    #         "BDA": 1
    #     }
    # }
'''

import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_NAME = os.path.join(BASE_DIR, "students.csv")
JSON_FILE_NAME = os.path.join(BASE_DIR, "summary.json")

def process_student_records(input_csv_path, output_json_path):
    total_students = 0
    total_scores = 0.0
    top_scorer = {"name": "", "score": float('-inf')}
    course_counts = {}
    average_score = 0.0

    with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_students += 1
            score = float(row['score'])
            total_scores += score
            
            # Update top scorer
            if score > top_scorer['score']:
                top_scorer['name'] = row['name']
                top_scorer['score'] = score
            
            # Count enrollments per course
            course = row['course']
            course_counts[course] = course_counts.get(course, 0) + 1

    # Calculate average score if records exist
    if total_students > 0:
        average_score = round(total_scores / total_students, 2)
    else:
        top_scorer = {"name": None, "score": 0.0}

    # Construct the summary report
    summary = {
        "total_students": total_students,
        "average_score": average_score,
        "top_scorer": top_scorer,
        "course_counts": course_counts
    }

    # Export to JSON
    with open(output_json_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(summary, jsonfile, indent=4)


def main():
    # Helper to generate dummy CSV file for test execution
    if not os.path.exists(CSV_FILE_NAME):
        sample_data = [
            ["student_id", "name", "course", "score"],
            ["101", "Arham", "AI", "88.5"],
            ["102", "Lisa", "BDA", "94.0"],
            ["103", "Vinod", "AI", "96.5"]
        ]
        with open(CSV_FILE_NAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(sample_data)

    process_student_records(CSV_FILE_NAME, JSON_FILE_NAME)
    print(f"Processed {CSV_FILE_NAME} and generated summary in {JSON_FILE_NAME}.")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' Structured CSV & JSON Data Processor ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)