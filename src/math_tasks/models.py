from django.db import models

# Create your models here.
class Task(models.Model):
	content = models.TextField(blank=False, null=True)