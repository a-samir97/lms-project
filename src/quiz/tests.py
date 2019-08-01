from django.test import TestCase, SimpleTestCase,Client
from django.urls import reverse,resolve
from . import views
from .models import Quiz
from .forms import QuizForm
from courses.models import Course
from users.models import User
# Create your tests here.

# TestForms 

class TestForms(SimpleTestCase):
    def test_form_not_valid(self):
        form = QuizForm(data={
            'course':'course1',
            'name':'assignment1',
        })
        self.assertFalse(form.is_valid())

    def test_form_no_data(self):
        form = QuizForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)

#TestUrls
class TestUrls(SimpleTestCase):
    def test_assignment_list(self):
        url = reverse('quiz:all-quizes')
        self.assertEquals(resolve(url).func,views.all_quizes)

    def test_create_assignment(self):
        url = reverse('quiz:create-quiz')
        self.assertAlmostEquals(resolve(url).func,views.create_quiz)
    
    
# test model
class TestModel(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='course1',content='content1')

    def test_assignment_name(self):
        quiz = Quiz.objects.create(name='assignment1',course=self.course)
        self.assertEquals(quiz.name,'assignment1')
    
    def test_assignemnt_course(self):
        quiz = Quiz.objects.create(name='assignment1',course=self.course)
        self.assertEquals(quiz.course,self.course)
    
    def test_assignments_count(self):
        self.assertEquals(Quiz.objects.all().count(),0)