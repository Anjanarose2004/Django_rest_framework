from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField()
    place=models.CharField(max_length=100,null=True,blank=True)
    contact=models.IntegerField()
    email=models.EmailField(max_length=100,null=True,blank=True)
    designation=models.CharField(max_length=100,null=True,blank=True)
    company=models.CharField(max_length=100,null=True,blank=True)


class Donordb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField()
    blood_group=models.CharField(max_length=100,null=True,blank=True)
    last_donation=models.DateField()