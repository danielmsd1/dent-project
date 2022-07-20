from django.db import models

# Create your models here.
class Project(models.Model):
	client = models.CharField(max_length=200,unique=True)
	complete = models.BooleanField(default=False)
	cover_image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.client

class Sketch(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/')

class Image(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/')

class Video(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	code = models.CharField(max_length=200)

	def __str__(self):
		return self.code