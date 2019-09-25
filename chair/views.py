from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.utils.encoding import smart_str
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
                           "pages": pages})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def sheet(request):
    TITLE = "Progress Sheet"
    if request.user.is_authenticated:
        if request.user.is_chair:

            profile = Chair.objects.get(user=request.user)
            own_committee = profile.committee
            sheet = ProgressSheet.objects.get(committee=own_committee)

            if request.method == "POST":
                sheet = ProgressSheet.objects.get(committee=own_committee)
                form = ProgressSheetForm(request.POST, instance=sheet)
                if form.is_valid():
                    updated_sheet = form.save()
                    messages.info(request, "Sheet updated")
                    return redirect('chair:sheet')

            else:
                sheet = ProgressSheet.objects.get(committee=own_committee)
                form = ProgressSheetForm(instance=sheet)
                return render(request,
                              "chair/sheet.html",
                              {"title": TITLE,
                               "form": form,
                               "own_committee": own_committee})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def requests(request):
    TITLE = "View Requests"
    if request.user.is_authenticated:
        if request.user.is_chair:

            profile = Chair.objects.get(user=request.user)
            own_committee = profile.committee
            past_requests = LogisticsRequest.objects.filter(
                committee=own_committee).order_by('-timestamp')

            return render(request,
                          "chair/requests.html",
                          {"title": TITLE,
                           "past_requests": past_requests,
                           "own_committee": own_committee})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def add_request(request):
    TITLE = "Add Request"
    if request.user.is_authenticated:
        if request.user.is_chair:

            if request.method == "POST":
                new_request = LogisticsRequest(
                    committee=Chair.objects.get(user=request.user).committee)
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
                               "form": form}
                              )

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def edit_request(request, request_key):
    TITLE = "Edit Request"
    if request.user.is_authenticated:
        if request.user.is_chair:

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
                               "form": form})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def delete_request(request, request_key):
    if request.user.is_authenticated:
        if request.user.is_chair:

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

            # get paper where paper_delegate__allocation_committee = own_committee
            papers = PositionPaper.objects.filter(
                delegate__allocation__committee=own_committee)
            return render(
                request,
                'chair/position_papers.html',
                {"title": TITLE,
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
            if paper.delegate.allocation.committee == own_committee:
                document = paper.document
                response = HttpResponse()
                response['Content-Type'] = ''
                response['Content-Disposition'] = "attachment; filename=" + \
                    str(document)
                messages.success(request, "Position paper downloaded")
                return response

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')
