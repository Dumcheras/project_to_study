from abstraction2 import Student

teacher = "Петр"
students = "Иван"
marks = 2
discipline = "Химия"
group = "10A"

st1 = Student(students, marks, discipline, group)
print(st1.student_taken_mark())
st2 = Student(teacher, students, marks, discipline)
print(st2.teacher_data())
