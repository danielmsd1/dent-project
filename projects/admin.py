from django.contrib import admin
from .models import Project,Sketch,Image,Video

# Register your models here.
admin.site.register(Project)
admin.site.register(Sketch)
admin.site.register(Image)
admin.site.register(Video)