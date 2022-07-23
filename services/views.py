from django.shortcuts import render,get_object_or_404
from dentcreatives.models import Social
from .models import Service,Detail
from contact.models import Contact

# Create your views here.
def service(request,serviceid):
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

	serviceid = get_object_or_404(Service,pk=serviceid)
	return render(request,'services/service.html',{
		'social':Social.objects,
		'service':Service.objects,
		'detail':Detail.objects,
		'serviceid':serviceid,
		'feedback':feedback,
	})

def rservice(request):
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
	return render(request,'services/service.html',{
		'social':Social.objects,
		'service':Service.objects,
		'detail':Detail.objects,
		'feedback':feedback,
	})