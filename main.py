import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

p = Person(
    first_name='Taro', last_name='Sato',
    birthday='2000-01-01', email='aa@mail.com',
    salary=100000, memo='memo Taro', web_site='http://www.google.com',
)

p = Person(
    first_name='Taro', last_name='Sato',
    birthday='2000-01-01', email='aa@mail.com',
    salary=None, memo='memo Taro', web_site='',
)

# p.save()

# Person.objects.create(
#     first_name='Jiro', last_name='Ito',
#     birthday='2001-01-01', email='bb@mail.com',
#     salary=20000, memo='memo Jiro', web_site='http://www.yahoo.co.jp'
# )

obj, created = Person.objects.get_or_create(
    first_name='Saburo', last_name='Ito',
    birthday='2001-01-02', email='bb@mail.com',
    salary=20000, memo='memo Jiro', web_site='http://www.yahoo.co.jp'
)

print(obj)
print(created)
