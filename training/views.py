from django.shortcuts import render
from dentcreatives.models import Social
from .models import Program,Instructor
from services.models import Service
# Create your views here.

def learning(request):
	return render(request,'training/learning.html',{
		'social':Social.objects,
		'program':Program.objects,
		'instructor':Instructor.objects,
		'service':Service.objects,
	})