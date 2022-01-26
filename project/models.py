from tkinter import CASCADE
from django.db import models
from django.conf import settings

from account.models import User

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()

    id= models.AutoField(primary_key=True, null=False, blank=False)
    created_at= models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)