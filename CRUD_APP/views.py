from django.shortcuts import render, HttpResponse
from .models import User
from django.views.generic import View
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import UserForm

@method_decorator(csrf_exempt, name='dispatch')
class User_data(View):
    """This class based view basically helps to do all type of CRUD operation
    for USER Information in the database"""

    def get_User_by_id(self, id):
        """This function helps to get User if Id is passed to this function"""
        try:
            User_info = User.objects.get(User_id=id)
        except User.DoesNotExist:
            User_info = None
        return User_info

    def get(self, request, *args, **kwargs):
        """This function helps to get all the User if Id is None, else if if is present, it calls get_User_by_id()"""
        data = request.body
        print(data)
        p_data = json.loads(data)
        User_id = p_data.get('id', None)

        if User_id is not None:
            User_obj = self.get_User_by_id(User_id)

            if User_obj is None:
                return HttpResponse(json.dumps({'msg': 'User id not available in our system'}),
                                    content_type='application/json')

            a = {
                'name': User_obj.User_name,
                'email': User_obj.User_email
            }

            b = json.dumps(a)
            return HttpResponse(b, content_type='application/json')

        qs = User.objects.all()
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            User_data = obj['fields']
            final_list.append(User_data)
            json_data = json.dumps(final_list)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        """This function helps to get create new user"""
        data = request.body
        print(data)
        p_data = json.loads(data)
        form = UserForm(p_data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.save()
            return HttpResponse(json.dumps({'msg': 'User added successfully'}), status=201)
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        """This function helps to update existing User"""
        data = request.body
        print(data)
        p_data = json.loads(data)
        User_id = p_data.get('User_id', None)
        if User_id is not None:
            User_obj = self.get_User_by_id(User_id)
            print(User_obj)
            if User_obj is None:
                return HttpResponse(json.dumps({'msg': 'User id not available in our system'}),
                                    content_type='application/json')
            new_User = p_data

            old_User = {
                'User_name': User_obj.User_name,
                'User_id': User_obj.User_id,
                'User_email': User_obj.User_email,

            }

            old_User.update(new_User)
            form = UserForm(old_User, instance=User_obj)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponse(json.dumps({'msg': 'Updated successfully'}))
            if form.errors:
                json_data = json.dumps(form.errors)
                return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        """This function helps to delete User if known Id is passed to this function"""
        data = request.body
        print(data)
        p_data = json.loads(data)
        User_id = p_data.get('id', None)
        if User_id is not None:
            User_obj = self.get_User_by_id(User_id)
            if User_obj is None:
                return HttpResponse(json.dumps({'msg': 'User id not available in our system'}),
                                    content_type='application/json')
            status, deleted_item = User_obj.delete()
            if status == 1:
                return HttpResponse(json.dumps({'msg': 'deleted successfully'}))
            return HttpResponse(json.dumps({'msg': 'some issue occured ,try again'}), status=404)