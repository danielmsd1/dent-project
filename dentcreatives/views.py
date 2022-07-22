from django.shortcuts import render
from .models import HomeDetail,Social
# Create your views here.
from projects.models import Project
from services.models import Service

def home(request):
	homedetail = HomeDetail.objects
	social = Social.objects
	project = Project.objects

	return render(request,'dentcreatives/home.html',{
		'homedetail':homedetail,
		'social':social,
		'project':project,
		'service':Service.objects,
		})
