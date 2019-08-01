from django.shortcuts import render,redirect

# Create your views here.
from .models import Announcement
from courses.models import Course
from .forms import AnnouncementForm

# create announcement

def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('announcement:all-announcements')
    else:
        form = AnnouncementForm()
    context = {
        'form':form,
    }
    return render(request,'announcement/create-announcement.html',context)

#delete announcement

def delete_announcement(request,id):
    if request.method == 'POST':
        del_announcement = Announcement.objects.get(id=id)
        del_announcement.delete()
        return redirect('announcement:all-announcements')
    return render(request,'announcement/delete-announcement.html')

# show all announcements of specific course

def all_announcements(request):
    course_obj = Course.objects.get(id=request.session['courseId'])
    all_announcements = Announcement.objects.filter(course=course_obj)

    context = {
        'all_announcements':all_announcements,
    }
    return render(request,'announcement/all-announcements.html',context)
