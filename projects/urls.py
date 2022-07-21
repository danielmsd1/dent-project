from django.urls import path
from . import views


urlpatterns = [
	path('projectsview', views.projectsview,name='projectsview'),
	path('project/<int:project_id>', views.project,name='project')
]