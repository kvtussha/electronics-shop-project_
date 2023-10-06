from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, _sim_num):
        super().__init__(name, price, quantity)
        self._sim_num = _sim_num

    @property
    def sim_num(self):
        return self._sim_num

    @sim_num.setter
    def sim_num(self, value):
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self._sim_num = value

    def __repr__(self):
        s = super().__repr__()
        return s.replace(')', ', ') + f'{self.sim_num})'
