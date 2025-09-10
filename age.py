# Student Grading and Absences System.py

while True:
    name = input("\nStudent name: ")

    while True:
        try:
            grade = int(input("Enter grade (0–100): "))
            if 0 <= grade <= 100:
                break
            print("Grade must be between 0 and 100.")
        except:
            print("Please enter a number.")

    while True:
        try:
            absences = int(input("How many absences? (max 5): "))
            if absences >= 0:
                break
            print("Absences can't be negative.")
        except:
            print("Please enter a number.")

    # Determine letter grade
    if grade < 60:
        letter = 'F'
    elif grade <= 69:
        letter = 'E'
    elif grade <= 79:
        letter = 'C'
    elif grade <= 89:
        letter = 'D'
    else:
        letter = 'A'

    # Pass/fail check
    passed = letter in ['A', 'B', 'C'] and absences <= 5
    status = "Passed" if passed else "Failed"

    # Remarks (using match, Python 3.10+)
    match letter:
        case 'A': remark = "Excellent"
        case 'B': remark = "Good job"
        case 'C': remark = "Needs Improvement"
        case 'D': remark = "On probation"
        case 'F': remark = "Failed"
        case _: remark = "Invalid grade"

    # Output result
    print(f"\n--- Result for {name} ---")
    print(f"Grade: {grade} → {letter}")
    print(f"Absences: {absences}")
    print(f"Status: {status}")
    print(f"Remarks: {remark}")
    print("------------------------")

    # Continue?
    again = input("Check another student? (yes/no): ").lower()
    if again != 'yes':
        break

# End message with while loop
while True:
    print("\nThanks for using the system. Goodbye!")
    break
