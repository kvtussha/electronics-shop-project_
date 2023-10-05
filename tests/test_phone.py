from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 1)
phone2 = Phone("iPhone 13", 100_000, 7, 2)
phone3 = Phone("iPhone 12", 89_000, 6, 3)


def sim_num_test():
    assert phone1.sim_num == 1
    assert phone2.sim_num == 2
    assert phone3.sim_num == 3


def repr_test():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 1)"
    assert repr(phone1) == "Phone('iPhone 13', 100000, 7, 2)"
    assert repr(phone1) == "Phone('iPhone 12', 89000, 6, 3)"
