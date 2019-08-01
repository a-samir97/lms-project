from django.test import TestCase, SimpleTestCase,Client
from django.urls import reverse,resolve
from . import views
from .models import User
from .forms import UserRegisterForm
# Create your tests here.

# TestForms 

class TestForms(TestCase):
    def test_form_not_valid(self):
        form = UserRegisterForm(data={
            'username':'ahmedsamir',
            'password1':'password123',
            'password2':'password123',
        })
        self.assertFalse(form.is_valid())

    def test_form_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

#TestUrls
class TestUrls(SimpleTestCase):
    def test_create_user_role(self):
        url = reverse('users:create-role')
        self.assertEquals(resolve(url).func,views.create_user_role)

    def test_delete_user(self):
        url = reverse('users:delete-user')
        self.assertEquals(resolve(url).func,views.delete_user)
    
    def test_user_admin(self):
        url = reverse('users:admin-page')
        self.assertEquals(resolve(url).func,views.admin_page)
    
    def test_user_instructor(self):
        url = reverse('users:instructor-page')
        self.assertEquals(resolve(url).func,views.instructor_page)
    
    def test_user_student(self):
        url = reverse('users:student-page')
        self.assertEquals(resolve(url).func,views.student_page)
    
class TestModel(TestCase):

    def test_user_username(self):
        user = User.objects.create(username='ahmedsamir',password='123123123')
        self.assertEquals(user.username,'ahmedsamir')
    
    def test_check_password(self):
        user = User.objects.create(username='ahmedsamir',password='123123123')
        self.assertTrue(user.password,'123123123')

    def test_assignments_count(self):
        self.assertEquals(User.objects.all().count(),0)
    