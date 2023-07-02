from django.core.mail import send_mail
from django.conf import settings


def sendEmailToOwner(name,recipentMail,email,email_subject,message):
    
        # send mail to owner

    subject="You have a new message in your Portfolio Website"
    
    email_message=f"A new message arrived!\n\nName :{name}\nEmail: {email}\nSubject:{email_subject}\n\nMessage: {message}\n\nThis email was automatically generated from the portfolio site!"
    
    email_from=settings.EMAIL_HOST_USER
    
    recipientList=[recipentMail]
    try:
        send_mail(
        subject,email_message,email_from,recipient_list=recipientList
        )
        return True
    
    except:
        return False
