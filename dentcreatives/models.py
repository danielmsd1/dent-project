from django.db import models

# Create your models here.
class HomeDetail(models.Model):
	title = models.CharField(max_length=200)
	cover_image = models.ImageField(upload_to='images/',blank=True,null=True)
	about_text = models.TextField()

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name_plural='Home Details'

class Social(models.Model):
	facebook = models.URLField(blank=True, null=True)
	instagram = models.URLField(blank=True, null=True)
	twitter = models.URLField(blank=True, null=True)

	class Meta:
		verbose_name_plural='Social Media'