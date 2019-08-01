from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Discussion, Post, Comment
from .forms import DiscussionForm, PostForm, CommentForm
from courses.models import Course

#show all discussions of specific course
def all_discussion(request):
    course_obj = Course.objects.get(id=request.session['courseId'])
    all_discussions = Discussion.objects.filter(course=course_obj)
    context = {
        'all_discussions':all_discussions,
    }
    return render(request,'discussion/all-discussions.html',context)

# discussion detail
def discussion_detail(request,id):
    request.session['discussionId'] = id
    discussion_obj = Discussion.objects.get(id=id)
    posts = Post.objects.filter(discussion=discussion_obj)
    context = {
        'discussion_obj':discussion_obj,
        'posts':posts,
    }
    return render(request,'discussion/discussion-detail.html',context)

# create discussion
def create_discussion(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('discussion:all-discussions')
    else:
        form = DiscussionForm()
    context = {
        'form':form
    }
    return render(request,'discussion/create-discussion.html',context)


# create post
def create_post(request):
    discussion_obj = Discussion.objects.get(id=request.session['discussionId'])
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.instance.discussion = discussion_obj
            form.save()
            return redirect('discussion:post-detail',form.instance.id)
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request,'discussion/create-post.html',context)

#post detail
# in post detail we create a comment and delete a comment
def post_detail(request,id):
    request.session['postId'] = id
    post_obj = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post_obj)

    # create comment
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.instance.post = post_obj
            form.save()
            return redirect('discussion:post-detail',id)
    else:
        form = CommentForm()
    context = {
        'post_obj':post_obj,
        'comments':comments,
        'form':form,
    }
    return render(request,'discussion/post-detail.html',context)


# delete discussion
def delete_discussion(request,id):
    deleted_dicussion = Discussion.objects.get(id=id).delete()
    return redirect('discussion:all-discussions')

#delete post
def delete_post(request,id):
    del_post = Post.objects.get(id=id).delete()
    return redirect('discussion:discussion-detail',request.session['discussionId'])

#delete comment
def delete_comment(request,id):
    del_comment =  Comment.objects.get(id=id).delete()
    return redirect('discussion:post-detail',request.session['postId'])
