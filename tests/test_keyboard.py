from src.keyboard import Keyboard

kb1 = Keyboard('Keyboard 1', 10870, 5)
kb2 = Keyboard('Keyboard 2', 6508, 13)


def test_keyboard():
    assert str(kb1) == "Keyboard 1"
    assert str(kb2) == "Keyboard 2"

    assert kb1.language == 'EN'
    assert kb2.language == 'EN'

    kb1.change_lang()
    assert str(kb1.language) == "RU"

    kb1.change_lang()
    assert str(kb1.language) == "EN"

    kb2.change_lang()
    assert str(kb2.language) == "RU"

    kb2.change_lang()
    assert str(kb2.language) == "EN"


test_keyboard()
