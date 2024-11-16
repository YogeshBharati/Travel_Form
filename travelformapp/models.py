from django.db import models

# Create your models here.
class Travel(models.Model):
 name = models.CharField(max_length=100)
 email = models.EmailField()
 travelfrom = models.CharField(max_length=100)
 travelto = models.CharField(max_length=100)
 traveldate = models.DateField()

 def __str__(self):
  return self.name