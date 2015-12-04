from django.core.management.base import BaseCommand, CommandError
from DOCS.models import Merch_Requirement, Testing_Procedure, Merchant, Finding
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):

        for m in Merchant.objects.all():
            print(m)
            for r in m.merch_requirement_set.all():
                print(r)
                print(r.req_status)
                if r.expire_date is not None:
                    print("not none")
                    if r.expire_date < timezone.now():
                        print("expiring")
                        r.req_status = "Not In Place"
                        r.save()
                        r.finding_set.create(
                            finding_text = "Expired",
                            finding_date = timezone.now()
                        )
        self.stdout.write("Successfully expired requirements")

