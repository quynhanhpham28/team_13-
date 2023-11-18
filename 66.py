grade_points = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}


total_grade_points = 0.0
num_grades = 0


while True:
    grade = input("Enter a letter grade (or blank line to finish): ")
   
    if grade == "":
        break
   
    if grade in grade_points:
        total_grade_points += grade_points[grade]
        num_grades += 1


if num_grades > 0:
    gpa = round(total_grade_points / num_grades, 2)
    print("Grade Point Average:", gpa)
else:
    print("No grades entered.")
