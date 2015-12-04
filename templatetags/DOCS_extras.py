from django import template
from django.template.loader import get_template
from DOCS.models import Requirement, Testing_Procedure, Merchant

register = template.Library()
#m = get_template('merchant_list.html')
#register.inclusion_tag(m)(nav_merchantlists)

@register.inclusion_tag('DOCS/merchant_list.html')
def nav_merchantlist():
    merchants = Merchant.objects.order_by('merchant_name')
    return {'merchants': merchants}