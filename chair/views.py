from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.utils.encoding import smart_str
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import os
from delegation.models import Committee, PositionPaper, Allocation
from secretariat.models import LogisticsRequest, Chair, ProgressSheet
from secretariat.forms import LogisticsRequestForm, ProgressSheetForm

# Create your views here.


def index(request):
    TITLE = "Home"
    if request.user.is_authenticated:
        if request.user.is_chair:

            pages = {
                "Logistics Requests": "requests/",
                "Committee Progress Sheet": "sheet/",
                "Position Papers": "position_papers/",
            }
            return render(request,
                          "chair/index.html",
                          {"title": TITLE,
                          "tenant": request.tenant,
                           "pages": pages})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def sheet(request):
    TITLE = "Progress Sheet"
    if request.user.is_authenticated:
        if request.user.is_chair:

            #Get user profile and committee
            profile = Chair.objects.get(user=request.user)
            own_committee = profile.committee
            try:
                #Get sheet of committee
                sheet = ProgressSheet.objects.get(committee=own_committee)
            except ObjectDoesNotExist:
                #If committee does not have sheet, create it
                new_sheet = ProgressSheet(committee=own_committee)
                new_sheet.save()

            if request.method == "POST":
                sheet = ProgressSheet.objects.get(committee=own_committee)
                form = ProgressSheetForm(request.POST, instance=sheet)
                if form.is_valid():
                    updated_sheet = form.save()
                    messages.info(request, "Sheet updated")
                    return redirect('chair:sheet')

            else:
                #Render sheet as form
                sheet = ProgressSheet.objects.get(committee=own_committee)
                form = ProgressSheetForm(instance=sheet)
                return render(request,
                              "chair/sheet.html",
                              {"title": TITLE,
                              "tenant": request.tenant,
                               "form": form,
                               "own_committee": own_committee})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def requests(request):
    TITLE = "View Requests"
    if request.user.is_authenticated:
        if request.user.is_chair:

            #Get profile and committee
            profile = Chair.objects.get(user=request.user)
            own_committee = profile.committee
            #Get requests and order them chronologically
            past_requests = LogisticsRequest.objects.filter(
                committee=own_committee).order_by('-timestamp')

            return render(request,
                          "chair/requests.html",
                          {"title": TITLE,
                          "tenant": request.tenant,
                           "past_requests": past_requests,
                           "own_committee": own_committee})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def add_request(request):
    TITLE = "Add Request"
    if request.user.is_authenticated:
        if request.user.is_chair:

            if request.method == "POST":
                #Create request when form is submitted
                new_request = LogisticsRequest(
                    committee=Chair.objects.get(user=request.user).committee)
                #Fill in description field
                form = LogisticsRequestForm(request.POST, instance=new_request)

                if form.is_valid():
                    form.save()
                    messages.success(request, "You have submitted a request")
                return redirect("chair:requests")

            else:
                form = LogisticsRequestForm()
                return render(request,
                              "chair/add_request.html",
                              {"title": TITLE,
                              "tenant": request.tenant,
                               "form": form}
                              )

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def edit_request(request, request_key):
    TITLE = "Edit Request"
    if request.user.is_authenticated:
        if request.user.is_chair:

            #Get and edit request
            if request.method == "POST":
                logisticsrequest = LogisticsRequest.objects.get(pk=request_key)
                form = LogisticsRequestForm(
                    request.POST, instance=logisticsrequest)
                if form.is_valid():
                    updated_request = form.save()
                    messages.info(request, "Request updated")
                    return redirect('chair:requests')

            else:
                logisticsrequest = LogisticsRequest.objects.get(pk=request_key)
                form = LogisticsRequestForm(instance=logisticsrequest)
                return render(request,
                              "chair/edit_request.html",
                              {"title": TITLE,
                              "tenant": request.tenant,
                               "form": form})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def delete_request(request, request_key):
    if request.user.is_authenticated:
        if request.user.is_chair:

            #Delete request
            logisticsrequest = LogisticsRequest.objects.get(pk=request_key)
            logisticsrequest.delete()
            messages.info(request, "You have deleted the request")
            return redirect('chair:requests')

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def position_papers(request):
    TITLE = "Position Papers"
    if request.user.is_authenticated:
        if request.user.is_chair:

            profile = Chair.objects.get(user=request.user)
            own_committee = profile.committee

            #Filter all the papers linked to a delegate in users committee
            # get paper where paper_delegate__allocation_committee = own_committee
            papers = PositionPaper.objects.filter(
                delegate__allocation__committee=own_committee)
            return render(
                request,
                'chair/position_papers.html',
                {"title": TITLE,
                "tenant": request.tenant,
                 'papers': papers,
                 'own_committee': own_committee}
            )

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def download_paper(request, paper_key):
    if request.user.is_authenticated:
        if request.user.is_chair:

            profile = Chair.objects.get(user=request.user)
            own_committee = profile.committee
            paper = PositionPaper.objects.get(pk=paper_key)
            #Check if user is allowed to download paper
            if paper.delegate.allocation.committee == own_committee:
                #Get file path
                document = paper.document
                #Create response
                response = HttpResponse()
                response['Content-Type'] = ''
                #Input file path to attach file to the response
                response['Content-Disposition'] = "attachment; filename=" + \
                    str(document)
                messages.success(request, "Position paper downloaded")
                return response

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')
