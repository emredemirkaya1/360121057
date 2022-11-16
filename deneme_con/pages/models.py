from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=50, verbose_name="Work Name")

class Teamss(models.Model):
    firstname=models.CharField(max_length=50, verbose_name="Firstname")
    lastname=models.CharField(max_length=50, verbose_name="Lastname")
    city=models.CharField(max_length=50, verbose_name="City")
    country=models.CharField(max_length=50, verbose_name="Country")
    position=models.CharField(max_length=50, verbose_name="Company Position")
    description=models.TextField(max_length=200, blank=True, null=True)
