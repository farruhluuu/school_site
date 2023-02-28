from django.shortcuts import render
from school.models import Teacher, Student, Graduate, Gallery
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
    return render(request, 'gallery.html', {'teacher': teacher, 'student': student, 'graduate': graduate, 'gallery':gallery, 'boll_cards': boll_cards, 'range_list': range_list})

def table1(request):
    return render(request, 'table1.html')



def table2(request):
    return render(request, 'table2.html')




def priem(request):
    return render(request, 'table1.html')
