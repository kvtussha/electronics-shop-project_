import pytest
from src.my_error import InstantiateCSVError


@pytest.mark.raises()
def test_mark_raises_not_found():
    raise FileNotFoundError('Отсутствует файл items.csv')


@pytest.mark.raises()
def test_mark_raises_broken():
    raise InstantiateCSVError('Файл items.csv поврежден')


test_mark_raises_not_found()
test_mark_raises_broken()
