from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ChairCreationForm
from .models import ProgressSheet, LogisticsRequest
from delegation.models import Delegate, Allocation, Committee, Country
from .filters import RequestFilter

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

def allocations(request):
	if request.user.is_authenticated:
		if request.user.is_secretariat:

			pass

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

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
