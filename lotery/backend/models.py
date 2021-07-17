from django.db import models

# Create your models here.

class Words(models.Model):
    word = models.CharField(max_length=30, blank=True, null=True)