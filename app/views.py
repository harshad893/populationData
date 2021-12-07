from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)
