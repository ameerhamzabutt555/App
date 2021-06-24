from django.db import models
from django.urls import reverse
# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    age = models.IntegerField()

    def get_absolute_url(self):
        return  reverse('students', kwargs={'pk':self.pk})
