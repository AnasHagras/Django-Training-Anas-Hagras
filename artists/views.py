from django.db.models import Count, Q
from django.shortcuts import render

from .models import Artist


def index(request):
    data = {
        'albums' : Artist.objects.filter(Q(album__is_approved=True)).annotate(count = Count('album')).order_by('-count')
    }
    return render(request,"index.html",data)