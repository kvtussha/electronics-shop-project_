import pytest

from src.item import Item


@pytest.mark.raises()
def test_mark_raises_not_found():
    Item.instantiate_from_csv('../src/itemsssss.csv')


@pytest.mark.raises()
def test_mark_raises_broken():
    Item.instantiate_from_csv('../src/my_error/item_wrong.csv')


test_mark_raises_not_found()
test_mark_raises_broken()
