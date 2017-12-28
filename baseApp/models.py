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