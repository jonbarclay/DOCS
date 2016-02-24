from django.conf.urls import url, patterns, include
import DOCS.views
from . import views
from DOCS.views import RequirementList

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^requirements/$', RequirementList.as_view()),
    url(r'^(?P<requirement_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^merchant/(?P<merchant_name>[-\w]+)/$', views.merchant, name='merchant'),
    url(r'^merchant/(?P<merchant_name_URL>[-\w]+)/(?P<version>[\w.]+)/(?P<saq_req>[\w]+)/(?P<req_number>[\w.]+)/$', views.merchant_requirement, name='merchant_requirement'),
    
    
]