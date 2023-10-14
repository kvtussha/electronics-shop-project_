from src.item import Item


def test_error():
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл items.csv

    # В файле items.csv удалена первая колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл items.csv поврежден

    # В файле items.csv удалена вторая колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл items.csv поврежден

    # В файле items.csv удалена третья колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл items.csv поврежден

    # Файл items.csv содержит все данные и программа работает.
    Item.instantiate_from_csv()
    # Инициализация экземпляров класса прошла успешно!
