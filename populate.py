# setting the Django EnvironMent
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project14.settings')
# access Django Features
import django
django.setup()
from app.models import *
import random as rm
from faker import Faker
f=Faker()
L=['Mario','Ludo',"SquidGame","Rummy"]
def add_topic():
    t=Topic.objects.get_or_create(topic_name=rm.choice(L))[0]
    t.save()
    return t
def add_webpage(name,url):
    t=add_topic()
    w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
    w.save()
    return w

def add_records(name,url,date):
    w=add_webpage(name,url)
    a=Access_Records.objects.get_or_create(name=w,date=date)[0]
    a.save()


def add_data():
    n=int(input('enter n value'))
    for i in range(n):
        f_name=f.first_name()
        f_url=f.url()
        f_date=f.date()
        add_records(f_name,f_url,f_date)
if __name__=='__main__':
    print('population is started')
    add_data()
    print('population is ended')