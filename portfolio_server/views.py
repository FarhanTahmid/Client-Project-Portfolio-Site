from django.shortcuts import render
from . models import SocialUrls,WavingLines,UserEducation,UserInformations
from django.conf import settings

# Create your views here.

def portfolio_page(request):
    
    user=UserInformations.objects.get()
    user_id=user.pk
    wavingTags=WavingLines.objects.filter(user=UserInformations.objects.get(pk=user_id)).values('line')
    education_details=UserEducation.objects.filter(user=UserInformations.objects.get(pk=user_id)).values().order_by('-weight')
    social_links=SocialUrls.objects.filter(user=UserInformations.objects.get(pk=user_id)).values()
    media_url=settings.MEDIA_URL
    social_links=social_links[0]
    context={
        'user':user,
        'wavingTags':wavingTags,
        'education':education_details,
        'media_url':media_url,
        'links':social_links,
        
    }
    return render(request,'index-2.html',context=context)