__author__ = 'barclajo'
from django.core.management.base import BaseCommand, CommandError
from DOCS.models import Requirement, Testing_Procedure, Merchant, Finding, Merch_Requirement, Hardware, Software, ServiceProvider, PaymentApplication, PaymentChannel, SAQ


class Command(BaseCommand):
    def handle(self, *args, **options):
        for r in Requirement.objects.all():
            print(r)
            s = SAQ.objects.get(saq_name=r.saq_req, saq_version=r.version)
            print(s)
            r.saq_required = s
            r.save()
#        for f in Finding.objects.all():
#            print(f)
#            f.save()
#        for mr in Merch_Requirement.objects.all():
#            print(mr)
#            mr.req_status = 'Not In Place'
#            mr.save()
        self.stdout.write("Successfully updated requirements")


