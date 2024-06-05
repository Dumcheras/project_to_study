class ClassMagazine:
    def __init__(self, teacher, students, marks, discipline):
        self.teacher = teacher
        self.students = students
        self.marks = marks
        self.discipline = discipline

    def teacher_data(self):
        return (f"{self.teacher} поставил студенту {self.students} "
                f"оценку {self.marks} по предмету {self.discipline}")


class Student(ClassMagazine):
    def __init__(self, students, marks, discipline, group):
        super().__init__(None, students, marks, discipline)
        self.group = group

    def student_taken_mark(self):
        return (f"Студент {self.students} {self.group} класса "
                f"получил {self.marks} по предмету {self.discipline}")

    def student_retaken_mark(self):
        return (f"Студент {self.students} {self.group} класса"
                f"исправил оценку на {self.marks} по предмету {self.discipline}")
