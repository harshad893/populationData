from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

def display_topic(request):
    #topics=Topic.objects.all()
    topics=Topic.objects.get(topic_name='Cricket')
    
    d={'topics':topics}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.all()[1:6:1]
    webpages=Webpage.objects.all().order_by('name')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())
    webpages=Webpage.objects.filter(name='Cassandra')
    webpages=Webpage.objects.exclude(name='Cassandra')
    webpages=Webpage.objects.filter(name__startswith='y')
    webpages=Webpage.objects.filter(name__endswith='a')
    webpages=Webpage.objects.filter(name__contains='k')
    webpages=Webpage.objects.filter(name__in=('Mark','Erika','Harshad','Ashu'))
    webpages=Webpage.objects.filter(name__regex=r'E\w+')
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(Q(url__startswith='https') & Q(topic_name='Rummy') )
    #webpages=Webpage.objects.filter(Q(topic_name='Ludo') & Q(name='Nancy'))
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)

def display_access(request):
    access=Access_Records.objects.all()
    #access=Access_Records.objects.filter(date='1995-01-18')
    #access=Access_Records.objects.filter(date__year='1995')
    #access=Access_Records.objects.filter(date__month='01')
    #access=Access_Records.objects.filter(date__day='18')
    access=Access_Records.objects.filter(date__year__gte='2004')
    access=Access_Records.objects.filter(date__year__lte='2004')
    d={'access':access}
    return render(request,'display_access.html',d)

def update_webpage(request):
    #Webpage.objects.filter(name='Charles').update(url='https://www.Charles.info/')
    #Webpage.objects.filter(topic_name='Cricket').update(name='VK')
    #Webpage.objects.filter(name='DSP').update(topic_name='Cricket')
    #Webpage.objects.all().update(url='http:///Cricket.com')
    #Webpage.objects.update_or_create(name='Erika',defaults={'url':'https://Erika.com'})
    #Webpage.objects.update_or_create(name='VK',defaults={'url':'https://VK.com'})
    t=Topic.objects.get_or_create(topic_name='Cricket')[0]
    t.save()
    Webpage.objects.update_or_create(name='Ashu',defaults={'topic_name':t,'name':'Ashu','url':'https://Ashu.in'})
    webpages=Webpage.objects.all()


    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):
    #Webpage.objects.filter(name='Todd').delete()
    #Webpage.objects.filter(topic_name='Ludo').delete()
    Webpage.objects.all().delete()
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)


