'''
    Grading on a Curve
    Scenario: A professor wants to adjust exam grades. Prompt the user to enter a list of space-separated test scores. 
    Convert them to a list of integers. Using a single list comprehension with conditionals, apply the following curve rules:
    
    If a score is below 50, add 10 points.
    If a score is 50 or higher, add 5 points.
    The maximum possible score is capped at 100 (e.g., a score of 98 becomes 100, not 103). Print the original and the curved grades.
    Sample Input: "45 88 30 98 50"
    Sample Output:
    Original: [45, 88, 30, 98, 50]
    Curved: [55, 93, 40, 100, 55]
'''
import os

def curve_grades(scores: list[int]) -> list[int]:
    return [min(100, score + 10) if score < 50 else min(100, score + 5) for score in scores]

def main():
    raw_input = input("Enter space-separated test scores: ").strip()
    if not raw_input:
        print("No scores entered!")
        return

    try:
        original_scores = [int(score) for score in raw_input.split()]
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return

    curved_scores = curve_grades(original_scores)

    print(f"Original: {original_scores}")
    print(f"Curved:   {curved_scores}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' Grading on a Curve ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)