import inspect

from src.item import Item


def total_price_test():
    tv = Item("Телевизор", 13800, 10)
    phone = Item("Телефон", 8700, 14)
    laptop = Item("Ноутбук", 105000, 18)

    assert tv.calculate_total_price() == 138000, "Функция calculate_total_price работает неправильно"
    assert phone.calculate_total_price() == 121800, "Функция calculate_total_price работает неправильно"
    assert laptop.calculate_total_price() == 1890000, "Функция calculate_total_price работает неправильно"


def apply_discount_test():
    Item.pay_rate = 0.9

    tv = Item("Телевизор", 13800, 10)
    phone = Item("Телефон", 8700, 14)
    laptop = Item("Ноутбук", 105000, 18)

    assert tv.apply_discount() == 12420, "Функция apply_discount работает неправильно"
    assert phone.apply_discount() == 7830, "Функция apply_discount работает неправильно"
    assert laptop.apply_discount() == 94500, "Функция apply_discount работает неправильно"


def string_to_number_test():
    n1 = '5'
    n2 = '3'
    n3 = '8'
    assert type(Item.string_to_number(n1)) == int, "Функция string_to_number работает некорректно"
    assert type(Item.string_to_number(n2)) == int, "Функция string_to_number работает некорректно"
    assert type(Item.string_to_number(n3)) == int, "Функция string_to_number работает некорректно"


def repr_test():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Планшет", 18000, 16)
    item3 = Item("Телевизор", 35000, 13)

    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Планшет', 18000, 16)"
    assert repr(item3) == "Item('Телевизор', 35000, 13)"


def str_test():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Планшет", 18000, 16)
    item3 = Item("Телевизор", 35000, 13)

    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Планшет'
    assert str(item3) == 'Телевизор'


total_price_test()
apply_discount_test()
string_to_number_test()
repr_test()
str_test()
