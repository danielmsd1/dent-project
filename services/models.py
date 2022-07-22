from django.db import models

# Create your models here.
class Service(models.Model):
	name = models.CharField(
		max_length=200,
		unique=True,
	)

	def __str__(self) -> str:
		return self.name


class Detail(models.Model):
	service = models.ForeignKey(Service,on_delete=models.CASCADE)
	description = models.TextField()
	cover_image = models.ImageField(upload_to='images/',blank=True,null=True)

	def __str__(self) -> str:
		return self.description

	class Meta:
		verbose_name_plural='Service Details'