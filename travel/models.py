from django.db import models

# Create your models here.


'''
class Destination():
    id:int
    name:str
    img:str
    desc:str
    price:int
    offer:bool

'''
class Destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class Contact(models.Model):
    contact_address=models.CharField(max_length=250)
    contact_phone=models.IntegerField()
    contact_email=models.EmailField(max_length=100)

class Contact_Blog(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message= models.TextField()