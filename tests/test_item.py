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


total_price_test()
apply_discount_test()