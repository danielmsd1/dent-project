from django.db import models

# Create your models here.
class Service(models.Model):
	GRAPHICDESIGN = 'GD'
	MOTIONGRAPHICS = 'MG'
	SERVICES_OPTION = [
		(GRAPHICDESIGN,'Graphic Design'),
		(MOTIONGRAPHICS,'Motion Graphics')
	]
	name_of_service = models.CharField(
		choices=SERVICES_OPTION,
	)
	service_text = models.TextField()
	service_cover_image = models.ImageField(upload_to='images/', blank=True, null=True)