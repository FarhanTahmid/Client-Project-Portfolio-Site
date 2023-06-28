from django.contrib import admin
from .models import UserSkills,SocialUrls,UserInformations,WavingLines,UserEducation

# Register your models here.

@admin.register(WavingLines)
class WavingLines(admin.ModelAdmin):
    list_display=[
        'pk','line'
    ]

@admin.register(UserInformations)
class UserInformation(admin.ModelAdmin):
    list_display=[
        'pk','first_name','email','nationality','phone'
    ]

@admin.register(UserEducation)
class UserEducation(admin.ModelAdmin):
    list_display=[
        'pk','user','degree_name','duration'
    ]

@admin.register(SocialUrls)
class SocialUrls(admin.ModelAdmin):
    list_display=[
        'pk','facebook_link','linkedin_link'
    ]

@admin.register(UserSkills)
class UserSkills(admin.ModelAdmin):
    list_display=[
        'pk','skill_name'
    ]