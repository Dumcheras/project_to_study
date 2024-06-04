class Teacher:  # класс с атрибутами(закрыты)\\ class with attributes(closed)
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience

        # Блок Геттеров\\Getter Block

    def get_name(self):
        return self._name

    def get_education(self):
        return self._education

    def get_experience(self):
        return self._experience

        # Блок Сеттеров\\Setter Block

    def set_experience(self, experience):
        self._experience = experience

    # Блок методов\\Methods block
    def get_teacher_data(self):
        return f"{self._name}, образование {self._education}, опыт преподавания {self._experience} года/лет"

    def add_mark(self, mark, student_name):  # вывод информации о полученной студентом оценке\
        # \output of information about the student's assessment
        return f"Преподаватель {self._name} поставил студенту {student_name} оценку {mark}"

    def remove_mark(self, mark, student_name):  # вывод информации об удалении оценки\
        # \output of information about the deletion of the assessment
        return f"Преподаватель {self._name} удалил у студента {student_name} оценку {mark}"

    def give_a_consultation(self, group):  # вывод информации о проведении консультации\
        # \conclusion of information about the consultation
        return f"Преподаватель {self._name} провел консультацию в классе {group}"


educat1 = Teacher("Еж Медведович", "ГУАП", 3)
print(educat1.get_teacher_data())
print(educat1.add_mark(4, "Вася"))
print(educat1.remove_mark(4, "Вася"))
print(educat1.give_a_consultation("10A\n\n"))


class DisciplineTeacher(Teacher):  # класс - наследник Teacher\\heir - class Teacher
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._job_title = job_title  # добавлен атрибут "должность"\\added the "position" attribute"
        self._discipline = discipline  # добавлен атрибут "дисциплина"\\added the "discipline" attribute"

    # Блок Геттеров\\Getter Block

    def get_discipline(self):
        return self._discipline

    def get_job_title(self):
        return self._job_title

    # Блок Сеттеров\\Setter Block
    def set_job_title(self, job_title):  # смена должности\\change of job_title
        self._job_title = job_title

    # Блок методов\\Methods block
    def get_teacher_data(self):
        return f"{super().get_teacher_data()}\nпредмет {self._discipline} должность {self._job_title}"

    def add_mark(self, mark, student_name):
        return f"{super().add_mark(mark, student_name)}\nпредмет {self._discipline}"

    def remove_mark(self, mark, student_name):
        return f"{super().add_mark(mark, student_name)}\nпредмет {self._discipline}"

    def give_a_consultation(self, group):
        return f"{super().give_a_consultation(group)}как {self._job_title} по предмету {self._discipline}"


educat2 = DisciplineTeacher("Еж Медведович", "ГУАП", 3, "Химия", "Директор")
print(educat2.get_teacher_data())
print(educat2.add_mark(4, "Вася"))
print(educat2.remove_mark(4, "Вася"))
print(educat2.give_a_consultation("10A\n"))
