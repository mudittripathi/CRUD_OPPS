import json
import requests

'''Use below functions to check CRUD operations.
You can run the project in 1 server and run "python test1.py" with the function you want to'''


def create_new_User():
    """This function helps to create new User.
    you can enter name,id and email in dict
    and that data will be inserted in the database by calling post method
    of User_data class in CRUD_APP.views.py"""
    new_data = {

        'User_name': 'Eric',
        'User_id': 1012,
        'User_email': 'eric.eric@gmil.com',
    }

    resp = requests.post('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(new_data))
    print(resp.json())


create_new_User()


def create_existing_User():
    """This function helps check that existing User can not be created.
    you can enter name,id and email in dict
    and that data will throw error that User with this User id already exists."""
    new_data = {
        'User_name': 'sam',
        'User_id': 1001,
        'User_email': 'sam.sam@gmil.com',
    }

    resp = requests.post('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(new_data))
    print(resp.json())


create_existing_User()


def get_User(id=None):
    """This function helps to get all the User.
    you can pass id = None
    and you will get all the Users"""
    data = {

    }
    if data is not None:
        data = {

            'id': id
        }

    resp = requests.get('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


get_User()


def get_unknown_User(id=1100):
    """This function will not be able to get the user if id passed is unknown (not in db).
    it will print User id not available in our system'"""
    data = {

    }
    if data is not None:
        data = {

            'id': id
        }

    resp = requests.get('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


get_unknown_User()


def update_User(id):
    """This function helps to update existing User.
    you can pass existing id in this function
    and that data will be updated in the database by calling put method
    of User_data class in CRUD_APP.views.py"""
    data = {
        'User_name': 'Anil',
        'User_id': id,
        'User_email': 'anil.anil@gmail.com',
    }
    resp = requests.put('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


update_User(1002)


def update_unknown_User(id):
    """This function helps to check if unknown id is passed, it will give no user id in db.
    you can pass an unknown id (not in db)"""

    data = {
        'User_name': 'Harsh',
        'User_email': 'Harsh@gmail.com',
        'User_id': id,
    }
    resp = requests.put('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


update_unknown_User(1000)


def delete_User(id=1012):
    """This function helps to delete existing User.
    you can pass an existing id in this function
    and that data will be deleted from the database by calling delete method
    of User_data class in CRUD_APP.views.py"""
    data = {

        'id': id,
    }
    resp = requests.delete('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


delete_User()


def delete_unknown_User(id=1100):
    """This function will not delete anything as the user id passed is not present in db.
    you can pass an unknown id in this function
    and that data will be not be deleted from the database. error will be
    'User id not available in our system'"""
    data = {

        'id': id,
    }
    resp = requests.delete('http://127.0.0.1:8000/User_basic/api/', data=json.dumps(data))
    print(resp.json())


delete_unknown_User()
