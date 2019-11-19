from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    TITLE = 'MUN-Net Home'
    return render(
        request,
        'tenants/index.html',
        {'title':TITLE}
    )
