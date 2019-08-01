## django core
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
## models
from quiz.models import Quiz
from utilities.models import Question,Answer,Grade
from courses.models import Course
from users.models import User
## forms
from quiz.forms import QuizForm
from utilities.forms import QuestionForm,AnswerForm

# show all quizes in specfic course
@login_required
def all_quizes(request):
	course_obj = Course.objects.get(id=request.session['courseId'])
	quizes = Quiz.objects.filter(course=course_obj)
	context = {
		'quizes':quizes,
		'course_id':request.session['courseId'],
	}
	return render(request,'quiz/all-quizes.html',context)

# show all quesitions in quiz
@login_required
def all_quiz_questions(request,id):
	all_questions = Question.objects.filter(quiz_id=id)
	quiz_name = Quiz.objects.get(id=id).name
	context = {
		'all_questions':all_questions,
		'quiz_name':quiz_name,
	}
	return render(request,'quiz/all-quiz-questions.html',context)

# create new quiz
@login_required
def create_quiz(request):
	if request.method == 'POST':
		form = QuizForm(request.POST or None)
		if  form.is_valid():
			form.save()
			return redirect('quiz:quiz-detail',form.instance.id)
	else:
		form = QuizForm()
	context = {'form':form}
	return render(request,'quiz/create-quiz.html',context)

# delete quiz
@login_required
def delete_quiz(request,id):
	del_quiz = Quiz.objects.get(id=id)
	if request.method == 'POST':
		del_quiz.delete()
		return redirect('quiz:all-quizes')
	return render(request,'quiz/delete-quiz.html')

# quiz details
# show informations about quiz
@login_required
def quiz_detail(request,id):
	quiz_obj = get_object_or_404(Quiz,id=id)
	quiz_questions = Question.objects.filter(quiz_id=id)
	all_grades = Grade.objects.filter(quiz=quiz_obj)
	student_grades = Grade.objects.filter(user_grade=request.user,quiz=quiz_obj)
	#request.session['quiz_id'] = id
	context = {
		'quiz':quiz_obj,
		'quiz_questions':quiz_questions,
		'student_grades': student_grades,
		'all_grades':all_grades,
	}
	return render(request,'quiz/quiz-detail.html',context)

# creating question in specfic quiz
@login_required
def quiz_question(request,id):
	quiz_obj = get_object_or_404(Quiz,id=id)
	question_counter = Question.objects.filter(quiz_id=id).count()
	if  request.method == 'POST' and request.POST.get('finish') == 'finished':
		print(request.POST)
		quiz_obj.finished = True
		quiz_obj.save()
		return redirect('quiz:quiz-detail',id)

	if  request.method == 'POST':
		print(request.POST)
		question_form = QuestionForm(request.POST or None)
		answer_form1 = AnswerForm(request.POST or None,prefix='first_answer')
		answer_form2 = AnswerForm(request.POST or None,prefix='second_answer')
		answer_form3 = AnswerForm(request.POST or None,prefix='third_answer')

		if  question_form.is_valid()  and answer_form1.is_valid() and answer_form2.is_valid() and answer_form3.is_valid():
			question_form.instance.quiz = quiz_obj
			question_form.save()
			answer_form1.instance.question = question_form.instance
			answer_form2.instance.question = question_form.instance
			answer_form3.instance.question = question_form.instance
			answer_form1.save()
			answer_form2.save()
			answer_form3.save()
			counter = Question.objects.filter(quiz_id=id).count()
			messages.success(request,"this quiz have {} questions".format(counter))
			return redirect('quiz:quiz-questions', id)
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
		'quiz_id':id,
	}
	return render(request,'quiz/quiz-questions.html',context)


# student solving the quiz

@login_required
def solving_quiz(request,id):
	student_obj = request.user
	quiz_obj = Quiz.objects.get(id=id)
	questions_list = Question.objects.filter(quiz_id=id)
	submit_button = True
	lists = list()
	correct_answers = 0
	if request.method == 'POST':

		for question in questions_list:
			submit_button = False
			if  request.POST.get('answer'+str(question.id)) == 'True':
				correct_answers += 1
		user_quiz_grades = Grade.objects.create(user_grade=student_obj,quiz=quiz_obj,total_marks=questions_list.count(),student_marks=correct_answers)

		if user_quiz_grades.student_marks >= user_quiz_grades.total_marks/2:
			score = (user_quiz_grades.student_marks/user_quiz_grades.total_marks)*100
		else:
			score = (user_quiz_grades.student_marks/user_quiz_grades.total_marks)*100
		return redirect('quiz:quiz-detail' ,id)
	else:
		pass
	context = {
		'questions':questions_list,
		'submit_button':submit_button,
		'quiz_obj':quiz_obj,
	}
	return render(request,'quiz/solve-quiz.html',context)

# to create more question in quiz or finish it to publish the quiz to the students
@login_required
def create_or_finish_quiz(request,id):
	if request.method =='POST':
		quiz_obj = Quiz.objects.filter(id=id)[0]
		quiz_obj.finished = True
		quiz_obj.save()
		return redirect('quiz:quiz-detail', id)
	else:
		pass
	return render(request,'quiz/finish-quiz.html')
