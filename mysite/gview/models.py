from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=128)

class Dog(models.Model):
    name = models.CharField(max_length=128)

class Horse(models.Model):
    name = models.CharField(max_length=128)

class Car(models.Model):
    name = models.CharField(max_length=128)

