from django.urls import re_path
from . import views

urlpatterns = [
    re_path('api/$',views.User_data.as_view()),
]
