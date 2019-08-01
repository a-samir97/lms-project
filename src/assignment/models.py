# Assignment Model
from django.db import models

from courses.models import Course

class Assignment(models.Model):
    name     = models.CharField(max_length=20)
    course   = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='assignment_course')
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_assignments_in_course(self,course_obj):
        all_assignments = course_obj.assignment_course.all()
        return all_assignments
