from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    # all
    path('quizes/',views.all_quizes,name='all-quizes'),
    path('quiz/<int:id>/questions/',views.all_quiz_questions,name='all-quiz-questions'),
    # creating
    path('create-quiz/',views.create_quiz,name='create-quiz'),
    #delete
    path('delete/<int:id>',views.delete_quiz,name='delete-quiz'),
    # questions
    path('quiz/<int:id>/create/questions/',views.quiz_question,name='quiz-questions'),
    #details
    path('quiz-detail/<int:id>/',views.quiz_detail,name='quiz-detail'),
    #solving
    path('quiz/<int:id>/',views.solving_quiz,name='solve-quiz'),
    # finishing creating questions
    path('quiz/info/<int:id>/',views.create_or_finish_quiz,name='finish-quiz'),
    # discussion
]
