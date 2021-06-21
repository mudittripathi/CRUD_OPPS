import json
import requests
import pytest
"""Run python manage.py runserver to run the project from terminal.
 and run this file by using 'pytest filename.py' command from another terminal"""

def delete_User(id=1009):
    """This function helps to delete existing User if Id is passed to this function"""
    data = {

        'id': id,
    }
    resp = requests.delete('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


# delete_User()


def test_delete_User(id=1009):
    """This function passes if giving ID is deleted"""
    data = {

        'id': id,
    }
    resp = requests.delete('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200


def delete_unknown_User(id=100100):
    """This function checks whether it is not able to search the given unknown ID, as it is not in DB"""
    data = {

        'id': id,
    }
    resp = requests.delete('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


# delete_unknown_User()


def test_delete_unknown_User(id=100100):
    """This function should fail if we are trying to delete non existing user"""
    data = {

        'id': id,
    }
    resp = requests.delete('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200
