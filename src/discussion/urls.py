from django.urls import path
from . import views

app_name = 'discussion'

urlpatterns = [
    # create discussion
    path('create/',views.create_discussion,name='create-discussion'),
    # create post
    path('post/create/',views.create_post,name='create-post'),
    # all discussions
    path('all/',views.all_discussion,name='all-discussions'),
    # discussion detail
    path('<int:id>/',views.discussion_detail,name='discussion-detail'),
    # post detail
    path('post/<int:id>/',views.post_detail,name='post-detail'),
    #delete discussion
    path('delete/<int:id>/',views.delete_discussion,name='delete-discussion'),
    #delete post
    path('post/delete/<int:id>/',views.delete_post,name='delete-post'),
    #delete comment
    path('comment/delete/<int:id>/',views.delete_comment,name='delete-comment'),
]
