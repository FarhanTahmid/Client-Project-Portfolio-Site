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
        verbose_name = "User Detail"

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
        verbose_name="User Education Detail"
        
    def __str__(self) -> str:
        return str(self.pk)
    def get_absolute_url(self):
        return reverse("education", kwargs={"degree_name": self.degree_name})


class SocialUrls(models.Model):
    user=models.ForeignKey(UserInformations,on_delete=models.CASCADE,null=False)
    facebook_link=models.CharField(null=True,blank=True,max_length=200)
    linkedin_link=models.CharField(null=True,blank=True,max_length=200)
    google_scholar_link=models.CharField(null=True,blank=True,max_length=200)
    
    class Meta:
        verbose_name="User Socials Url"

    def __str__(self) -> str:
        return str(self.pk)
    
    def get_absolute_url(self):
        return reverse("social_url", kwargs={"pk": self.pk})
    
class UserSkills(models.Model):
    user=models.ForeignKey(UserInformations,on_delete=models.CASCADE,null=False)
    skill_icon_picture=models.ImageField(null=True,upload_to='skill_icons/')
    skill_name=models.CharField(null=False,blank=False,max_length=100)
    skill_description=models.TextField(null=True,blank=True,max_length=500)
    skill_weight=models.IntegerField(null=False,blank=False,default=1)
    
    class Meta:
        verbose_name="User Skill"
        
    def __str__(self) -> str:
        return str(self.pk)
    def get_absolute_url(self):
        return reverse("skills", kwargs={"pk": self.pk})
    
class UserResearchExperience(models.Model):
    user=models.ForeignKey(UserInformations,on_delete=models.CASCADE,null=False)
    research_institute=models.CharField(null=False,blank=False,max_length=150)
    research_project=models.CharField(null=True,blank=True,max_length=200)
    project_description=models.TextField(null=True,blank=True,max_length=500)
    project_outcome=models.CharField(null=True,max_length=200)
    research_weight=models.TextField(null=False,blank=False,default=1)
    
    class Meta:
        verbose_name="User Research Experience"
        
    def __str__(self):
        return str(self.pk)
    def get_absolute_url(self):
        return reverse("research_experience", kwargs={"pk": self.pk})

class PublicationType(models.Model):
    publication_type=models.CharField(null=False,blank=False,max_length=100)
    
    class Meta:
        verbose_name="Publication Type"
    def __str__(self) -> str:
        return self.publication_type

class UserPublications(models.Model):
    user=models.ForeignKey(UserInformations,on_delete=models.CASCADE,null=False)
    publication_type=models.ForeignKey(PublicationType,on_delete=models.CASCADE,null=False)
    publication_title=models.CharField(null=False,max_length=200)
    publication_in=models.CharField(null=False,max_length=200)
    publishers_name=models.CharField(null=True,max_length=500)
    citation_link=models.CharField(null=True,max_length=200)
    picture=models.ImageField(null=True,default='user_publications/default.png',upload_to='user_publications/')
    publication_year=models.IntegerField(null=True,blank=True)
    weight=models.IntegerField(null=False,blank=False,default=1)
    
    class Meta:
        verbose_name="User Publication"
    def __str__(self) -> str:
        return str(self.pk)
    def get_absolute_url(self):
        return reverse("publications", kwargs={"pk": self.pk})
    
        
class WavingLines(models.Model):
    user=models.ForeignKey(UserInformations,on_delete=models.CASCADE)
    line=models.CharField(null=False,blank=False,max_length=100)
    
    class Meta:
        verbose_name="Tag Line"
        
    def __str__(self):
        return self.line
    
    def get_absolute_url(self):
        return reverse("waving_lnes", kwargs={"pk": self.pk})
    