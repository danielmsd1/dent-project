from django.urls import path

from dentcreatives import views
# from . import views


urlpatterns = [
	# path('',views.home,name='home'),
	# path('home',views.home,name='home'),
	path('portfolio', views.portfolio,name='portfolio'),
]