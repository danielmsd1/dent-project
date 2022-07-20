from django.db import models

# Create your models here.
class HomeDetail(models.Model):
	title = models.CharField(max_length=200)
	cover_image = models.ImageField(upload_to='images/')
	about_text = models.TextField()

	def __str__(self):
		return self.title

class Social(models.Model):
	facebook = models.URLField()
	instagram = models.URLField()
	twitter = models.URLField()

class Project(models.Model):
	client = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	cover_image = models.ImageField(upload_to='images/')

class Sketch(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/')

class Image(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/')

class Video(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	code = models.CharField(max_length=200)
