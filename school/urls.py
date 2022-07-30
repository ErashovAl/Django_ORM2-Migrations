from django.urls import path

from school.views import students_list, list_of_teacher

urlpatterns = [
    path('', students_list, name='students'),
    path('teacher/', list_of_teacher, name='teacher')
]