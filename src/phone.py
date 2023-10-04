from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, sim_num):
        super().__init__(name, price, quantity)
        self.sim_num = sim_num

    def __repr__(self):
        s = super().__repr__()
        return s.replace(')', ', ') + f'{self.sim_num})'
