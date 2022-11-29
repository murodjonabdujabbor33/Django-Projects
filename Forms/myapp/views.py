from django.shortcuts import render
from .models import Student

# Create your views here.

def register(request):
    if request.POST:
        model = Student()
        model.name = request.POST['name']
        model.email = request.POST['email']
        model.phone_number = request.POST['phone_number']
        model.password = request.POST['password']
        model.course_type = request.POST['course_type']
        model.save()
        print(request.POST.get('email', None))
    return render(request, 'register.html')


def main(request):
    if request.POST:
        print(request.POST.get('email'))
    return render(request, 'index.html')