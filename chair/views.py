from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from delegation.models import Committee
from secretariat.models import LogisticsRequest, Chair
from secretariat.forms import LogisticsRequestForm

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		if request.user.is_chair:

			pages = {
				"Logistics Requests": "requests/",
			}
			return render(request,
						  "chair/index.html",
						  {"pages": pages})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def requests(request):
	if request.user.is_authenticated:
		if request.user.is_chair:

			profile = Chair.objects.get(user=request.user)
			own_committee = profile.committee
			past_requests = LogisticsRequest.objects.filter(committee=own_committee).order_by('-timestamp')

			return render(request,
						  "chair/requests.html",
						  {"past_requests": past_requests,
						   "own_committee": own_committee})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def add_request(request):
	if request.user.is_authenticated:
		if request.user.is_chair:

			if request.method == "POST":
				new_request = LogisticsRequest(committee=Chair.objects.get(user=request.user).committee, timestamp=datetime.now())
				form = LogisticsRequestForm(request.POST, instance=new_request)

				if form.is_valid():
					form.save()
					messages.success(request, "You have submitted a request")
				return redirect("chair:requests")

			else:
				form = LogisticsRequestForm()
				return render(request,
							  "chair/add_request.html",
							  {"form": form}
				)

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def edit_request(request, request_key):
	if request.user.is_authenticated:
		if request.user.is_chair:

			if request.method == "POST":
				logisticsrequest = LogisticsRequest.objects.get(pk=request_key)
				form = LogisticsRequestForm(request.POST, instance=logisticsrequest)
				if form.is_valid():
					updated_request = form.save()
					messages.info(request, "Request updated")
					return redirect('chair:requests')

			else:
				logisticsrequest = LogisticsRequest.objects.get(pk=request_key)
				form = LogisticsRequestForm(instance=logisticsrequest)
				return render(request,
							  "chair/edit_request.html",
							  {"form": form})

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
