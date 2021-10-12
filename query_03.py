import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students

# print(Students.objects.all())
# print(Students.objects.filter(name__contains='郎').count())

# # 件数、最大値、最小値、平均値、合計
from django.db.models import Count, Max, Min, Avg, Sum
# print(Students.objects.aggregate(Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('age')))

# GROUP BY
# print(Students.objects.values('name').annotate(
#     Max('pk'), Min('pk')
# ))
# print(Students.objects.values('name', 'age').annotate(
#     max_id=Max('pk'), min_id=Min('pk')
# ))

for student in Students.objects.values('name', 'age').annotate(max_id=Max('pk'), min_id=Min('pk')):
    print(student['max_id'])