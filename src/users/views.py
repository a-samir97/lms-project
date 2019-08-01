## User Views ##
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth  import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from courses.models import Course
from .models import Role
from .forms import UserRegisterForm, RoleForm

User = get_user_model()

# home page
def home(request):
    print(request.user)
    return render(request,'users/home.html')

# create roles to the users
@login_required
def create_user_role(request):
    users = User.objects.filter(role=None)
    roles = ['admin','instructor','teaching assistant','student']
    course_obj = Course.objects.get(id=request.session['courseId'])
    if request.method == 'POST':
        user_list = request.POST.getlist('user')
        for user in user_list:
            user_object = User.objects.get(username=user)
            role = Role.objects.create(user_role = request.POST['role'],user_id=user_object.id)
            user_object.role = role
            if user_object.role.user_role != '1':
                course_obj.users.add(user_object)
                course_obj.save()
            user_object.save()
        return redirect('course:course-detail',course_obj.id)
    else:
        context = {
        'users':users,
        'roles':roles
        }
        return render(request,'users/create-role.html',context)

# delete user from database
@login_required
def delete_user(request):
    users = User.objects.exclude(role__user_role = "1")
    roles = ['instructor', 'teaching assistant','student']
    if  request.method == 'POST':
        get_users = request.POST.getlist('users')
        if not get_users:
            return HttpResponse('you have not deleted any one')
        for user in get_users:
            user_object = User.objects.get(username=user)
            role = Role.objects.filter(user=user_object)
            role.delete()
        return HttpResponse('You have been deleted users !')
    else:
        context = {
        'users':users,
        }
        return render(request,'users/delete-role.html',context)

# signup form to create a new user (without role )
def signup(request):
    if  request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')

    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request,'users/signup.html',context)

# instructor page shows all the functionalitiy that instructor can do
@login_required
def instructor_page(request):
    return render(request,'users/instructor-page.html',)

# admin page shows all the functionalitiy that admin can do
@login_required
def admin_page(request):
    return render(request,'users/admin-page.html',)

# student page shows all the functionalitiy that student can do
@login_required
def student_page(request):
    return render(request,'users/student-page.html')
