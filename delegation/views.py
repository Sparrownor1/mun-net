from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Delegate, CountryCommitteeAllocation
from users.models import Delegation
from .forms import DelegateForm, DelegationForm

# Create your views here.
def index(request):
	current_user = request.user
	if current_user.is_authenticated:
		if current_user.is_delegation:
			user_del = Delegation.objects.get(user=current_user)
			delegates_in_delegation = Delegate.objects.filter(delegate_delegation=user_del)
			allocations = CountryCommitteeAllocation.objects.filter(allocated_delegate__delegate_delegation=user_del)

			return render(request,
						  "delegation/index.html",
						  {"delegates": delegates_in_delegation,
						   "allocations": allocations}
						   )

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def add_delegate(request):
	if request.user.is_authenticated:
		if request.user.is_delegation:

			if request.method == "POST":
				newDel = Delegate(delegate_delegation = Delegation.objects.get(user=request.user),)
				form = DelegateForm(request.POST, instance=newDel)

				if form.is_valid():
					form.save()
					messages.success(request, "You have added a new delegate")
				return redirect("delegation:index")

			else:
				form = DelegateForm()
				return render(request,
							  "delegation/add_delegate.html",
							  {"form": form}
				)

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def edit_delegate(request, delegate_key):
	if request.user.is_authenticated:
		if request.user.is_delegation:

			if request.method == "POST":
				delegate = Delegate.objects.get(pk=delegate_key)
				form = DelegateForm(request.POST, instance=delegate)
				if form.is_valid():
					updated_delegate = form.save()
					messages.info(request, "You have saved a delegate's information")
					return redirect("delegation:index")

			else:
				delegate = Delegate.objects.get(pk=delegate_key)
				form = DelegateForm(instance=delegate)
				return render(request,
							  "delegation/edit_delegate.html",
							  {"form": form})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def delete_delegate(request, delegate_key):
	if request.user.is_authenticated:
		if request.user.is_delegation:

			delegate = Delegate.objects.get(pk=delegate_key)
			delegate.delete()
			messages.info(request, "You have deleted a delegate")
			return redirect("delegation:index")

	messages.error(request, "You are not authorized to do that")
	return redirect('users:index')

def edit_delegation(request):

	current_user = request.user
	if current_user.is_authenticated:
		if current_user.is_delegation:
			user_del = Delegation.objects.get(user=current_user)

			if request.method == "POST":
				form = DelegationForm(request.POST, instance=user_del)
				if form.is_valid():
					updated_delegation = form.save()
					messages.info(request, "Delegation information saved")
					return redirect("delegation:index")

			else:
				form = DelegationForm(instance=user_del)
				return render(request,
							  "delegation/edit_delegation.html",
							  {"form": form})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')
