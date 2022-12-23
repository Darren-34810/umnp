from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def portofolio(request):
    return render(request, 'portofolio.html')

def contact(request):
    return render(request, 'contact.html')

def portofolio_details(request,projectname):
    return render(
        request,
        'portofolio_detail.html',
        {'projectname': projectname}
    )

def career(request):
    return render(request, 'career.html')