class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name}{self.surname}'
    def get_total_income(self):
        return f'{sum(self.income.values())}'

manager=Position('Василий','Тёркин','CTO', 70000, 30000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_total_income())
