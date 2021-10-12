import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students, Schools, Prefectures

# s = Schools.objects.first()
# print(type(s))
# print(dir(s))
# print(s.prefecture.name)
# print(s.students_set)

from ModelApp.models import Places, Restaurants

# p = Places.objects.first()
# # print(type(p))
# # print(dir(p))
# print(p.restaurants.name)

# r = Restaurants.objects.first()
# print(r.place.name)

from ModelApp.models import Books, Authers

b = Books.objects.first()
print(b.authers.all())

a = Authers.objects.first()
print(a.books_set.all())