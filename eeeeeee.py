class Store:
    def __init__(self, a, b, c, d, e):
        self.my_unit = {'тип': a, 'название': b , 'цена': c, 'количество': d, 'единица измерения': e }
        self.store = []

    def reception(self, my_unit):
        self.my_unit = my_unit
        for el in self.store:
            print(el)
            if el.get['тип'] == self.my_unit.get['тип'] and el.get['название'] == self.my_unit.get['название'] \
                    and el.get['цена'] == self.my_unit.get['цена']:
                el['количество']= el.get['количество'] + self.my_unit['количество']
            else:
                self.store.append(self.my_unit)


class Printer:
    def __init__(self, a, b, c):
        self.my_unit = {'тип': 'принтер', 'название': a, 'цена': b, 'количество': c, 'единица измерения': 'шт'}



My_Store= Store('принтер', 'HP', 1000, 5, 'шт')

unit_p = Printer('HP', 1000, 5)
unit_c = Printer('HP', 10, 12)
My_Store.reception(unit_p.my_unit)
My_Store.reception(unit_c.my_unit)
print(My_Store.store)


