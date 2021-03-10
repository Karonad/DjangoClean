from django.db import models

# Create your models here.
class Fruits(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)