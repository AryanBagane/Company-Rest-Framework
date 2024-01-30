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

# Creating Employee model
    
