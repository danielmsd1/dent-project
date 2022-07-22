from django.db import models

# Create your models here.
class Program(models.Model):
	name = models.CharField(max_length=200, unique=True)
	program_fee = models.CharField(max_length=200)
	duration = models.CharField(max_length=200)
	description = models.TextField()
	cover_image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name


class Instructor(models.Model):
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	profile_image = models.ImageField(upload_to='images/')
	bio = models.TextField()

	def __str__(self):
		return self.name