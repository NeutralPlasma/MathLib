import main

def test_add():
    assert main.add(1, 2) == 3
    assert main.add(3, 4) == 7
    assert main.add(5, 6) == 11


def test_sub():
    assert main.subtract(3, 1) == 2
    assert main.subtract(3, -1) == 4
    assert main.subtract(3, 0) == 3
    assert main.subtract(3, 1) == 2


def test_mul():
    assert main.multiply(3, 3) == 9
    assert main.multiply(3, -1) == -3
    assert main.multiply(3, 0) == 0
    assert main.multiply(3, 1) == 3


def test_div():
    assert main.divide(3, 3) == 1
    assert main.divide(3, -1) == -3
    assert main.divide(3, 1) == 3


def test_max():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert main.get_max(array) == 9


def test_min():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert main.get_min(array) == 1


def test_average():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert main.get_average(array) == 5


def test_median():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert main.get_median(array) == 5
    array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
    assert main.get_median(array2) == 5.5


