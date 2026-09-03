import json
import os

# Master list for in-memory persistence
students = []

def compute_grade(marks):
    """Calculates letter grade based on numerical marks[cite: 1]."""
    if marks >= 85.0:
        return "A"
    elif marks >= 70.0:
        return "B"
    elif marks >= 50.0:
        return "C"
    else:
        return "F"

def get_next_id():
    """Generates a unique incremental ID for new records[cite: 1]."""
    if not students:
        return 1
    return max(s["id"] for s in students) + 1

def enroll_student():
    """Module A: Student Enrollment & Grade Evaluation Engine"""
    print("\n--- Enroll New Student ---")
    
    while True:
        name = input("Enter Student Name: ").strip()
        if name:
            break
        print("Error: Name cannot be empty.")
        
    while True:
        course = input("Enter Course Name: ").strip()
        if course:
            break
        print("Error: Course cannot be empty.")
        
    while True:
        try:
            marks = float(input("Enter Marks (0.0 - 100.0): "))
            if 0.0 <= marks <= 100.0:
                break
            print("Error: Marks must be between 0.0 and 100.0.")
        except ValueError:
            print("Error: Invalid numerical input for marks.")

    student_id = get_next_id()
    grade = compute_grade(marks)

    record = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": round(marks, 2),
        "grade": grade
    }
    
    students.append(record)
    print(f"\nStudent successfully enrolled with ID: {student_id} | Grade: {grade}")

def display_cohort_directory():
    """Module B: Cohort Tabular Reporting"""
    print("\n--- Cohort Directory ---")
    if not students:
        print("No student records found in memory.")
        return

    print("-" * 65)
    print(f"{'ID':<6} | {'Name':<20} | {'Course':<18} | {'Marks':<8} | {'Grade':<5}")
    print("-" * 65)
    for s in students:
        print(f"{s['id']:<6} | {s['name']:<20} | {s['course']:<18} | {s['marks']:<8.2f} | {s['grade']:<5}")
    print("-" * 65)

def query_records():
    """Module B: Multi-Criteria Search System"""
    print("\n--- Query Records ---")
    if not students:
        print("No student records available to search.")
        return

    query = input("Enter Student ID, Name, or Course to search: ").strip()
    if not query:
        print("Search query cannot be empty.")
        return

    results = []
    
    # Try ID search first
    if query.isdigit():
        target_id = int(query)
        results = [s for s in students if s["id"] == target_id]
    
    # If no ID match or query is string, perform substring match
    if not results:
        q_lower = query.lower()
        results = [s for s in students if q_lower in s["name"].lower() or q_lower in s["course"].lower()]

    if results:
        print(f"\nFound {len(results)} matching record(s):")
        print("-" * 65)
        print(f"{'ID':<6} | {'Name':<20} | {'Course':<18} | {'Marks':<8} | {'Grade':<5}")
        print("-" * 65)
        for s in results:
            print(f"{s['id']:<6} | {s['name']:<20} | {s['course']:<18} | {s['marks']:<8.2f} | {s['grade']:<5}")
        print("-" * 65)
    else:
        print("No records found matching criteria.")

def revise_evaluation():
    """Module C: Record Mutation with Auto-recalculated Grade"""
    print("\n--- Revise Student Record ---")
    try:
        student_id = int(input("Enter Student ID to update: "))
    except ValueError:
        print("Error: Invalid Student ID format.")
        return

    record = next((s for s in students if s["id"] == student_id), None)
    if not record:
        print(f"Error: No student found with ID {student_id}.")
        return

    print(f"Updating Record for: ID {record['id']} - {record['name']}")
    
    new_name = input(f"Enter New Name (Press Enter to keep '{record['name']}'): ").strip()
    if new_name:
        record["name"] = new_name

    new_course = input(f"Enter New Course (Press Enter to keep '{record['course']}'): ").strip()
    if new_course:
        record["course"] = new_course

    new_marks_str = input(f"Enter New Marks (Press Enter to keep '{record['marks']}'): ").strip()
    if new_marks_str:
        try:
            new_marks = float(new_marks_str)
            if 0.0 <= new_marks <= 100.0:
                record["marks"] = round(new_marks, 2)
                record["grade"] = compute_grade(new_marks) # Auto recompute grade
            else:
                print("Error: Marks out of range (0-100). Marks remain unchanged.")
        except ValueError:
            print("Error: Invalid numerical value. Marks remain unchanged.")

    print(f"Record ID {student_id} revised successfully!")

def purge_record():
    """Module C: Record Deletion with Confirmation"""
    print("\n--- Purge Student Record ---")
    try:
        student_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Error: Invalid Student ID format.")
        return

    record = next((s for s in students if s["id"] == student_id), None)
    if not record:
        print(f"Error: No student found with ID {student_id}.")
        return

    print(f"Record Details: ID {record['id']} | Name: {record['name']} | Course: {record['course']} | Grade: {record['grade']}")
    confirm = input("Are you sure you want to purge this record? (y/n): ").strip().lower()
    
    if confirm == 'y':
        students.remove(record)
        print(f"Record ID {student_id} purged successfully.")
    else:
        print("Purge operation cancelled.")

def save_to_json(filename="students.json"):
    """Module C: JSON Serialization[cite: 1]"""
    try:
        with open(filename, "w") as f:
            json.dump(students, f, indent=4) # indent=4 requirement
        print(f"Data successfully saved to '{filename}'. Total records: {len(students)}")
    except Exception as e:
        print(f"Error: Failed to save file - {e}")

def load_from_json(filename="students.json"):
    """Module C: JSON Deserialization[cite: 1]"""
    global students
    if not os.path.exists(filename):
        print(f"Warning: '{filename}' not found. No data loaded.")
        return

    try:
        with open(filename, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                students = data
                print(f"Data successfully loaded from '{filename}'. Total records: {len(students)}")
            else:
                print("Error: File payload must be a JSON array/list.")
    except json.JSONDecodeError:
        print(f"Error: '{filename}' contains malformed or invalid JSON structure.")
    except Exception as e:
        print(f"Error loading file: {e}")

def main():
    """Main CLI Execution Loop"""
    while True:
        print("\n" + "=" * 45)
        print("  STUDENT GRADE & ASSESSMENT MANAGEMENT SYSTEM")
        print("=" * 45)
        print("[1] Enroll Student")
        print("[2] Cohort Directory")
        print("[3] Query Records")
        print("[4] Revise Evaluation")
        print("[5] Purge Record")
        print("[6] Save to JSON")
        print("[7] Load from JSON")
        print("[8] Terminate")
        print("=" * 45)
        
        choice = input("Select an option (1-8): ").strip()
        
        if choice == '1':
            enroll_student()
        elif choice == '2':
            display_cohort_directory()
        elif choice == '3':
            query_records()
        elif choice == '4':
            revise_evaluation()
        elif choice == '5':
            purge_record()
        elif choice == '6':
            save_to_json()
        elif choice == '7':
            load_from_json()
        elif choice == '8':
            print("Terminating application. Goodbye!")
            break
        else:
            print("Error: Invalid menu choice. Please select an option between 1 and 8.")

if __name__ == "__main__":
    main()