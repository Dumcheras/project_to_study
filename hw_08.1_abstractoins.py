class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, ts_type):
        if ts_type == 2:
            return f'Это мотоцикл марки {self.name}.'
        elif ts_type == 3:
            return f'Это трицикл марки {self.name}.'
        elif ts_type == 4:
            return f'Это автомобиль марки {self.name}.'
        else:
            return "Я не знаю таких марок"

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f"Неплохо, {self.name} можно брать"
        elif 50001 < self.mileage < 100000:
            return f"{self.name} надо проверить"
        if 100001 < self.mileage < 150000:
            return f"{self.name} надо провести диагностику"
        if self.mileage > 150000:
            return f"{self.name} Ведро с болтами..."


audi = Vehicle("Audi", 60000)
print(audi.get_vehicle_type(3))
print(audi.get_vehicle_advice(), end="\n\n")

bmv = Vehicle("BMV", 1500000)
print(bmv.get_vehicle_type(2))
print(bmv.get_vehicle_advice(), end="\n\n")

moskvitch = Vehicle("moskvitch", 140000)
print(moskvitch.get_vehicle_type(5))
print(moskvitch.get_vehicle_advice(), end="\n\n")

lotus = Vehicle("Lotus", 0)
print(lotus.get_vehicle_type(4))
print(lotus.get_vehicle_advice(), end="\n\n")


class PersComp:
    def __init__(self, design, tasks, *args):
        self.equipment = ''.join(args).lower()
        self.design = design
        self.tasks = tasks

    def local_users(self, how_many_users):
        if how_many_users == 1:
            return f"\nОдин юзер, комп для {self.tasks}, комплектующие: {self.equipment}"
        elif how_many_users == 2:
            return f"\nДва юзера, нужно разграничить доступ, комп для {self.tasks}, комплектующие: {self.equipment}"
        else:
            return f"\nМного юзеров, нужен локальный админ, комп для {self.tasks}, комплектующие: {self.equipment}"

    def comp_price(self, price):
        if price > 50000:
            return f"Pешит любые задачи, включая задачи {self.tasks}"
        elif 30000 < price < 50000:
            return f"Справится с некоторыми задачами {self.tasks}"
        else:
            return "Гроб с микросхемами"

    def comp_design(self):
        return f"Для задач {self.tasks}, нужны комплектующие: {self.equipment}, в дизайне {self.design}"


logistic = PersComp("Простой короб", "Офисные", "Клавиатура", "Монитор", "МышЪ")

developers = PersComp("Серебряная молния", "Геймер - Про", "Дискретная видеокарта, SSD, Панорамный монитор")

print(logistic.local_users(2))
print(logistic.comp_price(25000))
print(logistic.comp_design())
print()

print(developers.local_users(4))
print(developers.comp_price(65000))
print(developers.comp_design())
