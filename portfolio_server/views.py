from django.shortcuts import render
from . models import WavingLines,UserEducation,UserInformations
from django.conf import settings

# Create your views here.

def portfolio_page(request):
    
    user=UserInformations.objects.get()
    user_id=user.pk
    wavingTags=WavingLines.objects.filter(user=UserInformations.objects.get(pk=user_id)).values('line')
    education_details=UserEducation.objects.filter(user=UserInformations.objects.get(pk=user_id)).values().order_by('-weight')
    media_url=settings.MEDIA_URL
    context={
        'user':user,
        'wavingTags':wavingTags,
        'education':education_details,
        'media_url':media_url,
        
    }
    return render(request,'index-2.html',context=context)