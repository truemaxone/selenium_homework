import pytest


@pytest.fixture(scope="module")
def set_module():
    print("\nEnter testing system")
    yield
    print("\nExit testing system")
