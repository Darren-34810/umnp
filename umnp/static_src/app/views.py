from django.shortcuts import render

from umnp.static_src.app.models import webPage
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')


def portofolio(request):
    webPages1 = webPage.objects.all()[0:2]
    webPages2 = webPage.objects.all()[2:4]
    return render(request, 'portofolio.html', {'webPages1': webPages1,'webPages2': webPages2})

def contact(request):
    return render(request, 'contact.html')

def portofolio_details(request,projectname):
    webpages = get_object_or_404(webPage,judul = projectname)

    return render(
        request,
        'portofolio_detail.html', {'webpages':webpages}
    )

def career(request):
    return render(request, 'career.html')

def handle_not_found(request, exception):
    return render(request, 'not_found.html')