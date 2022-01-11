import pytest
from src.application import app


@pytest.fixture
def appToTest():
    testApp = app()
    yield testApp
