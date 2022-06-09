import pytest

@pytest.fixture()
def partitura_fake() -> str:
    return '12345678'

@pytest.fixture()
def instrumento_fake() -> str:
    return 'test_instrumento'
