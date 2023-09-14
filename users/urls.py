"""Defniuje adresy url dla użytkowników"""

from django.urls import path, include

from . import views

app_name = 'users' #pozwala udróżnić Django adresy url aplikacji 'users' od innych urlów z projektu
urlpatterns = [
	#Dołączenie domyślnych adresów url uwierzytelniania
	path('', include('django.contrib.auth.urls')),
	#Strona rejestracji
	path('register/', views.register, name='register')
	]