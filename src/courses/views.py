from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import CourseForm

# show all courses
@login_required
def all_courses(request):
	if request.user.is_authenticated and request.user.role.user_role == '1':
		courses = Course.objects.all()
	elif request.user.is_authenticated:
		courses = Course.objects.filter(users=request.user)
	context = {
		'courses':courses,
	}
	return render(request,'course/all-courses.html',context)

# show all details of the course
@login_required
def course_detail(request,id):
	course_obj = Course.objects.get(id=id)
	request.session['courseId'] = id
	context = {
		'course':course_obj,
	}
	return render(request,'course/course-detail.html', context)

#create new course
@login_required
def create_course(request):
	if request.method == 'POST':

		form = CourseForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('course:course-detail',form.instance.id)
	else:
		form = CourseForm()

	context = {'form':form}
	return render(request,'course/create-course.html',context)

# delete course
@login_required
def delete_course(request,id):
	del_course = Course.objects.get(id=id)
	if request.method == 'POST':
		del_course.delete()
		return redirect('course:all-courses')
	return render(request,'course/delete-course.html')
