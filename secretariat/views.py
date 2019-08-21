from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from .forms import ChairCreationForm, AllocationForm, CountryForm, CommitteeForm
from .models import ProgressSheet, LogisticsRequest
from delegation.models import Delegate, Allocation, Committee, Country
from .filters import RequestFilter, DelegateFilter, AllocationFilter

# Create your views here.
def index(request):
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
						  {"pages": pages})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def conference(request):
	if request.user.is_authenticated:
		if request.user.is_superuser:

			no_committee_selected = False
			committees = Committee.objects.all().order_by('name')
			allocations = Allocation.objects.all()
			allocation_filter = AllocationFilter(request.GET, queryset=allocations)
			print(request.GET)

			if request.GET['committee'] == '':
				no_committee_selected = True
				selected_committee = Committee.objects.none()
			else:
				selected_committee = Committee.objects.get(pk=request.GET['committee'])

			committee_form = CommitteeForm
			allocation_form = AllocationForm

			return render(request,
						  "secretariat/conference.html",
						  {"committees": committees,
						  "committee_form": committee_form,
						  "allocation_form": allocation_form,
						  "allocation_filter": allocation_filter,
						  "no_committee_selected": no_committee_selected,
						  "selected_committee": selected_committee})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def add_committee(request):
	if request.user.is_authenticated:
		if request.user.is_superuser:

			if request.method == 'POST':
				if request.POST['name']:
					form = CommitteeForm(request.POST)
					new_committee = form.save()
					messages.success(request, "New committee added")
					return redirect('secretariat:conference')

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def countries(request):
	if request.user.is_authenticated:
		if request.user.is_superuser:

			countries = Country.objects.all().order_by('name')

			if request.method == 'POST':
				form = CountryForm(request.POST)
				if form.is_valid():
					new_country = form.save()
					messages.success(request, "New country added")
					return redirect('secretariat:countries')

			form = CountryForm()
			return render(
				request,
				"secretariat/countries.html",
				{'form': form,
				'countries': countries}
			)


	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def allocations(request):
	if request.user.is_authenticated:
		if request.user.is_secretariat:

			delegates = Delegate.objects.all().order_by('-past_conferences')
			delegate_filter = DelegateFilter(request.GET, queryset=delegates)
			allocations = Allocation.objects.all()
			allocation_filter = AllocationFilter(request.GET, queryset=allocations)

			return render(request,
						  "secretariat/allocations.html",
						  {
						  'delegate_filter': delegate_filter,
						  'allocation_filter': allocation_filter,
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
			print(delegate)
			print(allocation)
			allocation.delegate = delegate
			allocation.save()
			response = {
			 'status': 1,
			}

		except Exception as e:
			response = {
			 'status': 0,
			}

		return JsonResponse(response)

	return redirect('secretariat:allocations')

def add_chair(request):
	if request.user.is_authenticated:
		if request.user.is_secretariat:

			if request.method == "POST":
				form = ChairCreationForm(request.POST)
				if form.is_valid():
					user = form.save()
					username = form.cleaned_data.get('username')
					messages.success(request, f"You have successfully created a chair account: {username}")

				else:
					for msg in form.error_messages:
						messages.error(request, f"{msg}: {form.error_messages[msg]}")

						return render(request = request,
								  template_name = "secretariat/add_chair.html",
								  context={"form":form})

			form = ChairCreationForm
			return render(request,
						  "secretariat/add_chair.html",
						  {"form": form}
			)

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def progress(request):
	if request.user.is_authenticated:
		if request.user.is_secretariat:

			sheets = ProgressSheet.objects.all()
			return render(request,
						  "secretariat/progress.html",
						  {"sheets": sheets})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def progress_sheet(request, slug):
	if request.user.is_authenticated:
		if request.user.is_secretariat:

			sheet = ProgressSheet.objects.get(committee__name=slug)
			other_sheets = ProgressSheet.objects.exclude(committee=sheet.committee)

			return render(request,
						  "secretariat/progress_sheet.html",
						  {"sheet": sheet,
						   "other_sheets": other_sheets})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def requests(request):
	if request.user.is_authenticated:
		if request.user.is_secretariat:

			request_list = LogisticsRequest.objects.all().order_by('-timestamp')
			request_filter = RequestFilter(request.GET, queryset=request_list)

			return render(request,
						  "secretariat/requests.html",
						  {'requests': request_list,
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
			else: messages.info(request, "Request marked as incomplete")

			return redirect('secretariat:requests')

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')
