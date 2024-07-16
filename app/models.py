from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    about=models.TextField()
    college=models.CharField(max_length=20)
    degree =models.CharField(max_length=20)
    project = models.TextField()

class resumeProfile(models.Model):
    resume_id= models.ForeignKey(profile, on_delete=models.CASCADE)