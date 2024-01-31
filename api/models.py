from django.db import models

# Create your models here.
# Creating Company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    company_choice = (('IT','IT'),('Non IT','Non IT'))
    type = models.CharField(max_length=100, choices = company_choice)
    added_date = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Creating Employee model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    about = models.TextField(max_length=200)
    position = models.CharField(max_length=50, choices = (('Manager','manager'), ('Tech Lead','tech lead'), ('Developer','developer')))
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

    def __str__(self):
        return self.name