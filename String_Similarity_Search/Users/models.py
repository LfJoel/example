from tkinter import CASCADE

from django.db import models

# Create your models here.
class UserRegister_Model(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    mobilenum = models.BigIntegerField()
    emailId = models.EmailField()
    location = models.CharField(max_length=100)
    dob = models.DateField()

class UserUpload_Model(models.Model):
    user = models.ForeignKey(UserRegister_Model, on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    original_cluster = models.CharField(max_length=200)
    update_original_cluster = models.CharField(max_length=200)
    cluster = models.CharField(max_length=200, default='pending')
    improved_cluster = models.CharField(max_length=200, default='pending')
    document = models.FileField(upload_to='doc/')
    tweet = models.CharField(max_length=500)
    topics = models.CharField(max_length=300)
    sentiment = models.CharField(max_length=300)

class UserMatch_Model(models.Model):
    useriid = models.ForeignKey(UserRegister_Model, on_delete=models.CASCADE,)
    sname=models.TextField()
    fname = models.TextField()
    differ = models.TextField()