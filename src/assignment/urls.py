from django.urls import path
from . import views

app_name = 'assignment'

urlpatterns = [
    # all
    path('assignments/',views.all_assignments,name='all-assignments'),
    path('assignment/<int:id>/questions/',views.all_assignment_questions,name='all-assignment-questions'),
    # creating
    path('create-assignment/',views.create_assignment,name='create-assignment'),

    #delete
    path('delete/<int:id>/',views.delete_assignment,name='delete-assignment'),
    # questions
    path('assignment/<int:id>/create/questions/',views.assignment_question,name='assignment-questions'),
    #details
    path('assignment-detail/<int:id>/',views.assignment_detail,name='assignment-detail'),
    #solving
    path('assignment/<int:id>/',views.solving_assignment,name='solve-assignment'),
    # finishing creating questions
    path('assignment/info/<int:id>/',views.create_or_finish_assignment,name='finish-assignment'),

]
