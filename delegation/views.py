from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import Delegate, Allocation, PositionPaper
from users.models import Delegation
from .forms import DelegateForm, DelegationForm, PositionPaperForm

# Create your views here.
def index(request):
	current_user = request.user
	if current_user.is_authenticated:
		if current_user.is_delegation:

			user_del = Delegation.objects.get(user=current_user)
			delegates_in_delegation = Delegate.objects.filter(delegation=user_del)
			allocations = Allocation.objects.filter(delegate__delegation=user_del)

			if len(delegates_in_delegation) > user_del.size:
				messages.error(request, "You have more delegates than your delegation size states, please change it")
				return redirect('delegation:edit_delegation')

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

			user_del = Delegation.objects.get(user=request.user)
			delegates_in_delegation = Delegate.objects.filter(delegation=user_del)

			if len(delegates_in_delegation) < user_del.size:

				if request.method == "POST":
					newDel = Delegate(delegation = Delegation.objects.get(user=request.user),)
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
			else:
				messages.error(request, "Please change your delegation size before you add another delegate")
				return redirect('delegation:edit_delegation')

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

def upload_position_paper(request, delegate_key):
	if request.user.is_authenticated:
		if request.user.is_delegation:

			delegate = Delegate.objects.get(pk=delegate_key)

			try:
				Allocation.objects.get(delegate=delegate)

				try:
					current_paper = PositionPaper.objects.get(delegate=delegate)
				except ObjectDoesNotExist:
					current_paper = None

				if request.method == 'POST':
					if current_paper:
						form = PositionPaperForm(request.POST, request.FILES, instance=current_paper)
						if form.is_valid():
							try:
								form.save()
							except IntegrityError as e:
								messages.error(request, "This delegate already has uploaded a position paper")
								return redirect('delegation:index')
							messages.info(request, f"Position Paper uploaded for delegate {delegate.first_name} {delegate.last_name}")
							return redirect('delegation:index')

					else:
						paper = PositionPaper(delegate=delegate)
						form = PositionPaperForm(request.POST, request.FILES, instance=paper)
						if form.is_valid():
							try:
								form.save()
							except IntegrityError as e:
								messages.error(request, "This delegate already has uploaded a position paper")
								return redirect('delegation:index')
							messages.info(request, f"Position Paper uploaded for delegate {delegate.first_name} {delegate.last_name}")
							return redirect('delegation:index')

				else:
					delegate = Delegate.objects.get(pk=delegate_key)
					try:
						current_paper = PositionPaper.objects.get(delegate=delegate)
						form = PositionPaperForm(instance=current_paper)
					except ObjectDoesNotExist:
						form = PositionPaperForm()

				return render(request,
							  "delegation/upload_position_paper.html",
							  {'form': form,
							   'delegate': delegate,
							   'current_paper': current_paper,
							   })

			except ObjectDoesNotExist:
			   messages.error(request, "Sorry, you are not allowed to upload a position paper until a delegate has been allocated a country and committee")
			   return redirect('delegation:index')

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
