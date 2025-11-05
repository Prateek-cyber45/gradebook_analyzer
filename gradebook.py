# GradeBook – Beginner Friendly Version (Tasks 1–5)

# We only need statistics.median for Task 2
from statistics import median

# ---------------------------
# Task 2: Statistics Functions
# ---------------------------

def calculate_average(marks_dict):
    """Return average of all marks (0.0 if no data)."""
    if not marks_dict:
        return 0.0
    total = sum(marks_dict.values())
    count = len(marks_dict)
    return total / count

def calculate_median(marks_dict):
    """Return median of all marks (0.0 if no data)."""
    if not marks_dict:
        return 0.0
    return float(median(marks_dict.values()))

def find_max_score(marks_dict):
    """Return (name, highest_mark). ('', 0.0) if empty."""
    if not marks_dict:
        return ("", 0.0)
    # max() finds the key (student name) with the biggest value (marks)
    top_student = max(marks_dict, key=marks_dict.get)
    return top_student, marks_dict[top_student]

def find_min_score(marks_dict):
    """Return (name, lowest_mark). ('', 0.0) if empty."""
    if not marks_dict:
        return ("", 0.0)
    low_student = min(marks_dict, key=marks_dict.get)
    return low_student, marks_dict[low_student]

# -------------------------------
# Task 3: Grades + Distribution
# -------------------------------

def grade_for_score(score):
    """Return A/B/C/D/F based on the score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def assign_grades(marks_dict):
    """Make a new dict like {'Alice':'C', ...} for all students."""
    grades = {}
    for name, m in marks_dict.items():
        grades[name] = grade_for_score(m)
    return grades

def grade_distribution(grades_dict):
    """Count how many A/B/C/D/F."""
    dist = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades_dict.values():
        dist[g] += 1
    return dist

# -------------------------------------------------
# Task 4: Pass/Fail (List Comprehensions, pass=40)
# -------------------------------------------------

def pass_fail_lists(marks_dict, threshold=40.0):
    # Required: use list comprehensions
    passed = [name for name, m in marks_dict.items() if m >= threshold]
    failed = [name for name, m in marks_dict.items() if m < threshold]
    return passed, failed

# ---------------------------
# Task 1: Manual Data Entry
# ---------------------------

def input_marks():
    """
    Ask: how many students?
    Then for each student: name and marks (0–100).
    Return a dictionary like: {'Alice': 78, 'Bob': 92}
    """
    marks = {}
    while True:
        try:
            n = int(input("How many students? "))
            if n < 0:
                print("Please enter 0 or a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a whole number like 0, 1, 2, ...")

    for i in range(1, n + 1):
        # get a non-empty name
        while True:
            name = input(f"Enter name for student {i}: ").strip()
            if name != "":
                break
            print("Name cannot be empty. Try again.")
        # get a valid mark between 0 and 100
        while True:
            try:
                m = float(input(f"Enter marks for {name} (0-100): ").strip())
                if 0 <= m <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please type a number like 75 or 89.5")
        marks[name] = m

    return marks

# -----------------------------------------
# Task 5: Results Table + Menu (looped UI)
# -----------------------------------------

def print_table(marks_dict):
    """Show: Name Marks Grade (simple table)."""
    if not marks_dict:
        print("\nNo records to display yet. Please add students first.")
        return

    grades = assign_grades(marks_dict)

    print("\nName Marks Grade")
    print("-------------------- ------ -----")
    # keep original order (very beginner-friendly)
    for name in marks_dict:
        score = marks_dict[name]
        g = grades[name]
        print(f"{name:<20} {score:>6.2f} {g:^5}")

def print_statistics(marks_dict):
    """Print average, median, max and min in a neat way."""
    avg = calculate_average(marks_dict)
    med = calculate_median(marks_dict)
    top_name, top_score = find_max_score(marks_dict)
    low_name, low_score = find_min_score(marks_dict)

    print("\n=== Statistics ===")
    print(f"Total students : {len(marks_dict)}")
    print(f"Average : {avg:.2f}")
    print(f"Median : {med:.2f}")
    if marks_dict:
        print(f"Highest : {top_score:.2f} ({top_name})")
        print(f"Lowest : {low_score:.2f} ({low_name})")

def print_grade_summary(marks_dict):
    """Show grade counts A/B/C/D/F."""
    if not marks_dict:
        print("\nNo data to grade yet.")
        return
    grades = assign_grades(marks_dict)
    dist = grade_distribution(grades)

    print("\n=== Grade Summary ===")
    print(f"A : {dist['A']}")
    print(f"B : {dist['B']}")
    print(f"C : {dist['C']}")
    print(f"D : {dist['D']}")
    print(f"F : {dist['F']}")

def print_pass_fail(marks_dict, threshold=40.0):
    """Show passed/failed names and how many in each."""
    passed, failed = pass_fail_lists(marks_dict, threshold)
    print(f"\n=== Pass/Fail (Pass if >= {threshold}) ===")
    print("Passed (count {}):".format(len(passed)), ", ".join(passed) if passed else "None")
    print("Failed (count {}):".format(len(failed)), ", ".join(failed) if failed else "None")

def main():
    # This will store everything while the program runs
    marks = {}

    while True:
        print("\n========== GradeBook Menu ==========")
        print("1. Enter student data (Task 1)")
        print("2. Show statistics (Task 2)")
        print("3. Show grades + counts (Task 3)")
        print("4. Show pass/fail lists (Task 4, pass=40)")
        print("5. Show results table (Task 5)")
        print("6. Exit")
        choice = input("Choose [1-6]: ").strip()

        if choice == "1":
            new_data = input_marks() # get data from user
            marks.update(new_data) # merge into our main dictionary
            print("Current marks:", marks) # show what's stored (deliverable proof)

        elif choice == "2":
            print_statistics(marks)

        elif choice == "3":
            print_grade_summary(marks)

        elif choice == "4":
            print_pass_fail(marks, threshold=40.0)

        elif choice == "5":
            print_table(marks)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 6.")

if __name__ == "__main__":
    main()
