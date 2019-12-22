"""
Admin area is one of the best feature of Djanogo specially for a freelancer or a small team where it is difficut to create a custom admin area. Django gives this feature right out of the box. Now
if we go to localhost/admin, it takes us to login page. Currently we don't have login credentials. To access the admin area we will first create a superuser by running "python manage.py createsuperuser".
It will ask for 3 fields including username, Email address and Password which we will provide it here. After doing that we will use this information to access the admin area and we will get logged in.
When we are inside the admin area we have two option by default which are to Add or Change groups and users. However we also want to be able to add listings and realtors from the admin area. For this
first we will open admin.py file of our app folder. This is where we can customize admin stuff for our app. Specifically in this case we want to register our models here that we want to get accessed
from the admin area.

Now first we will need to import the model that we want to register. And once our model is imported we will register it using command "admin.site.register(Model Name)". After a model is registered it
can be then accessed from admin area and we can create a model instance (eg a Listing or a Realtor) and that information will be saved. But before we do that we will setup our media folder where all of
the photos will be saved. The setup is similar to what we did for static files setup in settings.py file i-e we will set MEDIA_ROOT and MEDIA_URL. But along with that we will also go to main urls.py
file (within btre folder) and at the end of urlpatterns list we will add " + static(settings.MEDIA.URL, document_root = settings.MEDIA_ROOT) ". In order to get this previous line of code work we will
have to import static and settings into main urls.py file because without this it will not understand what is static and settings in above line of code.

After doing all of above we will add all of the data from the admin area. Once we have added the data from admin the "media" folder will be created automatically. This is because we have set this up
in the settings.py file.

CUSTOMIZING ADMIN PAGE:

Now that we have added the data and are able to see our data from the admin area we will customize it. For this we will create a folder named "admin" within our template folder and inside this folder
we will make an html file "base_site.html" and it is important to give it this name. Inside this html we will first extend 'admin/base.html' and load our static files. We will make a branding block.

1) First we will change the title of admin page and use our brand log there. For this inside the block we will make a h1 heading and will use img inside this h1. For this we will give the a static
   src using {%  %} symbols, give it a height and also we will give this a class of "brand_img". By doing just this we will see that our title of admin page has been set as our brand logo.

2) If we want to use css for our admin page we will add another block called extrastyle. And inside that block we will use a link element to link with an css file. Once we do that we will make that
   css file. We will style our admin pages and for this we will have to select the elements using classes or ids. For viewing what class names and id names have been used we can look at chrome developer
   tools.
"""


from django.contrib import admin

# Register your models here.
from .models import Listing         #The Listing is the name that we gave to our model. The .models means models.py in current directory.

admin.site.register(Listing)