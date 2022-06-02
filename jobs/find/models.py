from distutils.command import upload
import profile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    profile = models.ImageField(upload_to='media/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    about = models.CharField(max_length=300)
    is_hiring  = models.BooleanField()

    def __str__(self):
        return self.Name

class Application(models.Model):
    Full_name = models.CharField(max_length=200)
    Age = models.IntegerField(default=18)
    Residence = models.CharField(max_length=200)
    number = models.BigIntegerField()
    email = models.EmailField()
    Cv = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.Full_name

class Individual(models.Model):
    Full_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_descr =  models.CharField(max_length=200)
    amount_due = models.IntegerField(default="$200")
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.job_title
