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
                Destination.objects.get(name=row['name'])
                print 'destination already exist'
            except:				                
                prov = Province.objects.get(name=row['province'])
                destination = Destination.objects.create(name=row['name'],
                                         short_description=row['short_description'],
                                         province_name=prov,
                                         url=row['url'],
                                         latitude=row['latitude'],
                                         longitude=row['longitude'],
                                         tagline=row['tagline'],                                         
                                         )
                destination.save()

                print "{} destination created".format(row['name'])

                total_records += 1

        print "total records = %s" % (str(total_records))


