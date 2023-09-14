from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model): #model dziedziczący po klasie nadrzędnej models
	"""Temat poznawany przez użytkownika"""
	text = models.CharField(max_length=200) #tworzy atrybut składający się ze znaków
	#podana nazwa zmiennej będzie wyświetlała się przy polu na stronie
	date_added = models.DateTimeField(auto_now_add=True) #automatcznie dodaje date i godzine do tworzonego przez użytkownika tematu
	owner = models.ForeignKey(User, on_delete=models.CASCADE) #po usunięciu użtkownika, wszystkie jego materiały będą usunięte
	#konieczne jest wykonanie migracji bazy danych i przypisanie wszystkich istniejących tematów do jednego użytkownika
	#albo wykonanie polecenia python manage.py flush - co wyczyści całą baze danych i użytkowników

	def __str__(self):
		"""Zwraca reprezentacje modelu w postaci ciągu tekstowego"""
		return self.text #wskazujesz który atrybut jest używany domyślnie przez model

class Entry(models.Model):
	"""Informacje o postępie w nauce"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #foreigney to odwołanie do rekordu z zewnętrznej bazy danych 
	#on_delete - wskazuje że po usunięciu danego wpisu wszystkie połączone do niego wpisy będą usuniete
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries' #podaje jak Django ma się odwoływać do tej metody, kiedy jest więcej wpisów

	def __str__(self):
		"""Zwraca reprezentacje modelu w postaci ciągu tekstowego"""
		if len(self.text) >= 50:
			return f"{self.text[:50]}..."
		else:
			return f"{self.text}"