## django core
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
## models
from assignment.models import Assignment
from utilities.models import Question,Answer,Grade
from courses.models import Course
from users.models import User
## forms
from assignment.forms import AssignmentForm
from utilities.forms import QuestionForm,AnswerForm

# show all assignments of specific course
@login_required
def all_assignments(request):
	course_obj = Course.objects.get(id=request.session['courseId'])
	assignments = Assignment.objects.filter(course=course_obj)
	context = {
		'assignments':assignments,
		'course_id':request.session['courseId'],
	}
	return render(request,'assignment/all-assignments.html',context)

#show all questions of specific assignment
@login_required
def all_assignment_questions(request,id):
	all_questions = Question.objects.filter(assignment_id=id)
	assignment_name = Assignment.objects.get(id=id).name
	context = {
		'all_questions':all_questions,
		'assignment_name':assignment_name,
	}
	return render(request,'assignment/all-assignment-questions.html',context)

# create new assignment
@login_required
def create_assignment(request):
	if request.method == 'POST':
		form = AssignmentForm(request.POST or None)
		if  form.is_valid():
			form.save()
			return redirect('assignment:assignment-detail',form.instance.id)
	else:
		form = AssignmentForm()
	context = {'form':form}
	return render(request,'assignment/create-assignment.html',context)

#delete assignment
@login_required
def delete_assignment(request,id):
	del_assignment = Assignment.objects.get(id=id)
	if request.method == 'POST':
		del_assignment.delete()
		return redirect('assignment:all-assignments')

	return render(request,'assignment/delete-assignment.html')

# shoyw details of the assignment and more information to instructor role and student role
@login_required
def assignment_detail(request,id):
	assignment_obj = get_object_or_404(Assignment,id=id)
	assignment_questions = Question.objects.filter(assignment_id=id)
	student_grades = Grade.objects.filter(user_grade=request.user,assignment=assignment_obj)
	all_grades = Grade.objects.filter(assignment=assignment_obj)

	context = {
		'assignment':assignment_obj,
		'assignment_questions':assignment_questions,
		'student_grades': student_grades,
		'all_grades':all_grades,
	}
	return render(request,'assignment/assignment-detail.html',context)

# create question to specific assignment
@login_required
def assignment_question(request,id):
	assignment_obj = get_object_or_404(Assignment,id=id)
	question_counter = Question.objects.filter(assignment_id=id).count()
	if  request.method == 'POST' and request.POST.get('finish') == 'finished':
		assignment_obj.finished = True
		assignment_obj.save()
		return redirect('assignment:assignment-detail',id)

	if  request.method == 'POST':
		question_form = QuestionForm(request.POST or None)
		answer_form1 = AnswerForm(request.POST or None,prefix='first_answer')
		answer_form2 = AnswerForm(request.POST or None,prefix='second_answer')
		answer_form3 = AnswerForm(request.POST or None,prefix='third_answer')

		if  question_form.is_valid()  and answer_form1.is_valid() and answer_form2.is_valid() and answer_form3.is_valid():
			question_form.instance.assignment = assignment_obj
			question_form.save()
			answer_form1.instance.question = question_form.instance
			answer_form2.instance.question = question_form.instance
			answer_form3.instance.question = question_form.instance
			answer_form1.save()
			answer_form2.save()
			answer_form3.save()
			counter = Question.objects.filter(assignment_id=id).count()
			messages.success(request,"this assignment have {} questions".format(counter))
			return redirect('assignment:assignment-questions', id)
		else:
			pass
	else:
		question_form = QuestionForm()
		answer_form1 = AnswerForm(prefix='first_answer')
		answer_form2 = AnswerForm(prefix='second_answer')
		answer_form3 = AnswerForm(prefix='third_answer')

	context = {
		'question_form':question_form,
		'first_answer':answer_form1,
		'second_answer':answer_form2,
		'third_answer':answer_form3,
		'question_counter':question_counter,
		'assignment_id':id,
	}
	return render(request,'assignment/assignment-questions.html',context)

# start solving the assignment
@login_required
def solving_assignment(request,id):
	student_obj = request.user
	assignment_obj = Assignment.objects.get(id=id)
	questions_list = Question.objects.filter(assignment_id=id)
	submit_button = True
	lists = list()
	correct_answers = 0
	if request.method == 'POST':

		for question in questions_list:
			submit_button = False
			if  request.POST.get('answer'+str(question.id)) == 'True':
				correct_answers += 1
		user_quiz_grades = Grade.objects.create(user_grade=student_obj,assignment=assignment_obj,total_marks=questions_list.count(),student_marks=correct_answers)

		if user_quiz_grades.student_marks >= user_quiz_grades.total_marks/2:
			score = (user_quiz_grades.student_marks/user_quiz_grades.total_marks)*100
		else:
			score = (user_quiz_grades.student_marks/user_quiz_grades.total_marks)*100
		return redirect('assignment:assignment-detail', id)
	else:
		pass
	context = {
		'questions':questions_list,
		'submit_button':submit_button,
		'assignment_obj':assignment_obj,
	}
	return render(request,'assignment/solve-assignment.html',context)

# to create more questions or to finish editing the assignments and publish it to students
@login_required
def create_or_finish_assignment(request,id):
	if request.method =='POST':
		quiz_obj = Assignment.objects.filter(id=id)[0]
		quiz_obj.finished = True
		quiz_obj.save()
		return redirect('assignment:assignment-detail', id)
	else:
		pass
	return render(request,'assignment/finish-assignment.html')
