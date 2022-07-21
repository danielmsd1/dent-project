from django.shortcuts import render
from .models import Header,Member
from dentcreatives.models import Social

# Create your views here.
def team(request):
	return render(request,'team/team.html',{
		'header': Header.objects,
		'member': Member.objects,
		'social':Social.objects,
	})