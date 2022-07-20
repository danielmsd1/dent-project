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
		max_length=2,
		choices=SERVICES_OPTION,
		unique=True,
	)
	service_text = models.TextField()
	service_cover_image = models.ImageField(upload_to='images/', blank=True, null=True)


	def __str__(self) -> str:
		return self.name_of_service