student_grade_scores = {
    "Haley": 87,
    "Kunal": 79,
    "Parker": 67,
    "lexi": 81,
    "Abby": 83
}

# creating an empty dictionary to collect the new values

student_grades = {}

for student in student_grade_scores:
    score = student_grade_scores[student]

if score >= 91:
    student_grades[student] = "Grade A"
elif score >= 81:
    student_grades[student] = "Grade B"
elif score >= 71:
    student_grades[student] = "Grade C"
elif score >= 61:
    student_grades[student] = "Grade D"
else:
    student_grades[student] = "Grade F"


print(student_grades)