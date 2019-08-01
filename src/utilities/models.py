from django.db import models
from django.shortcuts import redirect
from assignment.models import Assignment
from quiz.models import Quiz
from users.models import User
from courses.models import Course

class Question(models.Model):
    content = models.TextField()
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='quiz_question',null=True,blank=True)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,related_name='assignment_question',null=True,blank=True)

    def __str__(self):
    	return str(self.id)


    def get_absolute_url(self):
    	return redirect('/')

    def get_all_questions_quiz(self,quiz_id):
    	quizes = Question.objects.filter(quiz_id=quiz_id)
    	return quizes

    def get_all_questions_assignments(self,assignment_id):
    	assignments = Question.objects.filter(assignment_id=assignment_id)
    	return assignments

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question_answers')
    choice = models.CharField('choice',max_length=50)
    true_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice

    def check_student_answer(self,answer):
        if answer == True:
            return True
        return False

class Grade(models.Model):

    user_grade = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_grades')
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,related_name='assignment_grades',null=True,blank=True)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='quiz_grades',null=True,blank=True)
    total_marks = models.IntegerField(default=0)
    student_marks = models.IntegerField(default=0)


    def __str__(self):
        return str(self.total_marks)

    def increse_grade(self):
        self.student_marks += 1

    def get_user_quiz_grade(self,quiz_id,user_obj):
    	quiz_obj = Quiz.objects.get(id=quiz_id)
    	user_grade_quiz = Grade.objects.filter(user=user_obj,quiz__id=quiz_id)
    	return user_grade_quiz

    def get_user_assignment_grade(self,assignment_id,user_obj):
    	assignment_obj = Assignment.objects.get(id=assignment_id)
    	user_grade_assignment = Grade.objects.filter(user=user_obj,assignment__id=assignment_id)
    	return user_grade_assignment

    def get_user_grades(self,user_obj):
    	all_grade = user_obj.user_grades.all()
    	return all_grade


class Announcement(models.Model):
	course = models.ForeignKey(Course,on_delete=models.CASCADE,null=False,blank=False)
	announce_post = models.TextField()

	def __str__(self):
		return self.user.username
