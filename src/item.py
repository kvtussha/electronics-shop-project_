import csv

from src.my_error import InstantiateCSVError


class Item:
    pay_rate = 0
    all = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return str(self.__name)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name > 10):
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    def calculate_total_price(self) -> [int, float]:
        """
        Метод считает, сколько будут стоить все единицы определенного товара в магазине
        :return: общая цена
        """
        return round(self.price * self.quantity, 2)

    def apply_discount(self) -> [int, float]:
        """
        Метод считает цену с учетом скидки
        :return: итоговая цена
        """
        self.price = round(self.price * Item.pay_rate)
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        """
        Метод считывает данные из "items.csv" и инициализирует экземпляры класса со значениями из файла
        :return: итоговая цена
        """
        try:
            with open('../src/items.csv', encoding='utf-8') as f:
                dict_reader = csv.DictReader(f)
                try:
                    for row in dict_reader:
                        name, price, quantity = row['name'], row['price'], row['quantity']
                        cls(name, price, quantity)
                except Exception:
                    raise InstantiateCSVError()
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        else:
            return "Инициализация экземпляров класса прошла успешно!"

    @staticmethod
    def string_to_number(num):
        """
        Метод преобразовывает число в виде строки в число
        :return: преобразованное число
        """
        return int(num)
