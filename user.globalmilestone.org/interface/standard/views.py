from django.shortcuts import render
from standard.models import Student
# Create your views here.

def standard(request):
	students = Student.objects.all()
	context = {
		'students': students
	}
	return render(request, 'a_page.html', context)
