from django.db import models

# Create your models here
class Registration(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    paddress = models.CharField(max_length = 255)
    taddress = models.CharField(max_length = 255)
    pnum = models.CharField(max_length=255)
    dob = models.CharField(max_length = 255)
    
    def __str__(self):
        return 'Registration of ' + self.name