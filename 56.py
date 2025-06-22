# coding exercise
student_marks = {
    "jenny": 92,
    "harry": 78,
    "dimpy": 56,
    "rahul": 41,
    "kartik": 99,
    "prem": 34,
    "sanjana": 100
}
"""marks grades
   91-100  A+
   81-90   A
   71-80   B+
   61-70   B
   51=60   C
   41-50   D
   below 40 F
"""
student_grades = {}
for student in student_marks:
    marks = student_marks[student]
    if marks > 90:
        student_grades[student] = 'A+'
    elif marks > 80:
        student_grades[student] = 'A'
    elif marks > 70:
        student_grades[student] = 'B+'
    elif marks > 60:
        student_grades[student] = 'B'
    elif marks > 50:
        student_grades[student] = 'C'
    else:
        student_grades[student] = 'Fail'
print(student_grades)
