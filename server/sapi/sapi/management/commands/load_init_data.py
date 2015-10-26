from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Loads the inital data into the database.'

    def handle(self, *args, **options):
        print "Loading Initial Data"
        from sapi.init_data import load
        load()