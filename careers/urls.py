from django.urls import path


from . import views

urlpatterns = [
	path('careersview',views.careersview,name='careersview'),
	path('career/<int:careerid>',views.career,name='career'),
]