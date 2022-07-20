from django.db import models

# Create your models here.
class Program(models.Model):
	name = models.CharField(max_length=200, unique=True)
	program_fee = models.CharField(max_length=200)
	duration = models.CharField(max_length=200)
	cover_image = models.ImageField(upload_to='images/')


class Instructor(models.Model):
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	profile_image = models.ImageField(upload_to='images/')
	bio = models.TextField()