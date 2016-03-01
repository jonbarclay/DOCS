from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
import datetime
from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from .models import Requirement, Testing_Procedure, Merchant, Finding, Merch_Requirement, SAQ
from .forms import NameForm




@login_required(login_url='/login/')
def index(request):
    merchant_list = Merchant.objects.order_by('-saq_req', 'merchant_name')
    saq_list = SAQ.objects.order_by('-saq_risk')
    context = {'merchant_list': merchant_list, 'saq_list': saq_list}
    return render(request, 'DOCS/index.html', context)

@login_required(login_url='/login/')
def detail(request, requirement_id):
    requirement = get_object_or_404(Requirement, pk=requirement_id)
    return render(request, 'DOCS/detail.html', {'requirement': requirement})

@login_required(login_url='/login/')
def merchant(request, merchant_name_URL):
    merchant = get_object_or_404(Merchant, merchant_name_URL=merchant_name_URL)
    return render(request, 'DOCS/merchant.html', {'merchant': merchant})



class RequirementList(ListView):
    model = Requirement
    
@login_required(login_url='/login/')   
def merchant_requirement(request, merchant_name_URL, version, saq_req, req_number):
    users_in_group = request.user.groups.filter(name='pcidocs-admins').exists()
    # if this is a POST request we need to process the form data
    saq = get_object_or_404(SAQ, saq_name=saq_req, saq_version=version)
    merchant = get_object_or_404(Merchant, merchant_name_URL=merchant_name_URL)
    req = get_object_or_404(Requirement, req_number=req_number, saq_req=saq)
    merch_requirement = get_object_or_404(Merch_Requirement, requirement=req, merchant=merchant)
    req_children = req.child_req.all()
    merch_req_children = Merch_Requirement.objects.filter(requirement__in=req_children).filter(merchant=merchant).order_by(
        'merch_req_num_col1', 'merch_req_num_col2', 'merch_req_num_col3', 'merch_req_num_col4')

    if users_in_group :
        if request.method == 'POST':


            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                finding = form.cleaned_data['finding_text']
                merch_requirement_status = form.cleaned_data['status']
                current_user = request.user.get_full_name()
                finding_and_status = finding + " - " + str(merch_requirement_status) + " - " + str(current_user)
                time = timezone.now()
                merch_requirement.req_status = str(merch_requirement_status)
                merch_requirement.save()
                req_find = merch_requirement.finding_set
                req_find.create(
                    finding_text = finding,
                    finding_date = time,
                    req_status = str(merch_requirement_status),
                    user = str(current_user)
                    )

                # redirect to a new URL:
                return HttpResponseRedirect('./')
        else:
            form = NameForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'DOCS/merchant_requirement.html', {'form': form, 'merchant': merchant,
                                                              'merch_requirement': merch_requirement,
                                                              'merch_req_children': merch_req_children })

    

