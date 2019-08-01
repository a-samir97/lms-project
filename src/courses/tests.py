from django.test import TestCase, SimpleTestCase,Client
from django.urls import reverse,resolve

from .models import Course
from .forms import CourseForm
from . import views

# TESTForm

class TestForm(SimpleTestCase):
    def test_form_no_data(self):
        form = CourseForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)


class TestUrl(SimpleTestCase):
    def test_course_list(self):
        url = reverse('courses:all-courses')
        self.assertEquals(resolve(url).func,views.all_courses)

    def test_create_assignment(self):
        url = reverse('courses:create-course')
        self.assertAlmostEquals(resolve(url).func,views.create_course)

class TestView(TestCase):
    pass

class TestModel(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='course1',content='content1')

    def test_assignment_name(self):
        self.assertEquals(self.course.name,'course1')
    
    def test_assignemnt_content(self):
        self.assertEquals(self.course.content,'content1')
    
    def test_assignments_count(self):
        self.assertEquals(Course.objects.all().count(),1)