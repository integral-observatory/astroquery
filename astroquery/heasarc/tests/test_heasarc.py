# Licensed under a 3-clause BSD style license - see LICENSE.rst
import os
import pytest
import requests

DATA_FILES = {
    'mission_list': ''
}

class MockResponse(object):

    def __init__(self, content):
        self.content = content

@pytest.fixture
def patch_get(request):
    try:
        mp = request.getfixturevalue("monkeypatch")
    except AttributeError:  # pytest < 3
        mp = request.getfuncargvalue("monkeypatch")
    mp.setattr(requests.Session, 'request', get_mockreturn)
    return mp


def get_mockreturn(url, params=None, timeout=10):
    filename = data_path(DATA_FILES['votable'])
    content = open(filename, 'r').read()
    return MockResponse(content)

def data_path(filename):
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    return os.path.join(data_dir, filename)


def data_path(filename):
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    return os.path.join(data_dir, filename)