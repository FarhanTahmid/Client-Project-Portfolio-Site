from django.shortcuts import render
from . models import UserVolunteeringExperiences,UserDistinctions,UserPublications,PublicationType,UserResearchExperience,UserSkills,SocialUrls,WavingLines,UserEducation,UserInformations
from . import email_handler
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def portfolio_page(request):
    
    user=UserInformations.objects.get()
    user_id=user.pk
    wavingTags=WavingLines.objects.filter(user=UserInformations.objects.get(pk=user_id)).values('line')
    education_details=UserEducation.objects.filter(user=UserInformations.objects.get(pk=user_id)).values().order_by('-weight')
    social_links=SocialUrls.objects.filter(user=UserInformations.objects.get(pk=user_id)).values()
    media_url=settings.MEDIA_URL
    social_links=social_links[0] #getting the first object only
        
    user_skills=UserSkills.objects.filter(user=UserInformations.objects.get(pk=user_id)).values().order_by('-skill_weight')

    research_experience=UserResearchExperience.objects.filter(user=UserInformations.objects.get(pk=user_id)).values().order_by('-research_weight')

    international_publications=UserPublications.objects.filter(user=UserInformations.objects.get(pk=user_id),publication_type=PublicationType.objects.get(publication_type='International Conference')).values().order_by('-publication_year','-weight')
    national_publications=UserPublications.objects.filter(user=UserInformations.objects.get(pk=user_id),publication_type=PublicationType.objects.get(publication_type='National Conference')).values().order_by('-publication_year','-weight')
    journal_publications=UserPublications.objects.filter(user=UserInformations.objects.get(pk=user_id),publication_type=PublicationType.objects.get(publication_type='Journal')).values().order_by('-publication_year','-weight')

    total_publication_count=UserPublications.objects.filter(user=UserInformations.objects.get(pk=user_id)).count()
    
    distinctions=UserDistinctions.objects.filter(user=UserInformations.objects.get(pk=user_id)).values().order_by('-pk')

    volunteering_experience=UserVolunteeringExperiences.objects.filter(user=UserInformations.objects.get(pk=user_id)).values().order_by('pk')

    if(request.method=="POST"):
        
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        
        mail_to_owner=email_handler.sendEmailToOwner(name=name,recipentMail=user.email,email=email,email_subject=subject,message=message)
        
        if(mail_to_owner):
            messages.success(request,'Your message has been sent successfully')
            return HttpResponseRedirect(request.path+'#contact')
        
    context={
        'user':user,
        'wavingTags':wavingTags,
        'education':education_details,
        'media_url':media_url,
        'links':social_links,
        'skills':user_skills,
        'research_exp':research_experience,
        'international_publications':international_publications,
        'national_publications':national_publications,
        'journal_publications':journal_publications,
        'inter_pub_count':international_publications.count(),
        'national_pub_count':national_publications.count(),
        'journal_pub_count':journal_publications.count(),
        'total_pub_count':total_publication_count,
        'distinctions':distinctions,
        'volunteerings':volunteering_experience,
    }
    return render(request,'index-2.html',context=context)