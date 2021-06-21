import json
import requests
import pytest
"""Run python manage.py runserver to run the project from terminal.
 and run this file by using 'pytest filename.py' command from another terminal"""

def update_User(id=1002):
    """This function helps to update User if known user Id is passed to this function"""
    data = {
        'User_name': 'Anil',
        'User_id': id,
        'User_email': 'anil.aanil@gmail.com',
    }
    resp = requests.put('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


# update_User(1002)


def test_update_User(id=1002):
    """This function should pass because a known id is passed and it will get updated"""
    data = {
        'User_name': 'Anil',
        'User_id': id,
        'User_email': 'anil.aanil@gmail.com',
    }
    resp = requests.put('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200


def update_unknown_User(id=1100):
    """This function will not able to update user ID because it is not present in DB"""
    data = {
        'User_email': 'xxx@gmail.com',
        'user_id': id,
    }
    resp = requests.put('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
    print(resp.json())


# update_unknown_User()


def test_update_unknown_User(id=1100):
    """This function should fail as the id is not in DB. It won't get updated"""
    data = {
        'User_email': 'xxx@gmail.com',
        'user_id': id,
    }
    resp = requests.put('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200
