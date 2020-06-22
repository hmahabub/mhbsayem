from django.db import models

class specifics(models.Model):
    specifics = models.TextField()

class service(models.Model):
    service= models.TextField()

class basic(models.Model):
    basic_detail= models.TextField()

class basic_price(models.Model):
    basic_price= models.IntegerField()

class premium(models.Model):
    premium_detail = models.TextField()

class premium_price(models.Model):
    premium_price = models.IntegerField()

class message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

class projects(models.Model):
    image = models.ImageField()
    detail = models.TextField()
    link = models.URLField()


# Create your models here.
