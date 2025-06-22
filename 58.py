# coding exercise
student_data = [
    {
        'name': 'sanjana',
        'roll_no': 10,
        'age': 22,
        'course': 'python'
    },
    {
        'name': 'kartik',
        'roll_no': 11,
        'age': 23,
        'course': 'java'
    }
]


def add_new_student(name, roll_no, age, course):
    new_student = {}
    new_student["name"] = name
    new_student["roll_no"] = roll_no
    new_student["age"] = age
    new_student["course"] = course
    student_data.append(new_student)
    print(student_data)


add_new_student("shyam", 12, 23, "c++")
