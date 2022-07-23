from django.shortcuts import render
from dentcreatives.models import Social
from .models import Program,Instructor
from services.models import Service
from contact.models import Contact
# Create your views here.

def learning(request):
	feedback = ''
	if request.method == 'POST':
		name = request.POST.get('name')
		email_address = request.POST.get('emailAddress')
		reason = request.POST.get('reason')
		detail = request.POST.get('detail')

		contact = Contact()
		contact.name = name 
		contact.email = email_address
		contact.reason = reason
		contact.detail = detail
		contact.status = 'Not resolved'
		contact.save()
		
		# Send the email at this point
		feedback = 'Submitted Successfully!'

	return render(request,'training/learning.html',{
		'social':Social.objects,
		'program':Program.objects,
		'instructor':Instructor.objects,
		'service':Service.objects,
		'feedback':feedback,
	})