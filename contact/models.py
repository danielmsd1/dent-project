from email.policy import default
from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	reason = models.CharField(max_length=100)
	detail = models.TextField()
	status = models.CharField(max_length=100)

	def __str__(self):
		return '{0}, {1}'.format(self.reason, self.status)