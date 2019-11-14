from django.db import models

# Create your models here.
class Word(models.Model):
	name = models.CharField(max_length = 10000,null=False,unique=True)
	def __str__(self):
		return self.name