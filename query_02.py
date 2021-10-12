import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students, Person

# all
# print(Students.objects.all())

# IN
ids = [13, 14, 15]
# print(Students.objects.filter(pk__in=ids))

# contain部分一致
# print(Students.objects.filter(name__contains='三'))

# isnull
# p = Person(
#     first_name='Jiro', last_name='Yamada',
#     birthday='2001-01-01', email='aa@test.com',
#     salary=None, memo='memo Jiro', web_site='https://www.jiro.com'
# )
# p.save()

# filter: 指定内、exclude: 指定外
# print(Person.objects.filter(salary__isnull=True))
# print(Person.objects.exclude(salary__isnull=True))

# values: 一部のカラムのみ取り出す
print(Students.objects.values('name', 'age').filter(name__contains='三'))