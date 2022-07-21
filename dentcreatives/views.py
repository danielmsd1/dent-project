from django.shortcuts import render
from .models import HomeDetail,Social
# Create your views here.
from projects.models import Project

def home(request):
	homedetail = HomeDetail.objects
	social = Social.objects
	project = Project.objects

	return render(request,'dentcreatives/home.html',{
		'homedetail':homedetail,
		'social':social,
		'project':project,
		})
