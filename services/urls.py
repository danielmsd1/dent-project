from django.urls import path
from . import views


urlpatterns = [
	path('service', views.rservice,name='rservice'),
	path('service/<int:serviceid>', views.service,name='service')
]