from django.test import TestCase, SimpleTestCase,Client
from django.urls import reverse,resolve
from . import views
from .models import Assignment
from .forms import AssignmentForm
from courses.models import Course
from users.models import User
# Create your tests here.

# TestForms 

class TestForms(SimpleTestCase):
    def test_form_not_valid(self):
        form = AssignmentForm(data={
            'course':'course1',
            'name':'assignment1',
        })
        self.assertFalse(form.is_valid())

    def test_form_no_data(self):
        form = AssignmentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)

#TestUrls
class TestUrls(SimpleTestCase):
    def test_assignment_list(self):
        url = reverse('assignment:all-assignments')
        self.assertEquals(resolve(url).func,views.all_assignments)

    def test_create_assignment(self):
        url = reverse('assignment:create-assignment')
        self.assertAlmostEquals(resolve(url).func,views.create_assignment)
    

class TestModel(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='course1',content='content1')

    def test_assignment_name(self):
        assignment = Assignment.objects.create(name='assignment1',course=self.course)
        self.assertEquals(assignment.name,'assignment1')
    
    def test_assignemnt_course(self):
        assignment = Assignment.objects.create(name='assignment1',course=self.course)
        self.assertEquals(assignment.course,self.course)
    
    def test_assignments_count(self):
        self.assertEquals(Assignment.objects.all().count(),0)
    
#TestViews

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(name='course1',content='content1')
        self.assignment = Assignment.objects.create(name='assignment1',course=self.course)
    