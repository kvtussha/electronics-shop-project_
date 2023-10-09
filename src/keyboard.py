from src.item import Item


class MixinMode:

    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'


class Keyboard(Item, MixinMode):
    language = MixinMode().language

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.language = Keyboard.language


