from celery import shared_task
from django.core.mail import send_mail
from musicplatform import settings
from users.models import User
from artists.serializers.ArtistSerializer import ArtistSerializer

@shared_task()
def send_congratulation_email( album , artist ):
    subject = "Django-Traning AnasHagras!"
    message = f"Hello {artist.get('stageName')} , Your album {album} has been created successfully , thanks\
 for using our platform!"
    sentTo = User.objects.get(id=artist.get('user')).email
    send_mail(
        subject=subject,message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[sentTo,]
        ,fail_silently=True)
    return "Sent!"
    