from django.db import models

# Create your models here.
class Header(models.Model):
	header = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.header

class Member(models.Model):
	profile_image = models.ImageField(upload_to='images/')
	name = models.CharField(max_length=200)
	position = models.CharField(max_length=200)
	twitter = models.URLField(blank=True, null=True)
	instagram = models.URLField(blank=True, null=True)
	linkedin = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name
