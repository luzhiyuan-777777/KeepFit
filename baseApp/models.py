from django.db import models
from datetime import datetime

# Create your models here.
class LoginDatas(models.Model):
    # logging the info of user, email and password
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=20)
    Registerdate = models.DateField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.Username

class Symptom(models.Model):
    # symptom
    Meridian = models.CharField(max_length=30)
    MeridianName = models.CharField(max_length=30)
    CreateTime = models.DateField(auto_now_add=True)
    UpdateTime = models.DateField(auto_now=True)
    Symptom = models.TextField()
    ValidFlag = models.CharField(max_length=2)
    MeridianRoute = models.TextField(default='经络路线')

    def __unicode__(self):
        return self.Meridian

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.CreateTime = datetime.now
        self.UpdateTime = datetime.now
        return super(Symptom, self).save(*args, **kwargs)

class Point(models.Model):
    # Point
    Point = models.CharField(max_length=30)
    PointName = models.CharField(max_length=30)
    Meridian = models.CharField(max_length=30)
    MeridianName = models.CharField(max_length=30)
    CreateTime = models.DateField(auto_now_add=datetime.now, blank=True)
    UpdateTime = models.DateField(auto_now=datetime.now, blank=True)
    PointPosition = models.TextField()
    PointStep = models.CharField(max_length=2,default='1')
    ValidFlag = models.CharField(max_length=2)

    def __unicode__(self):
        return self.Point