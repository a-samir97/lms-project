from django.urls import path,include
from . import views
app_name = 'users'

urlpatterns = [
    path('create/',views.create_user_role,name='create-role'),
    path('delete/',views.delete_user,name='delete-user'),
    path('admin/',views.admin_page,name='admin-page'),
    path('instructor/',views.instructor_page,name='instructor-page'),
    path('student',views.student_page,name='student-page'),
]
