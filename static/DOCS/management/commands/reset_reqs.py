__author__ = 'barclajo'
from django.core.management.base import BaseCommand, CommandError
from DOCS.models import Merch_Requirement, Requirement, Testing_Procedure, Merchant, Finding


class Command(BaseCommand):
    def handle(self, *args, **options):
        for mr in Merch_Requirement.objects.all():
            print(mr)
            mr.req_status = 'Not In Place'
            mr.save()
        self.stdout.write("Successfully updated requirements")


