"""Definiujea dresy dla learning_logs"""

from django.urls import path
from . import views # . oznacza importowanie z katalogu, w którym znajduje się ten plik

app_name = 'learning_logs'
urlpatterns = [ #lista stron, które mogę być wywoływane z tego projektu
	#strona główna - szuka w pliku views.py finkcji index
	path('', views.index, name='index'), #definicja wzorsu URL - pierwszy argument, to do czego ma się odwołać, jeśli jest pusty, to odwołą się do localhost
		#drugi argument, to przekierowanie, co ma wyświetlić po dopasowaniu adresu do wzorca (pierwszego argumentu)
		#trzeci argument, to nazwa przekierowania

	#wyświetlanie wszystkich tematów
	path('topics/', views.topics, name='topics'),

	#strona szczegółowa dotyczaca jednego tematu
	path('topics/(<int:topic_id>)/', views.topic, name='topic'), #ten fragment <int...> każe w url wstawić odpowiednia cyfre z id

	#strona przeznaczona do dodawania nowego tematu
	path('new_topic/', views.new_topic, name='new_topic'),

	#strona przeznaczona do dodawania nowego wpisu
	path('new_entry/<int:topic_id>)', views.new_entry, name='new_entry'), #tworzy url dla nowych wpisów do tematów z numeracją po id tematów

	#strona przeznaczona do edycji wpisów
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	]