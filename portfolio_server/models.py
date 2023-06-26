from django.db import models
from django.urls import reverse

# Create your models here.


class UserInformations(models.Model):

    first_Name=models.CharField(null=False,blank=False, max_length=50)
    middle_name=models.CharField(null=True,blank=True,max_length=50)
    last_name=models.CharField(null=True,blank=True,max_length=50)
    about_info=models.CharField(null=True,blank=True,max_length=500)
    user_picture=models.ImageField(null=True,blank=True,upload_to='user_pictures/')
    user_cv=models.FileField(null=True,blank=True,upload_to='user_cv/')
    age=models.IntegerField(null=False,blank=False)
    email=models.EmailField(null=False,blank=False,max_length=60)
    address=models.CharField(null=True,blank=True,max_length=100)
    phone=models.CharField(null=True,blank=True,max_length=40)
    
    
    
    class Meta:
        verbose_name = "User Details"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})