from django.contrib import admin
from .models import UserVolunteeringExperiences,UserDistinctions,PublicationType,UserPublications,UserResearchExperience,UserSkills,SocialUrls,UserInformations,WavingLines,UserEducation

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
@admin.register(UserResearchExperience)
class UserResearchExp(admin.ModelAdmin):
    list_display=[
        'pk','research_institute','research_project'
    ]
@admin.register(PublicationType)
class PublicationType(admin.ModelAdmin):
    list_display=[
        'pk','publication_type'
    ]

@admin.register(UserPublications)
class UserPublications(admin.ModelAdmin):
    list_display=[
        'pk','publication_type','publication_title'
    ]
@admin.register(UserDistinctions)
class UserDistinctions(admin.ModelAdmin):
    list_display=[
        'pk','distinction_title'
    ]

@admin.register(UserVolunteeringExperiences)
class VolunteeringExperience(admin.ModelAdmin):
    list_display=[
        'pk','designation_and_organization','duration'
    ]