from django.shortcuts import render
from school.models import Teacher, Student, Graduate, Gallery, Events
from django.http import HttpResponseRedirect


# Create your views here.
def main(request):
    # info = Teacher.objects.all()
    return render(request, 'main.html')

def gallery(request):
    teacher = Teacher.objects.all()
    student = Student.objects.all()
    graduate = Graduate.objects.all()
    gallery = Gallery.objects.all()
    if gallery.exists() or student.exists() or graduate.exists() or teacher.exists():
        boll_cards = True
    else:
        boll_cards = False
    range_list = [0,1,2]
    return render(request, 'gallery.html', {'teacher': teacher, 'student': student, 'graduate': graduate, 'gallery':gallery, 'bool_cards': boll_cards, 'range_list': range_list})





def for_parents(request):
    return render(request, 'for_parents/main.html')

def admission_to_School(request):
    return render(request, 'for_parents/Admission_to_School.html')

def lesson_Schedule(request):
    return render(request, 'for_parents/lesson_schedule.html')

def meeting_schedule(request):
    return render(request, 'for_parents/meeting_schedule.html')

def uniform(request):
    return render(request, 'for_parents/uniform.html')

def payment_schedule(request):
    return render(request, 'for_parents/payment_schedule.html')




def for_students_and_graduates(request):
    return render(request, 'for_students/main.html')

def for_students(request):
    return render(request, 'for_students/for_students.html')

def for_graduates(request):
    return render(request, 'for_students/for_graduates.html')



def gallery(request):
    mentors = Teacher.objects.all()[1:7]
    students = Student.objects.all()[1:7]
    graduates = Graduate.objects.all()[1:7]


    return render(request, 'gallery/main.html', {'mentors': mentors, 'students': students, 'graduates': graduates})

def mentors(request):
    mentors = Teacher.objects.all()
    if mentors.exists():
        bool_cards = True
    else:
        bool_cards = False
    range_list = [0,1,2]
    return render(request, 'gallery/teachers.html', {'mentors': mentors, 'bool_cards': bool_cards, 'range_list': range_list})

def students(request):
    students = Student.objects.all()
    if students.exists():
        bool_cards = True
    else:
        bool_cards = False
    range_list = [0,1,2]
    return render(request, 'gallery/students.html', {'students': students, 'bool_cards': bool_cards, 'range_list': range_list})

def graduates(request):
    graduates = Graduate.objects.all()
    if graduates.exists():
        bool_cards = True
    else:
        bool_cards = False
    range_list = [0,1,2]
    return render(request, 'gallery/graduates.html', {'graduates': graduates, 'bool_cards': bool_cards, 'range_list': range_list})
def events(request):
    events = Events.objects.all()
    return render(request, 'gallery/events.html', {'events': events})

def error_page(request):
    return render(request, 'error.html')
