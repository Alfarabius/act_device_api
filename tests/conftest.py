import pytest


@pytest.fixture(scope="session")
def is_true():
    return True
