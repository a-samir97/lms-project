from django.db import models
from users.models import User

class Course(models.Model):

    name = models.CharField(max_length=30,unique=True)
    content = models.TextField(null=False,blank=False)
    users = models.ManyToManyField(User,related_name='course_users')

    def __str__(self):
        return self.name

    def students_count(self):
        return self.users.filter(role__user_role='4').count()

    def instructor_count(self):
        return self.users.filter(role__user_role='2').count()

    def teaching_assistant_count(self):
        return self.users.filter(role__user_role='3').count()
