"""

WEB DEVELOPMENT USING DJANGO:

   Now django has the idea of the project which is our website as a whole and inside that project we have something called 'apps'. So for example if we have a blog in our website then that blog will be
   an individual app that has its own model, views, urls files. Similarly if we have a store in our website then that store will be another app with its own files as well. So each piece of functionality
   is what we called an app. Even for static pages we will have a 'pages' app to handle static pages.

STARTING A NEW PROJECT IN DJANGO:

   We will start our project by running the command "django-admin startproject btre" using our terminal from our project directory. It will create a 'btre' directory and inside it, it will create 3
   python files "setting.py", "urls.py" and "wsgi.py". It will also create "manage.py" file outside this btre directory and inside "btre_project" directory and once we have started our project we
   won't use 'django-admin' any more and we will only use "manage.py" file for everything.

WE WANT TO CREATE PAGES APP WHICH CONTAINS A HOME PAGE AND ABOUT PAGE:

   We will start our pages app by running the command "python manage.py startapp pages" from our terminal. It will create a pages directory and inside it, it will also create admin.py, app.py,
   models.py, tests.py and views.py. We will also create another file called "urls.py" inside pages directory to handle http requests from the users of our website.

   REQUEST WORKFLOW:

   Now when a user sends a request to a specific url on our server our app will first go to the 'urls.py' file in the 'btre' directory. In that file we have 'urlpatterns' which is an array and each
   element of that array is a path. So in this 'urlpatterns' it will look for the route which was requested by the user. So in the 'urlpatterns' we will have to create a url for all of our endpoints
   and we do that using 'path' module which we will need to import (although for 'urls.py' within the btre directory it is already imported because it has already configured the admin page.). This 
   'path' will give us the 'path()' function which takes in url/route address as the first parameter and then the second parameter that we need to pass is to which app's 'url.py' file we need to send
   this user. And the way we do that is we use the 'include()' method which like 'path' is also imported from the 'django.urls'. And in the parenthesis of this 'include()' method we will pass 'pages.url'
   provided that the name of our app to which this route belongs to is 'pages'. Then again it will look in the 'urlpatterns' list within that that app and in it it will look for that specific route which
   was requested by the user. So again we need to define that path in the 'urlpatterns' list of the 'urls.py' file of that app to which this url belongs to. For this we will use the 'path()' method again
   and pass the 'route' as the first parameter and then 'views.index' as the second parameter. Now all of the methods to handle the request are defined in the 'views' folder of the app and 'index' is just
   a placeholder which we are using to point to the name of the method which will actually handle this request. So next we will go to the 'views.py' file and there we will define this 'index' method.
   Now each of these method will get access to 'request' and it will take this request as 'input'. Then we may want to manipulate with the request or just send the 'template' which correponds to this
   url route. Now if we want to send simple html elements like 'h1' or 'p' we will use 'HttpResponse' method which we need to import from 'django.http'. On the other hand if we want to send the template
   we will use 'render()' method and this render method will take 'request' as the first parameter and then the path and name of the template which we want to send as the second parameter and in this way
   we will have access to the 'request' object in our html template as well and we can make the templates dynamic. Now we will also pass a third argument 'name' and this corresponds to the 'url' of the 
   request and in this way we will get access to the url within our html templates to make our template dynamic.

   When a user goes to localhost:8000, then it first looks in our main urls.py file inside the 'btre' directory and looks for the empty pattern there relating to our home page (urlpatterns list).
   If the pattern for that address exists, then it asks where to send the user. This will be the second input (i.e (include('pages.urls'))) of the path function inside urlpatterns list, which will send
   our user to pages.urls, which is actually urls.py file inside pages app directory. Because the first argument within our path in main urls.py file is empty string, it will search for urlpattern
   within urlpatterns list of our urls.py file within pages directory, for the pattern with empty strings. Now in order to create a path/route/url we need to import the 'path' package from 'django.url
   because we use 'path' function to define the 'routes'. Because we have defined the pattern for our empty string i-e for our home route, and inside that pattern we have also specified to send the user 
   to views.index. However for this we will need to import the 'views' of the 'pages' app in the 'urls' page. So now we will send our user to views.py file and to look for the function named index. In 
   this function we will use HttpResponse to send plain html elements or we can simply send our html template we made for our home route. However if we want to send/render templates we also must do two 
   things. 1 is to add our app within the INSTALLED_APPS list inside settings.py. Second is to define our path where we are saving our templates within 'TEMPLATES' list also inside settings.py. Note that by
   default python will look for templates in the templates folder inside the current app folder, but if we want to change the default, we must define that in the TEMPLATES list inside settings.py file.
   In our case instead of making templates folder within every app, we will make a single templates folder inside our project directory i-e BTRE_PROJECT and then for every app we will make sub
   directories and we will make our templates relating to different apps in there relevent directories.
   
MAKING AND USING BASE HTML FILE:

   Now we want to apply the same styling for every pages but we will also avoid repeating head section, footer section and styling on every page. For this we will make a base.html inside templates
   directory (but outside pages directory which contains our index.html and about.html). This base.html will contain the styling, such as header, navbar and footer, for our whole website apps. For
   the content area we will create a 'block' in the 'base.html' file. Now if we want to inject any other html file into this 'base.html' we will write '{% extends 'base.html %} and then in the next
   line we will write {% block content %}. Then all of the code below the 'block content' of this file will be injected into this 'base.html'. The curly brackets and % signs are the jinja syntax.

HOW TO USE STATIC FILES IN OUR PROJECT:

   Although normally we will want to use CDNs for bootstrap, jquery and fontsawesome etc but brad traversy wanted to keep everything local so that we don't have to change the code if anything updates.
   Now we have our bootstrap, javascript, images and fontsawesome files and we want to bring into our website as static assets. Inside our main btre folder, which was created when we created the btre
   project using django-admin, we will make another folder "static". Inside that we will copy our css, js and webfonts folders. We will also make another folder "img" and copy our main image files and
   lightbox folder inside it. So in short we have to make static directory inside btre project directory and bring everything in it. After making our static files we also need to tell our app where these
   static files are present and for that we have to specify the path of these static files in the bottom of our settings.py file. At the moment we have a variable called 'STATIC_URL' which is set to 
   '/static/' but now we want to set two new variables. 1st is the 'STATIC_ROOT' and the idea is that when we deploy our app we call a method 'collectstatic' and it goes in all of our 'apps' and if any
   of the app has the 'static' folder it takes everything out and puts it into root static folder and that is what we will define here for 'STATIC_ROOT' variable and set it to 'os.path.join(BASE_DIR, 'static').
   Next we will also define a variable 'STATICFILES_DIRS' which will be an array and this array takes in elements for all of the 'static' directories paths. Now for our app we have all of the static
   resources in our directory 'static' withing the 'btre' directory so we will set it to 'os.path.join(BASE_DIR, 'btre/static').

   Now whenever we need to use any of these static files in our html files we will write {% load static %} at the top of each html page. And in the href or src we would have to write something like the
   href="{% static 'css/all.css' %} if we want to load "all.css" file.

   Now when our app is ready and we want to deploy our app on a server we will use "manage.py collectstatic" method to collect these files. When we will do this we will see that it will create a
   static directory in the root directory which is our main BTRE_PROJECT. This static folder will not only contain all the stuff that we put in the static folder that we made in our btre directory but
   also the admin folder. So when we will deploy, this is where it will look for all the css and js files. For now we don't want these static files to get commited so we will add it in our .gitignore
   file.

USING PARTIALS:

   Now we will add stuff from our html files, which were given to us by front end department, to our templates. First we can copy our header and footer section out of index.html into our base.html so
   that header and footer section is applied on all the pages of our app. However we also don't want our base.html to be cluttered up with so many lines of code. So what we will do is we will create
   another folder in our templates folder called "partials". And we will copy our top section, navbar and footer section into the seperate files and because these are partials the convention is to use
   underscore in filenames. And then when we want to include these partial files into our base.html we will use syntax {% include 'partials/_topbar.html' %}. This is analogous to in EJS where we used
   <%- include('header'); -%> syntax of EJS.

ADDING REMAINING HTML TO OUR RELEVENT SECTIONS IN OUR HTML PAGES:

   Now we will copy everything other than topbar, navbar and footbar from our index.html and paste it inside our index.html and also do the same for about.html. We will get our theme and also a few
   errors if we have chrome developer tools opened. These error are relating to listings and realtors images which needs to be entered from admin area which we haven't yet gone through. So the images
   will come from somewhere else and not from static files we have. However apart from this there is a static image for the about page which we need to load correctly. For this we will need to import
   static files into our about.html and we will do this by writing {% load static %} at the top. And then we will give the correct address of the image in src attribute of image. However for this
   we will use special syntax : "{% static 'img/about.jpg' %}". So we have told our app that we have all of our static files in the 'static' folder in the 'btre' directory. Then because we have our
   'about.jpg' file withing the 'img' directory in the 'static' folder we will specify it like 'img/about.jpg' like we did above. 

LINKING BUTTONS WITH CORRECT PAGES:

   At the moment our buttons on the navbar and breadcrumbs link on the 'about' page are not working. For this we need to use the correct address inside the href attributes of our anchor links. However 
   instead of using static addresses we want to use dynamic addresses. Specifically we want that href attributes in our navbar automatically picks the url from the urls.py file. For this we will use the 
   {% url 'name' %} in the href attribute, where the name will be replaced by whatever name we gave to that url in our urls.py file. In this way our links will be dynamic and if we wanted to change the 
   url address for any page, we will just have to do that in our urls.py file and not on our buttons href.

HIGHLIGHTING OF THE LINKS IN OUR NAVBAR:

   Even if we go to our about page, still HOME remains highlighted in our navbar. This is because in our navbar we have given a bootstrap class of "active" to our Home list-item. If we move the active
   from home to about then about will remain active no matter on which page we are currently on. But we want this to be dynamic. For this we will use if-else conditionals inside our _navbar.html. Now if
   want to use python code (if-else, loops etc) with in our html templates, each line of code must be within {%   %} symbols. Also we must specify where our python code ends by writing {% endif %} for
   if-else and {% endfor %} for ending for loop etc. Now we will have to use if conditional for each of the 'li' class. So for 'Home' li we will say if '/' is equal to 'request.path' then set the value
   of class to 'nav-item active mr-3'. Else if the requested path is not '/' then set the class to 'nav-item mr-3'. And we will do the same for each of the li link item in our navbar.

MORE APPS:

   Now when we are building an application we should complete our frontend and complete our templates before moving into functionality and databases. Therefore now we will create listings and realtors app. 
   In our terminal, from our project directory, we will write "python manage.py startapp listings" and do same for the "realtors" app.


MAKING OUR HOME PAGE DYNAMIC:

   At the moment our home page listings are just static markup and now we want to make the listings dynamic. We also want to make our about page dynamic to show the realtors images and realtor of the
   month. Now on home page we want to show the latest listings. Although we are rendering our home page ("index.html") from pages app, we can import models from other apps as well. So first we will
   import the Listing model from the listings app. Like in the listings app we will use django methods to import our listings. If we wanted to import all of the listings from our database without any
   condition, we can simply do that by writing "listings = Listing.objects.all()" and then use that "listings" variable to make a dictionary and finally pass that dictionary to the render method for our
   home page as a 3rd parameter. However we want to order our listings by date, we want to show only the published listings and finally for home page we only want it to show 3 listings. All of this can
   be achieved by a single line of code i-e "Listing.objects.order_by('-list_date').filter(is_published = True)[:3]. Once we do that we will be able to receive the listings from our "index.html" and we
   will simply loop through these and make our home page dynamic and linked with database just like we did in listings app.

MAKING OUR ABOUT PAGE DYNAMIC:

   In the next step we want our about page to be dynamic. We want the realtors and seller of the month section to be dynamic. For this we will import the Realtor model from realtors app. After we do that
   we want two things from that. One is the realtors and we will simply get them by using Realtor.objects.order_by (because we want to shows them in order of hire date). 2nd is to show one or more realtors
   who have been mvp for the month. For this we will use Realtor.objects.all method and then at the end we will apply the filter to return only those realtors who have mvp option checked. Once we do that
   we will pass both of the obove objects into our context dictionary and pass that dictionary in our render function as a 3rd arguement. This will give access to both of these objects from our about.html
   page.

MAKING SINGLE LISTING PAGE:
   Refer to views.py file of our listings app.


ACCOUNTS AND AUTHENTICATION:

   Refer to views.py file of accounts app.

CONTACT INQUIRIES:

   Refer to views.py file of contacts app.

DASHBOARD FUNCTIONALITY:

   Refer to views.py file of accounts app.

  

"""

from django.shortcuts import render
#from django.http import HttpResponse                           #HttpResponse is a function that does similar job as res.send() function does in express.
from listings.models import Listing
from listings.choices import state_choices, bedroom_choices, price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
      'listings': listings,
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices
    }
    return render(request, "pages/index.html", context)        #However we don't want to render html elements instead we will send our template from here. This is analogous to res.sendFile() in express.
                                                                
def about(request):
    from realtors.models import Realtor
    
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
       'realtors': realtors,
       'mvp_realtors' : mvp_realtors
    }
    return render(request, "pages/about.html", context)
