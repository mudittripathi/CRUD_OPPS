from django.db import models


class User(models.Model):
    User_name = models.CharField(max_length=20)
    User_id = models.IntegerField(primary_key=True)
    User_email = models.TextField()

    def __str__(self):
        return self.User_name



