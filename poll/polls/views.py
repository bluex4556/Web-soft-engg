from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Faculty
# Create your views here.

def index(request):
        facultylist= Faculty.objects.order_by('-id')[:5]
        context= {'facultylist': facultylist,}
        #output= ', '.join([q.faculty_name for q in facultylist])
        return render(request, 'polls/index.html',context)

def detail(request ,faculty_id):
        faculty= get_object_or_404(Faculty, pk=faculty_id)
        return render(request, 'polls/detail.html' , {'faculty': faculty})

def results(request,faculty_id):
        response = "Results %s"
        return HttpResponse(response %faculty_id)
def vote(request,faculty_id):
        return HttpResponse("Voting on %s" %faculty_id)
