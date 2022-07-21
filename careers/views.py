from django.shortcuts import render,get_object_or_404
from .models import Email,Position,Responsibility
from dentcreatives.models import Social

# Create your views here.
def careersview(request):
	return render(request,'careers/careersview.html',{
		'position':Position.objects,
		'social':Social.objects,
	})

def career(request, careerid):
	careerid1 = get_object_or_404(Position,pk=careerid)
	
	return render(request,'careers/career.html',{
		'email':Email.objects,
		'position':Position.objects,
		'responsibility':Responsibility.objects,
		'social':Social.objects,
		'careerid':careerid1,
	})