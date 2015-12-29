import csv

from django.core.management.base import BaseCommand

from travel.models import Destination, Province



class Command(BaseCommand):
    args = 'file location'
    help = 'populate ethis user'

    def handle(self, *args, **options):
        total_records = 0

        filename = args[0]
        delimiter = options.get('delimiter', ';')
        open_file = open(filename, 'rU')
        reader = csv.DictReader(open_file, delimiter=delimiter)

        for row in reader:
            try:
                Province.objects.get(name=row['name'])
                print 'province already exist'
            except:                
                province = Province.objects.create(name=row['name'],
                                         short_description=row['short_description'],
                                         island=row['geographical_units'],
                                         url=row['url'],)
                province.save()

                print "{} province created".format(row['name'])

                total_records += 1

        print "total records = %s" % (str(total_records))


