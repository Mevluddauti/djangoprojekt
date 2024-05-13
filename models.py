from django.db import models

# Create your models here.
class Reservation(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  location = models.CharField(max_length=50)
  date = models.DateField()
  time = models.TimeField()