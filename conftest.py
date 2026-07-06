import pytest
from app import LoiqdevFrameApp


@pytest.fixture
def app():
    return LoiqdevFrameApp()

@pytest.fixture
def test_client(app):
    return app.test_session()