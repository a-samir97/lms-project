from django.urls import path
from . import views

app_name = 'utilities'

urlpatterns = [
    # all
    path('all/',views.all_announcements,name='all-announcements'),
    #create
    path('create/',views.create_announcement,name='create-announcement'),
    #delete
    path('delete/<int:id>/',views.delete_announcement,name='delete-announcement'),
]
