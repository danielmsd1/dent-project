from tabnanny import verbose
from django.db import models

# Create your models here.
class Email(models.Model):
	email = models.EmailField()

	class Meta:
		verbose_name_plural='Application Email'

	def __str__(self):
		return self.email

class Position(models.Model):
	FULLTIME = 'FT'
	PARTTIME = 'PT'
	POSITIONTYPE = [
		(FULLTIME,'Full-time'),
		(PARTTIME,'Part-time'),
	]
	title = models.CharField(max_length=200)
	description = models.TextField()
	slots = models.IntegerField()
	type = models.CharField(
		max_length=2,
		choices=POSITIONTYPE,
		default=PARTTIME
	)

	def __str__(self):
		return self.title

class Responsibility(models.Model):
	position = models.ForeignKey(Position,on_delete=models.CASCADE)
	responsibility = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural='Responsibilities'

	def __str__(self):
		return self.responsibility