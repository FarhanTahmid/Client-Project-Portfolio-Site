from django.contrib import admin
from .models import UserInformations,WavingLines,UserEducation

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
