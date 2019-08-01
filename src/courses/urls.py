from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # all
    path('courses',views.all_courses,name='all-courses'),
    # creating
    path('create-course',views.create_course,name='create-course'),
    #details
    path('course-detail/<int:id>',views.course_detail,name='course-detail'),
    #delete
    path('delete/<int:id>/',views.delete_course,name='delete-course'),
]
