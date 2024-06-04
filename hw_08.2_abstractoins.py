class Teacher:  # класс с атрибутами(закрыты)\\ class with attributes(closed)
    def __init__(self, name, experience, discipline, student_name, mark, *args):
        self._name = name
        self._education = ''.join(args)  # преобразование кортежа к строке\\converting a tuple to a string.
        self._experience = experience
        self._discipline = discipline
        self._student_name = student_name
        self._mark = mark

    # Блок Геттеров\\Getter Block
    def get_name(self):
        return self._name

    def get_student_name(self):
        return self._student_name

    def get_mark(self):
        return self._mark

    def get_education(self):
        return self._education

    def get_experience(self):
        return self._experience

    # Блок Сеттеров\\Setter Block
    def set_experience(self, experience):
        self._experience = experience

    def set_mark(self, mark):
        self._mark = mark

    def set_student_name(self, student_name):
        self._student_name = student_name

    # Блок методов\\Methods block
    def teacher_data_out(self):  # вывод информации о преподавателе\
        # \output of information about the teacher
        return f"{self._name}, образование {self._education}, опыт преподавания {self._experience} года/лет"

    def add_mark(self):  # вывод информации о полученной студентом оценке\
        # \output of information about the student's assessment
        return f"Преподаватель {self._name} поставил студенту {self._student_name} оценку {self._mark}"

    def remove_mark(self):  # вывод информации об удалении оценки\
        # \output of information about the deletion of the assessment
        return f"Преподаватель {self._name} удалил у студента {self._student_name} оценку {self._mark}"

    def give_a_consultation(self, group):  # вывод информации о проведении консультации\
        # \conclusion of information about the consultation
        return f"Преподаватель {self._name} провел консультацию в классе {group}"


educat1 = Teacher("Еж Медведович", 4, "Химия", "Вася",
                  3, "ГУАП, курсы йоги, психология")
print(educat1.teacher_data_out())
print(educat1.add_mark())
print(educat1.remove_mark())
print(educat1.give_a_consultation("10A\n\n"))


class DisciplineTeacher(Teacher):  # класс - наследник Teacher\\heir - class Teacher
    def __init__(self, name, experience, discipline, job_title, student_name, mark, education):
        super().__init__(name, experience, discipline, student_name, mark, education)
        self._job_title = job_title  # добавлен атрибут "должность"\\added the "position" attribute"

    # Блок Геттеров\\Getter Block

    def get_discipline(self):  # атрибут заявлен в родительском классе\\the attribute is declared in the parent class
        return self._discipline

    def get_job_title(self):
        return self._job_title

    # Блок Сеттеров\\Setter Block
    def set_job_title(self, job_title):  # смена должности\\change of job_title
        self._job_title = job_title

    def set_discipline(self, discipline):  # смена предмета\\changing the discipline
        self._discipline = discipline

    # Блок методов(полиморфировано из родителя)\\Methods block(
    # polymorphed from the parent)

    def teacher_data_out(self):  # вывод информации о преподавателе\\output of information about the teacher
        return (f"{self._name}, образование {self._education}, опыт преподавания {self._experience} года/лет\n"
                f"Предмет {self._discipline} должность {self._job_title}")

    def add_mark(self):  # вывод информации о полученной студентом оценке\
        # \output of information about the student's assessment
        return (f"Преподаватель {self._name} поставил студенту {self._student_name} оценку {self._mark}\n"
                f"Предмет {self._discipline}")

    def remove_mark(self):  # вывод информации об удалении оценки\
        # \output of information about the deletion of the assessment
        return (f"Преподаватель {self._name} удалил у студента {self._student_name} оценку {self._mark}\n"
                f"Предмет {self._discipline}")

    def give_a_consultation(self, group):  # вывод информации о проведении консультации\
        # \conclusion of information about the consultation
        return (f"Преподаватель {self._name} провел консультацию в классе {group}\nПредмет {self._discipline} "
                f"как {self._job_title}")


educat2 = DisciplineTeacher("Еж Медведович", 4, "Химия", "Директор",
                            "Вася", 3, "ГУАП, курсы йоги, психология")
print(educat2.teacher_data_out())
print(educat2.add_mark())
print(educat2.remove_mark())
print(educat2.give_a_consultation("10A"))

# Проверка работы геттеров\сеттеров\\Checking the operation of getters\setters
educat2.set_mark(5)
educat2.set_discipline("Биология")
print(educat2.add_mark())

educat2.set_mark(2)
educat2.set_discipline("Физика")
print(educat2.remove_mark())

educat2.set_job_title("Уборщик")
print(educat2.give_a_consultation("10Б"))
print(type(educat2.teacher_data_out()))
