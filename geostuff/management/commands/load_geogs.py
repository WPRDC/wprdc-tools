from django.core.management import BaseCommand

from geostuff.data_collection.load import run


class Command(BaseCommand):

    def handle(self):
        run()