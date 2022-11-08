import csv
from cats.models import Cat, Breed

# https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript cats_load


def run():
    fhand = open('cats/meow.csv')
    reader = csv.reader(fhand)
    next(reader)  # advance past the header

    Cat.objects.all().delete()
    Breed.objects.all().delete()

    for row in reader:
        print(row)

        b, created = Breed.objects.get_or_create(name=row[1])

        c = Cat(nickname=row[0], breed=b, weight=row[2])
        c.save()
