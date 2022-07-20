from django.db import models

# Create your models here.
class HomeDetail(models.Model):
	title = models.CharField(max_length=200)
	cover_image = models.ImageField(upload_to='images/')
	about_text = models.TextField()