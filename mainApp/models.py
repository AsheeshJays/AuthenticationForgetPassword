from django.db import models
from django.db.models.fields import EmailField
from django.db.models.fields.related import ForeignKey

class UserModel(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15,default=None,null=True,blank=True)
    city = models.CharField(max_length=50,default=None,null=True,blank=True)
    otp = models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return str(self.uid)+' '+self.name 