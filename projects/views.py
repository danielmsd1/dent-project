from django.shortcuts import render, get_object_or_404
from .models import Project,Sketch,Image,Video
from dentcreatives.models import Social
from services.models import Service
# Create your views here.

def projectsview(request):
	project = Project.objects
	social = Social.objects
	return render(request,'projects/projectsview.html',{
		'project':project,
		'social':social,
		'service':Service.objects,
		})


def project(request,project_id):
	project_detail = get_object_or_404(Project,pk=project_id)
	project = Project.objects
	social = Social.objects
	sketch = Sketch.objects
	image = Image.objects
	video = Video.objects
	return render(request,'projects/project.html',{
		'project':project,
		'social':social,
		'sketch':sketch,
		'image':image,
		'video':video,
		'project1':project_detail,
		'service':Service.objects,
	})