from src.item import Item


class MixinMode:

    def __init__(self):
        self._langs = {"EN": "EN", "RU": "RU"}
        self._language = "EN"

    @property
    def language(self):
        return self._language

    def change_lang(self, mode):
        if mode in self._langs:
            self._language = self._langs[mode]
        else:
            raise ValueError("Язык не поддерживается")


class Keyboard(Item, MixinMode):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinMode.__init__(self)
