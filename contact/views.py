from django.shortcuts import render
from services.models import Service
# Create your views here.

def contact(request):
	if request.method == 'POST':
		print(request.POST)
	return render(request,'contact/contact_form.html',{
		'service':Service.objects,
	})