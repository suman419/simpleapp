from django.db import models


# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=40)
    smobile=models.IntegerField()
    ssal=models.FloatField()
    semail=models.CharField(max_length=50)
    saddress=models.CharField(max_length=256)
    simage=models.ImageField(null=True,blank=True,default="default.png")
    #height_field=models.IntegerField(default=0)
    #width_field=models.IntegerField(default=0)
