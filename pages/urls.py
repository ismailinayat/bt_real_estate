from django.urls import path

from . import views                          # Because below we are using the functions from views.py file which is in the same folder, we will need to import that file in here. "." means to  look
                                             # in current directory.

urlpatterns = [
    path('', views.index, name = 'index'),    #This will not work initially because views file has no method index. So we will go to views.py file and make a function called "index". 

    path('about/', views.about, name = 'about'),
]