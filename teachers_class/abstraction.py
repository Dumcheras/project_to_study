class Teachers:
    # блок инициализации\\initialization block
    def __init__(self, name_surname, job_title, discipline):
        self._name_surname = name_surname
        self._job_title = job_title
        self._discipline = discipline

    # Блок Геттеров\\Getter Block

    def get_name_surname(self):
        return self._name_surname

    def get_job_title(self):
        return self._job_title

    def get_discipline(self):
        return self._discipline

    # Блок Сеттеров\\Setter Block

    def set_experience(self, discipline):
        self._discipline = discipline

    def set_job_title(self, job_title):
        self._job_title = job_title


class Students:
    def __init__(self, name_surname, group, discipline, mark):
        self._name_surname = name_surname
        self._group = group
        self._discipline = discipline
        self._mark = mark
