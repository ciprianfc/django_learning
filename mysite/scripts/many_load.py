import csv

# python3 manage.py runscript many_load

from many.models import Person, Course, Membership

def run():
    fhand = open('many/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Person.objects.all().delete()
    Course.objects.all().delete()
    Membership.objects.all().delete()
    
    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python
    
    for row in reader:
        print(row)

        p, created = Person.objects.get_or_create(email=row[0])
        c, created = Course.objects.get_or_create(title=row[2])

        r = Membership.INSTRUCTOR if row[1] == 'I' else Membership.LEARNER # ternary in python 

        m = Membership(role=r, person=p, course=c)
        m.save()
