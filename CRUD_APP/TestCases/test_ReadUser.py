import json
import requests
import pytest
"""Run python manage.py runserver to run the project from terminal.
 and run this file by using 'pytest filename.py' command from another terminal"""


def get_User(id=None):
    """This function helps to get User if known Id is passed to this function"""
    data = {

    }
    if data is not None:
        data = {

            'id': id
        }

    resp = requests.get('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


# get_User()

def test_get_User(id=None):
    """This function should pass in test as it is fetching known user ID"""
    data = {

    }
    if data is not None:
        data = {

            'id': id
        }

    resp = requests.get('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200


def get_unknown_User(id=1000):
    """This function will throw error if you pass unknown user ID"""
    data = {

    }
    if data is not None:
        data = {

            'id': id
        }

    resp = requests.get('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


get_unknown_User()


def test_get_unknown_User(id=1000):
    """This function should fail as the id is not present in DB"""
    data = {

    }
    if data is not None:
        data = {

            'id': id
        }

    resp = requests.get('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200
