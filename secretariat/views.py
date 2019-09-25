from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from .forms import ChairCreationForm, AllocationForm, CountryForm, CommitteeForm
from .models import ProgressSheet, LogisticsRequest
from delegation.models import Delegate, Allocation, Committee, Country
from .filters import RequestFilter, DelegateFilter, AllocationFilter

# Create your views here.


def index(request):
    TITLE = "Home"
    if request.user.is_authenticated:
        if request.user.is_secretariat:

            pages = {
                "Add Chair": "add_chair/",
                "Allocations": "allocations/",
                "Progress Sheets": "progress/",
                "Logistics Requests": "requests/",
            }

            return render(request,
                          "secretariat/index.html",
                          {"title": TITLE,
                          "pages": pages})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def allocations(request):
    TITLE = "Allocations"
    if request.user.is_authenticated:
        if request.user.is_secretariat:

            delegates = Delegate.objects.all().order_by('-past_conferences')
            delegate_filter = DelegateFilter(request.GET, queryset=delegates)
            allocations = Allocation.objects.all()
            allocation_filter = AllocationFilter(
                request.GET, queryset=allocations)
            no_committee_selected = True

            if request.GET and 'committee' in request.GET:
                if request.GET['committee']:
                    no_committee_selected = False

            return render(request,
                          "secretariat/allocations.html",
                          {
                              "title": TITLE,
                              'delegate_filter': delegate_filter,
                              'allocation_filter': allocation_filter,
                              'no_committee_selected': no_committee_selected,
                          }
                          )

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def add_allocation_delegate(request):

    if request.method == "POST":
        delegateID = request.POST['delegateID']
        allocationID = request.POST['allocationID']

        try:
            delegate = Delegate.objects.get(pk=delegateID)
            allocation = Allocation.objects.get(pk=allocationID)
            allocation.delegate = delegate
            allocation.save()
            response = {
                'status': 1,
            }
            messages.info(request, "Delegate allocated")

        except Exception as e:
            response = {
                'status': 0,
            }

        return JsonResponse(response)


def delete_allocation_delegate(request):

    if request.method == "POST":
        delegateID = request.POST['delegateID']

        try:
            allocation = Allocation.objects.get(delegate__pk=delegateID)
            allocation.delegate = None
            allocation.save()
            response = {
                'status': 1,
            }
            messages.info(request, "Delegate removed")

        except Exception as e:
            response = {
                'status': 0,
            }

        return JsonResponse(response)


def add_chair(request):
    TITLE = "Add Chair Account"
    if request.user.is_authenticated:
        if request.user.is_secretariat:

            if request.method == "POST":
                form = ChairCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(
                        request, f"You have successfully created a chair account: {username}")

                else:
                    for field in form:
                        for error in field.errors:
                            messages.error(request, error)

                    return render(request=request,
                                  template_name="secretariat/add_chair.html",
                                  context={"title": TITLE,
                                           "form": form})

            form = ChairCreationForm
            return render(request,
                          "secretariat/add_chair.html",
                          {"title": TITLE,
                           "form": form}
                          )

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def progress(request):
    TITLE = "Progress Sheets"
    if request.user.is_authenticated:
        if request.user.is_secretariat:

            sheets = ProgressSheet.objects.all()
            return render(request,
                          "secretariat/progress.html",
                          {"title": TITLE,
                           "sheets": sheets})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def progress_sheet(request, slug):
    TITLE = "Progress Sheet"
    if request.user.is_authenticated:
        if request.user.is_secretariat:

            sheet = ProgressSheet.objects.get(committee__name=slug)
            other_sheets = ProgressSheet.objects.exclude(
                committee=sheet.committee)

            return render(request,
                          "secretariat/progress_sheet.html",
                          {"title": TITLE,
                           "sheet": sheet,
                           "other_sheets": other_sheets})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def requests(request):
    TITLE = "Requests"
    if request.user.is_authenticated:
        if request.user.is_secretariat:

            request_list = LogisticsRequest.objects.all().order_by('-timestamp')
            request_filter = RequestFilter(request.GET, queryset=request_list)

            return render(request,
                          "secretariat/requests.html",
                          {"title": TITLE,
                           'requests': request_list,
                           'filter': request_filter})

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')


def change_status(request, request_key):
    if request.user.is_authenticated:
        if request.user.is_secretariat:

            logistics_request = LogisticsRequest.objects.get(pk=request_key)
            logistics_request.completed = not logistics_request.completed
            logistics_request.save()
            if logistics_request.completed:
                messages.info(request, "Request marked as completed")
            else:
                messages.info(request, "Request marked as incomplete")

            return redirect('secretariat:requests')

    messages.error(request, "You are not authorized to access that page")
    return redirect('users:index')
