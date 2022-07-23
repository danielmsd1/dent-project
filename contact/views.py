from django.shortcuts import render
from services.models import Service
from .forms import ContactForm
# Create your views here.

def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		print(request.POST)
	return render(request,'contact/contact_form.html',{
		'service':Service.objects,
		'form':form
	})