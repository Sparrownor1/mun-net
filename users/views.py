from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import DelegationSignUpForm, NewUserChangeForm

# Create your views here.
def home(request):

    TITLE = "MUN-Net"
    TENANT = request.tenant

    return render(
        request,
        "users/index.html",
        {"title":TITLE,
         "tenant": request.tenant}
    )

def register(request):

    TITLE = "Register"

    if request.method == "POST":
        form = DelegationSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"You have successfully created a delegation account as: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as: {username}")
            return redirect("delegation:edit_delegation")
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)

            return render(request=request,
                          template_name="users/register.html",
                          context={"form": form,
                                   "title": TITLE,
                                   "tenant": request.tenant})

    form = DelegationSignUpForm
    return render(request,
                  "users/register.html",
                  {"form": form,
                   "title": TITLE,
                   "tenant": request.tenant}
                  )


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("users:index")
            else:
                messages.error(request, "Invalid username or password")

        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm
    return render(request=request,
                  template_name="users/login.html",
                  context={"form": form,
                           "tenant": request.tenant}
                  )


def logout_request(request):

    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect("users:index")


def account(request):

    TITLE = "My Account"

    if request.method == "POST":
        form = NewUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, "Account data saved")
            return redirect("users:index")
    else:
        form = NewUserChangeForm(instance=request.user)
        return render(request,
                      "users/account.html",
                      {"title": TITLE,
                      "form": form,
                      "tenant": request.tenant})


def index(request):

    if request.user.is_authenticated:
        if request.user.is_secretariat:
            return redirect("secretariat:index")
        if request.user.is_chair:
            return redirect('chair:index')
        if request.user.is_delegation:
            return redirect("delegation:index")

    return redirect('users:home')
