from django.shortcuts import render,get_object_or_404
from dentcreatives.models import Social
from .models import Service,Detail


# Create your views here.
def service(request,serviceid):
	serviceid = get_object_or_404(Service,pk=serviceid)
	return render(request,'services/service.html',{
		'social':Social.objects,
		'service':Service.objects,
		'detail':Detail.objects,
		'serviceid':serviceid,
	})

def rservice(request):
	return render(request,'services/service.html',{
		'social':Social.objects,
		'service':Service.objects,
		'detail':Detail.objects,
	})