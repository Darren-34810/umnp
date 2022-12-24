from django.shortcuts import render

from umnp.static_src.app.models import webPage

# Create your views here.

def index(request):
    return render(request, 'index.html')

def portofolio(request):
    webPages = webPage.objects.all()
    
    return render(request, 'portofolio.html', {'webPages': webPages})
    

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