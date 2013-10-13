from django.db import models

# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length=128,
        help_text='Name of Event')
    start_date = models.DateField(help_text='Start date of Event')
    end_date = models.DateField(help_text='End date of Event')
    start_time = models.TimeField(help_text='Start time of Event')
    end_time = models.TimeField(help_text='End Time of Event')
    description = models.TextField(help_text='Description of Event')

    def __str__(self):
      return '%s' % (self.name,)

class People(models.Model):
    fname = models.CharField(max_length=64, help_text='First Name')
    lname = models.CharField(max_length=64, help_text='Last Name')
    email = models.EmailField(max_length=128, help_text='Email Address')
    phone = models.CharField(max_length=16, help_text='Phone Number')
    enrollments= models.ManyToManyField(Events)