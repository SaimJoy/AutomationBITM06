import pytest

@pytest.yield_fixture()
def browser_config():
    print("chrome Launch succesfull")

    yield
    print("browser close")

def test_valid_login(browser_config):
    print("valid Login Success")

def test_invalid_login(browser_config):
    print("invalid login succesfull")