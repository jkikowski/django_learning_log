from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""Rejestracja nowego użytkownika"""
	if request.method != "POST":
		#wyświetlanie pustego formularza rejestracji
		form = UserCreationForm()
	else:
		#przetworzenie formularza
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			#zalogowanie użytkownika i przekierowanie go na strone główną
			login(request, new_user)
			return redirect('learning_logs:index') #po rejestracji użytkownik ląduje na stronie głównej

	#wyświetlenie pustego formularza
	context = {'form':form}
	return render(request, 'registration/register.html', context)