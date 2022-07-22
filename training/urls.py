from django.urls import path
from . import views


urlpatterns = [
	path('learning', views.learning,name='learning')
]