from django.shortcuts import render, redirect

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
