class Item:
    pay_rate = 0
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

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
