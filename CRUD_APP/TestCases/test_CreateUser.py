import json
import requests
import pytest
"""Run python manage.py runserver to run the project from terminal.
 and run this file by using 'pytest filename.py' command from another terminal"""

def create_new_User():
    """This function helps to create new User."""
    new_data = {

        'User_name': 'Blake',
        'User_id': 1009,
        'User_email': 'blake.blake@gmil.com',
    }

    resp = requests.post('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(new_data))
    print(resp.json())

# create_new_User()

def test_create_new_User():
    """This function helps to check weather new User is created successfully"""
    new_data = {

        'User_name': 'Blake',
        'User_id': 1009,
        'User_email': 'blake.blake@gmil.com',
    }
    resp = requests.post('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(new_data))
    assert resp.status_code == 201, "Data created"

def create_existing_User():
    """This function should give error because we cannot create existing User again by the same user ID"""
    new_data = {
        'User_name': 'sam',
        'User_id': 1001,
        'User_email': 'sam.sam@gmil.com',
    }

    resp = requests.post('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(new_data))
    print(resp.json())

# create_existing_User()

def test_create_existing_User():
    """This function should fail as no same ID can be created again"""
    new_data = {
        'User_name': 'sam',
        'User_id': 1001,
        'User_email': 'sam.sam@gmil.com',
    }

    resp = requests.post('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(new_data))
    assert resp.status_code == 201, "Data already there "