## Users Model
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
## Course , User ==> Many to Many relationship
#from courses.models import Course

class Role(models.Model):
    choices = [
    ('1','admin'),
    ('2', 'instructor'),
    ('3','teaching assistant'),
    ('4', 'student')
    ]

    #user id 
    user_role = models.CharField(max_length=1,choices=choices,default='1')
    user_id = models.PositiveIntegerField(null=True,blank=True)
    def __str__(self):
        return self.user_role

class User(AbstractUser):
    # user have one role, role can be referenced to many users
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.username
