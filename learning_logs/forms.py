from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta: #wskazuje Django jakie pola ma utworzyć i skąd ma brać dane
		model = Topic
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})} #ten atrybut pozwala poszerzyć ilość miejsca, jaką użytkownik dostanie do wpisania swojego wpisu
		