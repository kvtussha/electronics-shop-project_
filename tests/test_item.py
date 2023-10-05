from src.item import Item
from src.phone import Phone

tv = Item("Телевизор", 13800, 10)
phone = Item("Телефон", 8700, 14)
laptop = Item("Ноутбук", 105000, 18)

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Планшет", 18000, 16)
item3 = Item("Телевизор", 35000, 13)


def total_price_test():
    assert tv.calculate_total_price() == 138000, "Функция calculate_total_price работает неправильно"
    assert phone.calculate_total_price() == 121800, "Функция calculate_total_price работает неправильно"
    assert laptop.calculate_total_price() == 1890000, "Функция calculate_total_price работает неправильно"


def apply_discount_test():
    Item.pay_rate = 0.9

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
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Планшет', 18000, 16)"
    assert repr(item3) == "Item('Телевизор', 35000, 13)"


def str_test():
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Планшет'
    assert str(item3) == 'Телевизор'


def add_test():
    phone1 = Phone("iPhone 14", 120_000, 5, 1)
    phone2 = Phone("iPhone 14", 100_000, 7, 2)
    phone3 = Phone("iPhone 14", 89_000, 6, 3)

    assert phone1 + item1 == 25
    assert phone2 + item2 == 23
    assert phone3 + item3 == 19


total_price_test()
apply_discount_test()
string_to_number_test()
repr_test()
str_test()
add_test()
