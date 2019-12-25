"""

LISTINGS:

    In our terminal, from our project directory, we will write "python manage.py startapp listings".

    Our listings app will contain 3 pages including "listings" which will contain all the listings, "listing" which will contain single listing and "search" page. So we will create templates for these
    pages. In our templates folder we will make another folder listings and inside that we will make 3 html files for each of our page.

    Similar to pages app we will copy our html code that we got from our front end department to the relevent templates that we created. Also we need to create "urls.py" for the listings app inside
    listings directory. In this 'urls.py' file we will again create the routes relating to our 'listings' app and for that we will first import 'path' and the 'views' module. Next we will create the
    routes in the 'urlpatterns' list. For 'listings' we will create 'path('', views.index, name = 'listings'). Now the route for the single 'listing' page should be such that after the '/listings/'
    it should have the 'listing id' of that listing. So we want to set 'listing_id' as a url parameter and in django we do that by writing '<int:listing_id>'. And then we will also set the route for
    the 'search' as well. Now the reason that we are not writing the complete paths is that we are actually gonna create the 'listings/' route in our main 'urls.py' file and whenever a request will 
    have the route like 'listings/' it will be sent to this listings app urls.py file and therefore here in this listings app 'urls.py' file we only need to define the route for the remaining url.

    Next we will create the method for each of these routes. Also remember to include the app in the settings.py file as well. 

SETTING UP DATABASE:

    Now that we have setup our front end of our web application we will move towards setting up our database. Once we have setup our database and created our schemas, we will make our admin page using
    admin.py file which automatically gets created when we start our app using 'python manage.py startapp nameofapp'. We will modify our admin page so that we are able to insert the information about 
    our listings and realtors to our relevent tables in our database. After we have done that we will use that admin page to upload the data of all the listings and realtors to our database. Finally 
    we will link our html files with the database. Lets do all of this step by step:

    Step 1: Setting up our Database:
                                    Refer to "postgrest setup and connecting with our django app.docx" file for all of the information relating to our database setup.

    Step 2: Creating our Schemas:
                                Refer to "schemas.txt" and "models.py" file for this.

    Step 3: Setting Up our Admin Page:
                                Refer to "admin.py" file for this.


FETCHING DATA FROM DATABASE TO OUR WEB APPLICATION:
                                                    Now that we have setup our database and added data to our database from the Admin page, next we will fetch data from our database to our application
    relevent pages. The idea is that we will fetch our listings using our model and then we will insert it into our template and then we will simply loop through it to output the listings that are in our
    database. All of this procedure is done in the views.py file where we are rendering the listings.html file. For this we need to import our Listing model.

    We can actually send any data from here (views.py) to the html pages. For example lets say I want to send my name right next to the heading of our listings.html page. What we will do is simply in
    the function where we are rendering the listings.html page we will create a dictionary with key value pair { 'name': 'Ismail' }. Then in our listings.html we can use this by just calling the
    keys (without quotations) of our dictionary inside the double curly brackets {{}}. However instead of creating and passing dictionary, a more common practice is to create a dictionary inside the
    function and then pass the name of the dictionary as another parameter.

     Also we don't want to send the name, instead we want to send the listings. So first we will fetch the listings from the database. Now because we have imported our Listing model we can simply write
    "listings = Listings.objects.all()" and save our data in the listings variable. This is a django function and vscode doesn't understand this. And it will show an error. Although our app will work
    fine, however if we want to get rid of this error we will install a package "pylint-django". Just by installing django we won't get rid of this error and have to add some lines of code in vscode and
    these lines can be found from https://stackoverflow.com/questions/45135263/class-has-no-objects-member.

    So we will fetch all of our listings by writing "listings = Listings.objects.all()" inside our function and then we will save it as a dictionary named "context". Now we will simply use that dictionary
    as a second parameter in our render method and this will enable us to use our listings data from within our listings.html page. We don't have to do use any SQL queries to fetch data.

    Now we will go to our html and loop through our listings. So as of now to display 6 listings we have to write code for each of these listings. But now we will need to write html for only single
    listing and then we will make that dynamic by simply looping through our listings database using jinja syntax. We will loop through our listings inside an if conditional so that if there is no
    listings, we are able to display a message that no listings are available. Now in the for loop we will change all of the static data and replace it with dynamic data using double curly brackets {{ }}.
    So for example instead of writing $490,000 we will write "listing.price" inside these double curly brackets. However we will get the amount without commas which doesn't look very professional. So to
    make it look professional we will use an app called "humanize" which is not added automatically in our setting.py file. We can add it by going to our settings.py and under INSTALLED_APPS section we
    will write "django.contrib.humanize". Then the template in which we want to use the methods of this app we will load this there using {% load humanize %}. Once we do that we get access to whole lot
    of functions available in humanize. To use the commas in the prices of our listings we will simply add an "or" pipe | and after this we will write "intcomma".

    RECENT LISTINGS ON TOP:

    Now lets say we want to sort our listing based on any of the fields in our database for example list date so that the recent listings appear at the top. What we can do is that instead of writing
    Listing.objects.all(), we will instead write "Listing.objects.order_by('-list_date')'. We have used - at the start of our field so that recent listing appears first.

    REMOVING A LISTING FROM FRONT END IF WE UNCHECK is_published FIELD FROM ADMIN PAGE:

    Another thing that need to be changed is that at the moment even if we uncheck the is_published field of any of our listing from the admin area, that listing doesn't disappears from our front-end. To
    make it work we need to add a filter at the end of the listing method that we are using above and that will become "Listing.objects.order_by(-'list_date').filter(is_published = True)". So it would
    show only those listings for which "is_published" is True i-e checked.


    Now in the realtor field because we made a relationship between our listings model and realtors model and because inside realtors model we have written "def __str__(self): return self.name", due to
    this we can use listings.realtors to get the name of the realtors.

    And finally to get the total time passed since a listing has been posted, we can use another humanize function called 'timesince' and it will calculate the the time passed since the list_date.

    Currently the more info button below each of the listings doesn't work. And the routes that we have set up for each of the listing is such that we want our users to be able to access any of the
    listings by just providing the id of the listing. For example lets say we have given an id of 1 to one of our listings, then the route to the individual page of that listing will be "listings/1".
    To make our more info button go to the correct listing, we will write "{% url 'listing' listing.id %}" inside the href attribute of the more info button.

PAGINATION:

    Next we will work on our paginator. We know that our client wants to have paginator in the listings page. At the moment we have a paginator using bootstrap classes but in order to make it work we
    will have to see some django documentations by going to https://docs.djangoproject.com/en/2.2/topics/pagination/ link. Basically in our views.py file of our app, we will import EmptyPage,
    PageNotInteger and Paginator from django.core.paginator.  Then inside the function where we are rendering the html file in which we want to have pagination functionality we will use the Paginator
    as we did in the below function.

    That is the first part i-e fetching from the database. Now we need to deal how to display it. There are documentations on the above link that also shows how we can do this. We can simply copy that
    from there and modify the fields but it will look ugly. Instead we will use bootstraps pagination. Now in bootstrap pagination we have 3 main classes. First we will use ul element and give it a class
    of "pagination" and for each li element we will give it a class of "page-item" and for anchor links inside these li elements we will use class named "page-link". For li element along with "page-item"
    we will give a class "disabled" if there is not previous page and whichever one is active we will use "active" class. We will combine bootstrap and django pagination together so that we have a nice
    looking and also functional pagination. 

    HAS OTHER PAGES:

    First step is to check of there are other pages. So for example currently we are showing 3 listings in each page but if there are less than 3 listings we don't want the pagination to be shown on our
    listings page. For this we have a method "listings.has_other_pages" which will return true if there are more listings than can be shown on single page. So we will use if conditional to check this
    first. And if it does we will create a "ul" element and give it a class of "pagination". Now for pagination if there are other pages then we need to have 3 main things included. These 3 things are
    "Previous page Button" "Buttons for All of the Pages" and Finally "Next Page Button".

    HAS PREVIOUS:

    Next we will check if there are previous pages. If it has previous we want to have a back arrow button which will take the users to previous page, else if there is no previous page we want to have
    a button with disabled link. To check this we have a method called "listings.has_previous" which we will use using another if conditional inside the above if conditional which is checking if we even
    have other pages.  For this we will create a list item and give it a class of "page-item" and inside that list item we will use an anchor link. Now to calculate the href of this anchor we will write
    "?page={{ listings.previous_page_number }} and then inside the anchor links text field we will some left faced arrows which can be achieved by writing "&laquo;" and this will give us these arrows.

    Now if there is no previous page we will again use a list item and give it a classes of "page-item" and "disabled". Inside that list item we will create an anchor link and give that anchor link a 
    class of "page-link", no href because there is not previous page and finally we will also use "&liquo;" to get the previous arrows.

    BUTTONS FOR ALL OF THE PAGES:

    What we want is to loop through all of the pages but for that we must know how many pages are there. Django has something called "paginator.page_range" method that will be appended at last of our
    listings variable to get the number of total pages. So we will write a for loop on "listings.paginator.page_range" and then if our current page is equal to page_number we will give it a class of 
    active and no href. And finally for all other buttons we will give it a class of only page-item (no active class) and for href attribute of anchor links we will simply write "?page={{i}}".

     
    HAS NEXT:

    Next we will check if there are next pages. If it has next we want to have a forward arrow button which will take the users to the next page, else if there is no next page we want to have a next
    button with disabled link. To check this we have a method called "listings.has_next" which we will use using another if conditional inside the above if conditional which is checking if we even
    have other pages.  For this we will create a list item and give it a class of "page-item" and inside that list item we will use an anchor link. Now to calculate the href of this anchor we will write
    "?page={{ listings.next_page_number }} and then inside the anchor links text field we will some forward faced arrows which can be achieved by writing "&raquo;" and this will give us these arrows.

    Now if there is no forward page we will again use a list item and give it a classes of "page-item" and "disabled". Inside that list item we will create an anchor link and give that anchor link a 
    class of "page-link", no href because there is not next page and finally we will also use "&riquo;" to get the next arrows.

MAKING HOME AND ABOUT PAGE DYNAMIC:

    Refer to "views.py" file of our pages app.

SINGLE LISTING PAGE:

    Next we will work on our individual listing page which is rendered when a user clicks on more info button on any of our listings from our "home page" or "listings page". At the moment our routes are
    working fine i-e if a user clicks  on more info button it will be taken to the listing page but that page shows only "Listing" at the moment. So what we want is to write our correct markup and also
    to reach our database to display the correct information about each of our listings. So we will work on two files including the "views.py" file where we are rendering the "listing" page and other is
    the listing.html file. 

    First we will extend our "base.html" file and load humanize and then we will get our mark-up from our material file (provided to us by our front end dept) and copy it to our "listing.html". If we do
    that and reload our page we will get the static markup. Now we will make it dynamic by reaching into the model and grab the data relating to a particular listing. So in the listing method we will 
    call a function "get_object_or_404() and we will provide our model "Listing" and primary key "listing_id as inputs and save this inside a variable called "listing"("remember that we have already 
    imported our Listing model into views.py). What this will do is that when a user tries to fetch a listing with an id which is out of the range or does not exists, he will get 404 error in return. 
    However we need to import this "get_object_or_404" method from django shortcuts.

    Next we will give this variable "listing" inside context dictionary and then pass that dictionary to our listing.html so that we can access the information from there and make it dynamic.

    Some listings have less than 6 photos (other than main photo), therefore we will have to write an if conditional around each of our photo inside our markup, otherwise if a user goes to any of the 
    listing which have less than 6 photos other than main photo, it will get an error.

SEARCH FROM CHOICES:

    (Don't be confused due the reason that our search menu is on our home page (i-e pages app) but our "search page" is inside the "listings app".

    Next we want to work on the search menu. However before we do that we will shorten our "index.html" file. So at them moment for each of the option within our dropdown menu of "State", "Bedrooms" and
    "Bathrooms" we have written each of this options in this "index.html". Instead what we will do is that we will make another python file and in it we will make 3 dictionaries and then importing that 
    file into our pages app (views.py) and we will also add these 3 dictionaries into our context dictionary and then passing them to our render method where we are rendering "index.html" file. This is 
    because our search menu is on this "index.html" file.

    Now in our "index.html" we will delete all the static options and instead we will loop through these dictionaries.

    Next lets handle the submit button because at the moment when we hit this button it makes a get request to "search.html" which is not even a thing in our pages app. So in our form instead of static
    "search.html" we will write {% url 'search' %}. Inside our urls.py file inside listings app, we have this path named "search". And what happens is that when a submit button is pressed it will call
    this views.search method, and inside this views.py file of listings app it will load "search.html" template. 

    Notice that if we select from the options in our search field, the values also appear in the search bar of our browser as parameters. 

    So we will copy our mark up from the file that we got from front end dept and paste it in our search.html template. And now if we click the submit button it will take us to "search" page with all
    of the static html. This search page also contains the search menu at the top. So first, similar to what we did for the search menu in the index.html, we will remove all of the html which gives us
    the options in our drop down menu and instead we will import the dictionaries for these fields from the same choices.py file and loop through it in our search.html file. Also all the listings are 
    static html, so instead we will fetch the data from our listings database and loop through these.


GIVING FUNCTIONALITY TO OUR SEARCH MENU:

    At the moment if we click the submit button, after entering and selecting from the search fields, we will be taken to static "search.html". Now we will give functionality to both of these search 
    forms (i-e one on the home page and other on the search page). Basically what we will do is that when a user inputs values in the search box and clicks submit, we will get the values and save thsse
    inside variable and then we will base our query set on these variable i-e we will filter by that. For example if the user selects state of "Alabama" then we will filter our listings based on this 
    state. 
    We will do this in the "views.py" and "search.html" files of listings app. At the moment our search.html contains static markup for each of the listing. So first we will get our Listing model in
    the search function and then pass it to "search.html" using a dictionary named "context" and loop through the listings over there.

    Once we have connected our "search.html" with the database the next thing that we want is to be able to filter the listings based on what the user selcts in the search fields. For this we need to
    get whatever the user wrote or selected in the search fields and django has "request.GET" method for this which returns all of the values as a key value pair, where keys are whatever is the name
    given to the input and select elements in the html form and value will be whatever the user has written in the fields. 

    Now we will go through these fields one by one.

    1) KEYWORDS FIELD:
                    First we will check if the 'keywords' actually exists in the dictionary that we get by 'request.GET' method. If it does we will save it inside a variable called 'keywords'. Then
        we will use another if statement to make sure that keywords is just not an empty string. If it is not than we will apply the filter on our listings by applying the filter method on our listings
        based on whatever is written in the keywords section. Now what we want to do is that whatever is typed in the keywords field, we will search that in our description field of our database and then
        we will show only those listings which have those keywords in there description. For such searches where we are searching for a specific words in whole of the paragraph we use a method 
        "description__icontains=keywords. If we want case sensitive search we will omit "i" letter and just use "description__contains = keywords. We will filter our listings based on our keywords and 
        pass the filtered listings to the 'search.html'.

    2) CITY AND STATE FIELDS:
                City are also a text field but unlike the keywords we want to exactly match city entered by the user with cities in our database and only show listings for those cities which are searched
        for in the city field. So if we want to do such search we will use a method "city__iexact". Every thing else is same as what we did for keywords field.

    3) BEDROOMS:
                Now for bedrooms field we can filter our listings by exactly matching whatever was written in the search field by using "iexact" method. However instead what we want is that if a user
        searches for say 3 bedrooms, we will show all the listings which have 3 or more bedrooms in it. For this we have "bedrooms__gte" method which stands for "greater than or equal to". Similarly we
        can use lte, gt and lt methods corresponding to "less than or equal to", "greater than" and "less than" respectively. Now if a user selects lets say 4 in the bedroom fields, he will se all the
        listings which has bedrooms equal to 4 or greater. Another thing that we can do is that we can apply the order_by and give "bedrooms" as input and it will sort the results such that the users
        will have listings with 4 bedrooms first and than 5 and so on.

    4) PRICE FIELDS:
                    We will do this similar to our bedrooms fields other than the fact that we want our user to get the search results with the listings which have price equal to less than. 


PRESERVING FORM INPUTS:
                    Next thing that we want to do is that whatever the users inputs in the search fields, we want it to stay there even after the submit button. For this we know that we get the values 
    of whatever the user puts in the form by using the "request.GET" method. So what we will do is that pass this form data withing our context dictionary and in this way we will have access to whatever
    the user has written and selected from the form in our "search.html" page. Now we have used the "values" word to pass our form data to context dictionary and we can now access any fields data. For
    example if we want to get the "keywords", we will simply use "values.keywords". 

    Now in our "search.html" we want whatever a user enters to stay there, so we will give our inputs another parameter "value" and we will set it to whatever the user has typed in the "keywords" field
    by writing {{ values.keywords }}. We will do the same for city because it is also a text input. 

    Now in the drop down selectors, we have the option element in our html element. The way we want our option selcted is that we enter another attribute "selected" in the opening tag of option element.
    So in the opening tag we will use an if condition to check to which of the value in our database is equal to whatever the user picked from the dropdown option. And to whatever option that return true
    we will use "selected" attribute on that. Once we do that to all of our dropdowns options in our search.html, then even after the submit button the previous inputs stay in the search fields.

TO BE ABLE TO SELECT ALL STATES, ANY BEDROOMS and ALL PRICE RANGE:
    At the moment our user cannot select all of the state, any number of bedrooms and any price range options i-e they must select one of the options. This is because we have give an attribute disabled
    to each of these options. However if we want our users to be able to see all the listings and be able to select all states, bedrooms and price options then what we will do is first we will remove
    the disabled from the option. And then in our view method relating to search.html we will use a conditional statement to each of these fields, which will basically say that if this options is
    selected we won't filter our listings page using that field.


"""


from django.shortcuts import  get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import state_choices, bedroom_choices, price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)  #We are fetching all of the data from our Listing model and saving it in a variable called "listings".

    paginator = Paginator(listings, 6)                                           #We are giving our listings object to the Paginator function and saying that we want 3 listings in each page.

    page = request.GET.get('page')                                               #We want to get the page from the get request. Because lets say we are on page 2, we will have a url parameter that says
                                                                                 #page = 2, and we need to get that.

    paged_listings = paginator.get_page(page)                                    #The page number that we get from above will be then provided as a input to this paginator.get_page method.

    context = {
        'listings': paged_listings                                               #Instead of just sending simple listings, we will instead send "paged_listings" that we got above after applying pagination.
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk = listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    listings = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains = keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact = city)   
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            if state == "State (All)":
                listings = listings
            else:
                listings = listings.filter(state__iexact = state) 

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.order_by('bedrooms').filter(bedrooms__gte = bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.order_by('price').filter(price__lte = price)

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET 
    }
    return render(request, 'listings/search.html', context)