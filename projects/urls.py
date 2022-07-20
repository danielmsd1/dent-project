from django.urls import path

from dentcreatives import views
# from . import views


urlpatterns = [
	path('portfolio', views.portfolio,name='portfolio'),
]