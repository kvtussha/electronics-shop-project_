from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, sim_num):
        super().__init__(name, price, quantity)
        self.sim_num = sim_num

    def __repr__(self):
        s = list(super().__repr__())
        s.insert(28, f', {self.sim_num}')
        return "".join(s)

    def __add__(self, other):
        if issubclass(other, Phone):
            if isinstance(self, Item):
                all_q = Item(self.name, self.price, self.quantity + self.sim_num)
                return all_q
