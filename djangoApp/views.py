from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def listStudents(request):
    studentsList = [{'id':1 , 'name': 'Mohamed Raddaoui', 'age': 24}, {'id':2 , 'name': 'Nidhal Gharbi', 'age': 28}, {'id':3 , 'name': 'Rabaa Gharbi', 'age': 30}]
    return render(request, "djangoApp\list.html", {'students':studentsList})

def detailsStudent(request, id):
    studentsList = [{'id':1 , 'name': 'Mohamed Raddaoui', 'age': 24}, {'id':2 , 'name': 'Nidhal Gharbi', 'age': 28}, {'id':3 , 'name': 'Rabaa Gharbi', 'age': 30}]
    studentsList = next((student for student in studentsList if student['id'] == id), None)
    return render(request, "djangoApp\details.html", {'student':studentsList})