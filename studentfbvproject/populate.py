import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentfbvproject.settings')
import django
django.setup()

from studentapp.models import *
from faker import Faker
from random import *

faker=Faker()
def phonenumbergen():
    d1=randint(7777777777,9999999999)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
        mobile=int(num)
        return mobile

def populate(n):
    for i in range(n):

        fsname=faker.name()
        fssal=randint(20000,30000)
        fsemail=faker.email()
        fsmobile=phonenumbergen()
        fsaddress=faker.city()
        emp_record=Student.objects.get_or_create(sname=fsname,ssal=fssal,smobile=fsmobile,semail=fsemail,saddress=fsaddress)
populate(15)
