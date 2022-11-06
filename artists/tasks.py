from musicplatform import settings
from users.models import User
from artists.serializers.ArtistSerializer import ArtistSerializer
from artists.models import Artist
from datetime import datetime , timezone
from celery import shared_task
from dateutil.relativedelta import relativedelta
from albums.models import Album
from django.core.mail import send_mail
from musicplatform import settings
import pytz

@shared_task()
def send_warning_messages():
    artists = Artist.objects.filter()
    sentTo = []
    for artist in artists:
        # print("First : " , (datetime.now().replace(tzinfo=timezone.utc)-relativedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S"))
        # print("Second : " ,pytz.utc.localize(datetime.now()).strftime("%Y-%m-%d %H:%M:%S"))
        # print("Query : ",Album.objects.filter(created_at__range=[(pytz.utc.localize(datetime.now())-relativedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S"),pytz.utc.localize(datetime.now()).strftime("%Y-%m-%d %H:%M:%S")]).filter(is_approved=True))
        # print("Real Date : " , Album.objects.get(name="Second").created_at)
        albums = Album.objects.filter(created_at__range=[(pytz.utc.localize(datetime.now())-relativedelta(months=1,hours=2)).strftime("%Y-%m-%d %H:%M:%S"),pytz.utc.localize(datetime.now()).strftime("%Y-%m-%d %H:%M:%S")]).filter(is_approved=True)
        # print(artist,albums)
        if len(albums) == 0:
            sentTo.append(User.objects.get(id=artist.user.id).email) 
    subject = "Warning From Musicplatform"
    # print("Update : " , sentTo)
    message = f"Hello {artist.stageName} , You haven't published any albums since a month ago , \
 you are losing your popularity , so please join us again and publish more albums !"
    for toEmail in sentTo:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[toEmail,]
            ,fail_silently=True)
        # print ("Sent email To " + artist.stageName)
    return "Finished Sending Warning Messages!"
