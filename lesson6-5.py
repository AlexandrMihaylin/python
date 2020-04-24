class Stationery:
    def __init__(self, title='Производитель письменной принадлежности'):
        self.title = title

    def draw(self):
        print(f'Начинаем рисовать {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')


a = Stationery()
a.draw()
pen = Pen("Stabilo")
pen.draw()
pencil = Pencil("Caran d'Ache Ecridor")
pencil.draw()
handle = Handle("Berlingo")
handle.draw()
