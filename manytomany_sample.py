import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Authers, Books

def insert_books():
    book1 = Books(name='book1')
    book2 = Books(name='book2')
    book3 = Books(name='book3')
    book1.save()
    book2.save()
    book3.save()

def insert_authers():
    auther1 = Authers(name='auther1')
    auther2 = Authers(name='auther2')
    auther3 = Authers(name='auther3')
    auther1.save()
    auther2.save()
    auther3.save()

# insert_books()
# insert_authers()

book1 = Books.objects.get(pk=1)
book2 = Books.objects.get(pk=2)
book3 = Books.objects.get(pk=3)
auther1 = Authers.objects.get(pk=1)
auther2 = Authers.objects.get(pk=2)
auther3 = Authers.objects.get(pk=3)
# book1.authers.add(auther1, auther2)
book2.authers.add(auther2, auther3)
book3.authers.add(auther1, auther2, auther3)