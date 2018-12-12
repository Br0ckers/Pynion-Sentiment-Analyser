import os
import tempfile
import pytest
import flask


app = flask.Flask(__name__)

@pytest.fixture
def happenseverytime():
    pass

with app.test_request_context('/'):
    assert flask.request.path == '/'
    #assert flask.request.args['name'] == 'Peter'

with app.test_request_context('/test'):
    assert flask.request.path == '/test'
    #assert flask.request.args['name'] == 'Peter'
