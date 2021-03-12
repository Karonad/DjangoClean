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

class Cv(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    mail = models.EmailField()
    phone_number = models.IntegerField()
    age = models.IntegerField()
    permis = models.BooleanField()
    city = models.CharField(max_length=100)
    sector = models.CharField(max_length=100,default='none' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)

class Experience(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    start_at = models.DateTimeField(auto_now_add=False)
    end_at = models.DateTimeField(auto_now_add=False)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)

class Formation(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    start_at = models.DateTimeField(auto_now_add=False)
    end_at = models.DateTimeField(auto_now_add=False)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)

