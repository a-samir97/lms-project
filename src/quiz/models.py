from django.db import models

from courses.models import Course

class Quiz (models.Model):
    name = models.CharField(max_length=20)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='quiz_course')
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_quizes_in_course(self,course_obj):
        all_quizes = course_obj.quiz_course.all()
        return all_quizes

    def get_user_quizes(self,user_id):
        user_quizes = Quiz.objects.filter(course__user__id=user_id)
        return user_quizes
