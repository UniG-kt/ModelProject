import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students

students = Students.objects.all()
# print(students[:5])
# print(students[5:8].query)
# print(type(students))
# print(dir(students))