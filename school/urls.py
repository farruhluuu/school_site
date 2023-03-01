from django.urls import path
from school.views import main, gallery, mentors, students, graduates
from school.views import for_parents, admission_to_School, lesson_Schedule, meeting_schedule, uniform, payment_schedule
from school.views import for_students_and_graduates, for_students, for_graduates

urlpatterns = [
    path('', main, name='main'),
    
    path('for_parents/', for_parents, name='for_parents'),
    path('admission_to_school/', admission_to_School, name='admission_to_school'),
    path('lesson_Schedule/', lesson_Schedule, name='lesson_Schedule'),
    path('meeting_schedule/', meeting_schedule, name='meeting_schedule'),
    path('uniform/', uniform, name='uniform'),
    path('payment_schedule/', payment_schedule, name='payment_schedule'),

    path('for_students_and_graduates/', for_students_and_graduates, name='for_students_and_graduates'),
    path('for_students/', for_students, name='for_students'),
    path('for_graduates/', for_graduates, name='for_graduates'),

    path('gallery/', gallery, name='gallery'),
    path('mentors', mentors, name='mentors'),
    path('students', students, name='students'),
    path('graduates', graduates, name='graduates'),
    
]
