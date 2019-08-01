from django import forms
from .models import Question,Answer,Announcement

class QuestionForm (forms.ModelForm):
    class Meta:
    	model = Question
    	fields = ['content']

class AnswerForm(forms.ModelForm):
    choice = forms.CharField()
    class Meta:
    	model = Answer
    	fields = ['choice','true_answer']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['announce_post','course']
