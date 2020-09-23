from django.shortcuts import render
from standard.models import Student
# Create your views here.

def standard(request):
	context  = {}
	return render(request, 'login.html', context)
