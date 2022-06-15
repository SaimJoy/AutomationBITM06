import pytest

@pytest.mark.order(4)
def test_method1():
    print('hello')

@pytest.mark.order(3)
def test_method2():
    print('Hello Dhaka')

@pytest.mark.order(2)
def test_method3():
    print('hello Bitm')

@pytest.mark.order(1)
def test_method4():
    print('Hello PnT')