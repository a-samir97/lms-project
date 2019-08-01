from django.db import models
from courses.models import Course
# Create your models here.
from django.utils import timezone
import datetime
class Discussion(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    content = models.TextField()
    discussion = models.ForeignKey(Discussion,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
