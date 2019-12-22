"""btre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.c om/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),                 #Because this is gonna be home page we will leave first argument empty. Using "include('pages.urls')" we are basically saying that if anyone
                                                     #makes request for the home route ("i-e localhost: 8000), we will send him to the "urls.py" file within pages app.

    path('listings/', include('listings.urls')),     #We are saying that if anybody asks for "localhost://listings/" we are gonna send them to "url.py" file within listings.

    path('accounts/', include('accounts.urls')),

    path('contacts/', include('contacts.urls')),
    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
