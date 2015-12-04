__author__ = 'barclajo'
from django.core.management.base import BaseCommand, CommandError
from DOCS.models import Merch_Requirement, Requirement, Testing_Procedure, Merchant, Finding


class Command(BaseCommand):
    def handle(self, *args, **options):

        ver = '3.1'

        saq = ['P2PE', 'D', 'C-VT', 'C', 'B', 'A-EP', 'A']
        for saq_sel in saq:
            merch = Merchant.objects.filter(saq_req=saq_sel)
            saq = Requirement.objects.filter(saq_req=saq_sel, version=ver)
            for m in merch:
                for req in saq:
                    mreq = m.merch_requirement_set.all()
                    try:
                        mr = mreq.get(merch_req_num = req.req_number)
                        print(mr)
                    except:
                        mr = Merch_Requirement(requirement=req, merchant=m)
                        print(m.merchant_name + ' ' + req.req_number + ' added')
                        mr.save()
        self.stdout.write("Successfully updated merchant requirements")


