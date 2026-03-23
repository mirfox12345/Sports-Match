from django.db import models

# Create your models here.

class Club(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	location = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=6, decimal_places=2)
