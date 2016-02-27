import os
import csv
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CDX2016.settings')

import django
django.setup()

from Citadel.models import UserProfile,User,BankingDetails


def readcsv():
    with open("data.csv","rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        count = 0
        for row in reader:
            count += 1
            templist = row[0].split(",")[1:]
            add_user(templist[0],templist[1],Decimal(templist[2]),count)



def add_user(lastname,firstname,balance,count):
    u = User()
    usernamestring = firstname + lastname + str(count)
    print usernamestring
    u.username = usernamestring
    u.password = make_random_password(15)
    u.save()
    c = UserProfile.objects.create(user=u)
    c.name = firstname
    c.surname = lastname
    print c.name
    c.save()
    print balance
    b = BankingDetails.objects.create(user=c,Balance=balance)
    b.save()
    return True

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    readcsv()
