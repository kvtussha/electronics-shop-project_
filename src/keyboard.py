from src.item import Item


class MixinMode:

    def __init__(self):
        self.language = 'EN'

    @property
    def language(self):
        return self.language

    @language.setter
    def language(self, mode):
        if mode in ['RU', 'EN']:
            if self.language == 'RU':
                self.language = 'EN'
            else:
                self.language = 'RU'

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'


class Keyboard(Item, MixinMode):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
