import os
import pytest
import flask

app = flask.Flask(__name__)

with app.test_request_context('/'):
    assert flask.request.path == '/'

with app.test_request_context('/result'):
    assert flask.request.path == '/result'
    assert flask.request.args['messages'] == []

with app.test_request_context('/test'):
    assert flask.request.path == '/test'
