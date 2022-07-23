from django.shortcuts import render
from .models import HomeDetail,Social

from projects.models import Project
from services.models import Service
from careers.models import Email
from contact.models import Contact

# Create your views here.
def home(request):
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

	homedetail = HomeDetail.objects
	social = Social.objects
	project = Project.objects
	

	return render(request,'dentcreatives/home.html',{
		'homedetail':homedetail,
		'social':social,
		'project':project,
		'service':Service.objects,
		'email':Email.objects,
		'feedback':feedback,
		})
