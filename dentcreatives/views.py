from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'dentcreatives/home.html')


def portfolio(request):
	return render(request,'dentcreatives/projectsview.html')