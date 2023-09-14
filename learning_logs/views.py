from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
	"""Strona główna dla plikacji learning Log"""
	return render(request, 'learning_logs/index.html') #odnośnik do tego co ma znajdować się na stronie głównej

@login_required #dekorator, który pozwala tylko zalogowanym użytkownikom oglądanie treści na stronie
def topics(request):
    """wyświetla wszystkie tematy"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    #jeśli zalogowany użytkownik jest taki sam co ten, który utworzył temat, to będzie on wyświetlony
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """wyświetla pojedyńczy temat i powiązane z nim wpisu"""
    topic = Topic.objects.get(id=topic_id)

    check_topic_owner(topic.owner, request.user)

    """if topic.owner != request.user: #jeśli zalogowany użytkownik nie będzie właścicielem tematu, strona wyświetli błąd 404
    	raise Http404"""

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	"""Dodaje nowy temat"""
	if request.method != 'POST': #POST każe formularzowi wysłać dane do bazy danych, natomiast GET zasysa z bazy danych informacje
		#nie przekazano żadnych danych, należy utworzyć pusty formularz
		form = TopicForm()
	else:
		#przekazano dane za pomocą żądania POST
		form = TopicForm(data=request.POST)
		if form.is_valid(): #sprawdza czy wszystkie pola formularza są wypełnione
			new_topic = form.save(commit=False) #przed zapisaniem konieczne jest zmodyfikowanie tematu (przypisanie twórcy)
			new_topic.owner = request.user #przypisuje autora tematu
			form.save() #zapisuje temat wraz z autorem
			return redirect('learning_logs:topics') #redirect() przekierowuje użytkownika do strony Topics po dodaniu nowego wpisu

	#wyświetlenie pustego formularza
	context = {'form':form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	"""Dodanie nowego wpisu dla określonego tematu"""
	topic = Topic.objects.get(id=topic_id) #pobiera odpowiedni temat do dodania opisu

	check_topic_owner(topic.owner, request.user)

	if request.method != 'POST': #użyta metoda określona w kodzie html szablonu strony
		#nie przekazano żadnych danych - należy utworzyć pusty formularz
		form = EntryForm()

	else:
		#przekazano dane za pomocą żądania POST i należy je pzetworzyć
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False) #tworzy miejsce w zmiennej new_entry do zapisania wpisu
			new_entry.topic = topic
			new_entry.save() #zapisuje wpis do bazy danych do odopwiedniego tematu
			return redirect('learning_logs:topic', topic_id=topic_id)

	#wyświetlenie pustego formularza
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context) #pusty i nieprawidłowy szablon spowoduje wyświetlenie znowu formularza

@login_required
def edit_entry(request, entry_id):
	"""Edycja istniejącego wpisu"""
	entry = Entry.objects.get(id=entry_id) #pobiera wpis do edytowania
	topic = entry.topic #pobiera temat, który jest powiązany z edytowanym wpisem

	check_topic_owner(topic.owner, request.user)

	if request.method != 'POST':
		#żądanie początkowe - wypełnienie formularza aktualną treścią wpisu
		form = EntryForm(instance=entry) #nakazuje Django wyświetlić formularz z już uzupełnionymi danymi wpisu
	else:
		#przekazano dane za pomocą żądania POST, należy je przetworzyć
		form = EntryForm(instance=entry, data=request.POST) #nakazanie Django utworzenia formularza z nowymi danymi
		if form.is_valid():
			form.save() #nadpisanie wpisu
			return redirect('learning_logs:topic', topic_id=topic_id)

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(owner, user):
	"""Sprawdza, czy zalogowany użytkownik jest właścicielem tematu"""
	if owner!= user:
		raise Http404

	