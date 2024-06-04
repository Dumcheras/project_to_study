class Teachers:
    # блок инициализации\\initialization block
    def __init__(self, teachers_name_surname, job_title, discipline):
        self._teachers_name_surname = teachers_name_surname
        self._job_title = job_title
        self._discipline = discipline

    # Блок Геттеров\\Getter Block

    def get_teachers_name_surname(self):
        return self._teachers_name_surname

    def get_job_title(self):
        return self._job_title

    def get_discipline(self):
        return self._discipline

    # Блок Сеттеров\\Setter Block

    def set_discipline(self, discipline):
        self._discipline = discipline

    def set_job_title(self, job_title):
        self._job_title = job_title


class Students:
    def __init__(self, name_surname, group, discipline, mark):
        self._name_surname = name_surname
        self._group = group
        self._discipline = discipline
        self._mark = mark

    # Блок Геттеров\\Getter Block

    def get_name_surname(self):
        return self._name_surname

    def get_group(self):
        return self._group

    def get_discipline(self):
        return self._discipline

    def get_mark(self):
        return self._mark

        # Блок Сеттеров\\Setter Block

    def set_group(self, group):
        self._group = group

    def set_discipline(self, discipline):
        self._discipline = discipline

    def set_mark(self, mark):
        self._mark = mark


class Consultation(Teachers, Students):
    def __init__(self, teachers_name_surname, name_surname, discipline, mark):
        self._teachers_name_surname = teachers_name_surname
        self._name_surname = name_surname
        self._discipline = discipline
        self._mark = mark

    def make_mark(self):
        return (f"Преподаватель {self._teachers_name_surname} поставил ученику {self._name_surname}"
                f" оценку{self._mark} по предмету{self._discipline}")
