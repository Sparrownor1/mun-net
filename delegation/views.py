from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import Delegate, Allocation, PositionPaper
from users.models import Delegation
from .forms import DelegateForm, DelegationForm, PositionPaperForm

# Create your views here.
def index(request):
	TITLE = "Home"
	#Authenticate and authorize user
	current_user = request.user
	if current_user.is_authenticated:
		if current_user.is_delegation:

			#Get delegates from users delegation
			user_del = Delegation.objects.get(user=current_user)
			delegates_in_delegation = Delegate.objects.filter(delegation=user_del)
			no_delegates = len(delegates_in_delegation) == 0
			#Get allocations from delegates
			allocations = Allocation.objects.filter(delegate__delegation=user_del)

			#Check if user has more delegates in delegation than is specified
			if len(delegates_in_delegation) > user_del.size:
				messages.error(request, "You have more delegates than your delegation size states, please change it")
				return redirect('delegation:edit_delegation')

			return render(request,
						  "delegation/index.html",
						  {"title": TITLE,
						   "delegates": delegates_in_delegation,
						   "no_delegates": no_delegates,
						   "allocations": allocations}
						   )

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def add_delegate(request):
	TITLE = "Add Delegate"
	#Check if user is authorized to access page
	if request.user.is_authenticated:
		if request.user.is_delegation:

			#Get delegates in delegation
			user_del = Delegation.objects.get(user=request.user)
			delegates_in_delegation = Delegate.objects.filter(delegation=user_del)

			if len(delegates_in_delegation) < user_del.size:
				#When form is posted, create a delegate in delegation
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
								  {"title": TITLE,
								   "form": form}
					)
			else:
				messages.error(request, "Please change your delegation size before you add another delegate")
				return redirect('delegation:edit_delegation')

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def edit_delegate(request, delegate_key):
	TITLE = "Edit Delegate"
	#Check if user is authorized to access page
	if request.user.is_authenticated:
		if request.user.is_delegation:

			if request.method == "POST":
				#Get delegate user wants to edit
				delegate = Delegate.objects.get(pk=delegate_key)
				#Fill in current details to form
				form = DelegateForm(request.POST, instance=delegate)
				if form.is_valid():
					updated_delegate = form.save()
					messages.info(request, "You have saved a delegate's information")
					return redirect("delegation:index")

			else:
				#Get delegate user wants to edit
				delegate = Delegate.objects.get(pk=delegate_key)

				#Check if delegate is in users delegation
				if delegate.delegation != Delegation.objects.get(user=request.user):
					messages.error(request, 'You cannot do that')
					return redirect('users:index')

				#Fill in current details to form
				form = DelegateForm(instance=delegate)
				return render(request,
							  "delegation/edit_delegate.html",
							  {"title": TITLE,
							   "form": form})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')

def delete_delegate(request, delegate_key):
	if request.user.is_authenticated:
		if request.user.is_delegation:

			delegate = Delegate.objects.get(pk=delegate_key)

			#Check if delegate is in users delegation
			if delegate.delegation != Delegation.objects.get(user=request.user):
				messages.error(request, 'You cannot do that')
				return redirect('users:index')

			#Delete
			delegate.delete()
			messages.info(request, "You have deleted a delegate")
			return redirect("delegation:index")

	messages.error(request, "You are not authorized to do that")
	return redirect('users:index')

def upload_position_paper(request, delegate_key):
	if request.user.is_authenticated:
		if request.user.is_delegation:

			delegate = Delegate.objects.get(pk=delegate_key)
			#Check if delegate is in delegation
			if delegate.delegation != Delegation.objects.get(user=request.user):
				messages.error(request, 'You cannot do that')
				return redirect('users:index')

			try:
				Allocation.objects.get(delegate=delegate)

				try:
					current_paper = PositionPaper.objects.get(delegate=delegate)
				except ObjectDoesNotExist:
					current_paper = None

				if request.method == 'POST':
					#If delegate has position paper
					if current_paper:
						#Display uploaded file
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
						#Create position paper for delegate
						paper = PositionPaper(delegate=delegate)
						#Create form for position paper
						form = PositionPaperForm(request.POST, request.FILES, instance=paper)
						if form.is_valid():
							try:
								form.save()
							#If database throws error
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
				#Save delegation details
				form = DelegationForm(request.POST, instance=user_del)
				if form.is_valid():
					#check for amount of delegates in delegation against inputted size
					delegates_in_delegation = Delegate.objects.filter(delegation=user_del)
					delegation_size = form.cleaned_data['size']
					if len(delegates_in_delegation) <= delegation_size:
						#If there are less or as many delegates than specified, save data
						updated_delegation = form.save()
						messages.info(request, "Delegation information saved")
						return redirect("delegation:index")
					else:
						#Else throw error
						messages.error(request, "You have more delegates than your delegation size states, please change it")
						return redirect('delegation:edit_delegation')
			#Show delegation details
			else:
				form = DelegationForm(instance=user_del)
				return render(request,
							  "delegation/edit_delegation.html",
							  {"form": form})

	messages.error(request, "You are not authorized to access that page")
	return redirect('users:index')
