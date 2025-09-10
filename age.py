while True:
    name = input("\nEnter student name: ")
  # Optional: To make it easier to exit the program
  if name.lower() == 'exit':
    break


  while True:
    try:
      score = int(input("Enter score (0-100): "))
      if 0 <= score <= 100:
        break
      print("Score must be between 0 and 100.")
    except ValueError:
      print("Invalid input. Score must be a number.")
  
  while True:
    try:
      absences = int(input("Enter absences (max 5): "))
      if 0 <= absences <= 5:
        break
      print("Absences must be between 0 and 5.")
    except ValueError:
      print("Invalid input. Absences must be a number.")


  # Check the grade and remarks based on the score
  if score >= 90:
    grade, remarks = "A", "Excellent"
  elif score >= 80:
    grade, remarks = "B", "Good job"
  elif score >= 70:
    grade, remarks = "C", "Needs Improvement"
  elif score >= 60:
    grade, remarks = "D", "On Probation"
  else:
    grade, remarks = "F", "Failed"


  # Collect all the reasons for failure in one list


  fail_reasons = []
  if absences > 5:
    fail_reasons.append("Too many absences.")
  if score < 70:
    fail_reasons.append(f"Grade is {grade}.")
    
  # Determine the status and generate the string for the failure reason
  if fail_reasons:
    status = "Failed"
    fail_reason = " and ".join(fail_reasons)
  else:
    status = "Passed"
    fail_reason = None # There is no reason to pass
  
  print("\n--- Student Report ---")
  print(f"Name: {name}")
  print(f"Score: {score}")
  print(f"Grade: {grade}")
  print(f"Absences: {absences}")
  print(f"Status: {status}")
  if fail_reason: # Will only print if there is a reason for failure.
    print(f"Reason for failure: {fail_reason}")
  print(f"Remarks: {remarks}")
  print("----------------------")


  if input("Check another grade? (yes/no): ").lower() != "yes":
    print("System Ended.")
    break