from django.db import models
from django.urls import reverse

# Create your models here.
class UserInformations(models.Model):

    first_name=models.CharField(null=False,blank=False, max_length=50)
    middle_name=models.CharField(null=True,blank=True,max_length=50)
    last_name=models.CharField(null=True,blank=True,max_length=50)
    about_info=models.TextField(null=True,blank=True,max_length=2000)
    interest=models.TextField(null=True,max_length=1000)
    user_picture=models.ImageField(null=True,blank=True,upload_to='user_pictures/')
    banner_picture=models.ImageField(null=True,upload_to='banner_pictures/')
    user_cv=models.FileField(null=True,blank=True,upload_to='user_cv/')
    age=models.IntegerField(null=False,blank=False)
    email=models.EmailField(null=False,blank=False,max_length=60)
    address=models.CharField(null=True,blank=True,max_length=100)
    phone=models.CharField(null=True,blank=True,max_length=40)
    nationality=models.CharField(null=True,blank=True,max_length=40)
    
    
    class Meta:
        verbose_name = "User Details"

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class UserEducation(models.Model):
    user=models.ForeignKey(UserInformations,on_delete=models.CASCADE)
    degree_name=models.CharField(null=False,blank=False,max_length=200)
    duration=models.CharField(null=False,blank=False,max_length=50)
    institutions=models.CharField(null=True,blank=True,max_length=200)
    description=models.TextField(null=True,blank=True,max_length=1000)
    project=models.TextField(null=True,blank=True,max_length=1000)
    specific_degree=models.CharField(null=True,blank=True,max_length=120)
    weight=models.IntegerField(null=False,blank=False,default=1)
    class Meta:
        verbose_name="User Education Details"
        
    def __str__(self) -> str:
        return str(self.pk)
    def get_absolute_url(self):
        return reverse("education", kwargs={"degree_name": self.degree_name})








class WavingLines(models.Model):
    user=models.ForeignKey(UserInformations,on_delete=models.CASCADE)
    line=models.CharField(null=False,blank=False,max_length=100)
    
    class Meta:
        verbose_name="Tag Lines"
        
    def __str__(self):
        return self.line
    
    def get_absolute_url(self):
        return reverse("waving_lnes", kwargs={"pk": self.pk})
    