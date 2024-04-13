import pytest

from blog.app import app as _app

@pytest.fixture()
def app():
    _app.config.update({
        "TESTING": True
    })
    return _app

@pytest.fixture()
def client(app):
    return app.test_client()
