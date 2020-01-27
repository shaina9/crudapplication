from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

    class Meta:
        db_table ="employee"
    def __str__(self):
        return self.name
class Login(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.email

class Drop(models.Model):
    id = models.AutoField(primary_key=True)
    sub = models.CharField(max_length=30)

    def __str__(self):
        return self.sub


class Dropform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    sub = models.CharField(max_length=30)

    def __str__(self):
        return self.name

