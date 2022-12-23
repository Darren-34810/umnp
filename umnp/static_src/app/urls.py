from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('works', views.portofolio, name='portofolio'),
    path('works/<projectname>', views.portofolio_details, name='portofolio_detail'),
    path('career', views.career, name='career'),
    path('contact', views.contact, name='contact'),
]
