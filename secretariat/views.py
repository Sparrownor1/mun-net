from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ChairCreationForm
from .models import ProgressSheet

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		if request.user.is_secretariat:

			pages = {
				"Progress Sheets": "progress/",
				"Logistics Requests": "requests/",
				"Add Chair": "add_chair/",
			}
			return render(request,
						  "secretariat/index.html",
						  {"pages": pages})

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
