"""
 We want our users in the front end to be able to register and then login. For this functionality we will create a new app called "accounts".

SETTING UP OUR REGISTER AND LOGIN ROUTES:
    Nos django already has a user system inplace and we don't have create our own account or user model. So if we go to pgAdmin, we can see the "auth_user" table there with the columns including like
    "username", "first_name", "last_name", "email", "is_staff", "is_superuser", "last_login" etc. At the moment we have only one user and it is the superuser that we created to access the admin area.
    In the first step we'll setup our "register" and "login" routes and to do that we need to create "register" and "login" templates. Inside templates folder we will create a new directory "accounts"
    and inside this we will create 3 templates including "dashboard.html", "login.html" and "register.html". Once we do this we will setup our routes and we know that we don't get a urls file by default
    when we create a new app so we will create it ourself. We will need to create 4 routes in the urls.py file including register, login, logout and dashboard. Then for each of these routes we will need to
    create methods in views.py of accounts app. However the logout method is not going to render a seperate template instead we will implement some functionality to logout our users and then redirect them 
    to our home page i-e index.html. Now to redirect we would need to import this method from django.shortcuts. And finally in order for our routes to work we also must include our accounts.urls file into
    main urls.py file inside btre folder. Similary we will need to change the "href" attributes of register and login buttons inside the navbar so that they take us to correct pages.

    Now once a user is actually logged in we don't want to show these register and login buttons. So what we will do is that we will add a conditionals and it will say wellcome to the user and will have 
    links to the dashboard and a logout link (We will do this later).

    Another thing that we want is similar to what we did to other buttons in our navbar to have a dynamic active class to our "nav-item", depending upon where we are in our route using the if conditional.
    
    Next we will copy our html from the register and login templates that we got from front end and copy it into our register and login templates.

    Now there are two kind of request for register.html. A get request when someones clicks on register button and a post request when a users registers using the form in register.html. So we will use a
    if conditional inside 'views.py' file of our accounts app to check if the request is a post request or a get request and also what to do in response to these each type of request. Also we need to change
    the action and method attribute of our register and login forms within html templates so that they go to correct page after the form is submitted and that method is POST method. Another thing that we need 
    to do is that inside our forms we will include something called "csrf_token" which prevents cross site forgery. To include it imediately after the form tag we will write "{% csrf_token %}".


MESSAGE ALERTS:

    Now that we have setup our login and register pages and setup our routes for these, next we will work on message alerts so that in case if users do something wrong while filling the form 
    than we want to display a nice bootstrap formatted message alert about what got wrong. Django by default comes with messages app and we just need to configure this by entering message tags in our
    settings.py file at the very end. And we can simply get this message tag from django documentation relating to this messages app. Then we will make some changes in this tag and instead of the
    "messages.INFO" to "messages.ERROR" and set this to "danger". And the reason that we have set it to danger is that we will use this in our markup later and this "danger" represents the red color in
    bootstrap.
    We will then create a seperate template for our messages/alerts inside the partials folder. And we will use bootstrap classes to show nice looking messages. 

    _ALERTS.HTML:

    Inside the alert we will first check if there are any messages by using if conditional. If there are any messages than we will loop through them and for each message we will create a div and give it an 
    id of "message" and class of "container". Inside that div we will create another div and give it two bootstrap classes including "alert" and "alert-danger". However in the setting because we have set
    the "messages.ERROR" to danger so instead of "alert-danger we will write "alert-{{message.tags}}. Next we want this message to be dismissible so for that we will give this div another class called
    "alert-dismissible", "text-center" to make it center, use an attribute called "role" and set it to "alert". Now in this inner div because we are displaying a dismissible alert we also will need to create a
    button and give it a type of button and a class of "close". We will also use another bootstrap attribute for this button called "data-dismiss" and set it to "alert". We want an X mark to close the
    message and for this inside our button tags we will use a span and set its "aria-hidden" attribute to "true" and inside that span we will write "&times;". A

    Next inside this inner div we will create a strong tag to display our alert message. For this we will use an if conditional to check whether the title of the message should be an error or not. If it is 
    an error we will simply write "Error:". If not will write {{ message.tags | title }}. Below these strong tags we will write {{ message }}, this is because we only want to show word "Error" in bold letters
    and message in normal letters.

    We can use this message alert html snippet in all of our django applications to display the errors.

    Now in order to use this _alert partials in whichever template/page, we will simply go into the view method/function relating to that page, we will use "message.error() function and inside this fuction 
    we will provide two inputs "request" and then whatever message we want to output. Next we need to include our _alert partial in the template where we want to display the message (where we are redirecting
    to after we receive a POST request). In this case we will not include our _alert partial at the top, instead we need to decide where we want to display the message and at that place we will simply write
    {% include 'partials/_alerts %}. In our case we will use it in our "register" and "login" templates just below the div with a class of "card-body". However for all of this we will first need to import 
    messages app into our "views.py" file and we can do this by writing "from django.contrib import messages".

    SELF DISMISSING ALERT:

    Now another thing that we can do is to make our errors to disappear on its on. For this we will use some custom javascript. Our javascript file is inside the js directory, inside static, inside btre 
    directory. Inside it we will use "setTimeout" function which is a javascript function which does something after holding it for sometime. This function takes a callback function and inside that call
    back function we will use jQuery to grab an element with id of "message". And on it we will use a "fadeOut()" method which takes in speed as input. We will give it a input "slow". The second parameter
    of the "setTimeout" function is the time and we will write "3000". So after 3 seconds it will fadeOut.

    Since we have put this function in the static folder inside btre directory we will need to run "python manage.py collectstatic". And now we can use it. (Remember that sometimes we need to clear the
    caches in our browser (Shortcut shift + F5) to make things work properly.)

USER REGISTERATION:

    GETTING DATA FROM USERS:

    In order to register our users we need to fetch whatever is written in the registeration form. Now we know that our registeration form method is set to "POST" and in order to get the data from POST
    request we use "request.POST" method and this method takes in the name that we gave to the input element in our HTML form. So we will get all of the fields from our registeration form and we will
    save these in 6 variables.

    VALIDATIONS:

    Next we will do some validations to confirm that information provided is valid. First thing that we will check is that both password fields match. If not we will display an error using "messages.error"
    method. 
    If the passwords match we will move to next validation which is to check if the entered username or email doesn't already exist in our users database. We didn't created a user database, however this is
    already included within the django by default but in order to use it we need to bring it in. To do that we will write "from django.contrib.auth.models import User". Once we brought the User model, we will
    check if the username entered by our user already exist in it by writing "if User.objects.filter(username=username).exists()". The first username in this method is the name of field in the database and 
    this method simply loops through all the users to check if a user with the same username already exist in our database. If it returns True we will again display an error using "messages.error" method.
    We will do the same for email also using else.

    REGISTER A NEW USER:

    After the user passes the validation we will use create a "user" variable and for this we will use "create_user()" method on "User.objects". However this method requires all of the fields to be given to
    it.

    WHAT TO DO AFTER REGISTERING A USER:

    Next thing to decide is what we will do after we have registered a new user in our database. Following are two strategies that we can implement:

        1) 1st is to login our user automatically. For this we will use "auth.login(request, user)" method. However for this we have to bring in "auth" from django.contrib. We will also want to display a
        success method along with logging our user in so we will write "messages.success(request, "You are successfully logged in"). And final thing to do in this method is where to send the user. In this
        case lets send them to Home Page using "redirect" method. However we have not included the _alerts partial in the home page yet so it won't be able to display the messages. 

        2) Another strategy is to instead of logging in our users automatically we will send them a success message and will ask them to log in while redirecting them to login page.


    Now when a new user is registered we will be able to see him from our superuser admin area. The hashing of password is automatically done by django so we don't have to worry about that.


LOGGING IN OUR USER:

     Now we will make our users to be able to log in once they have been registered. Similarly to what we did while registering our users, first we will need to get whatever is entered in "username" and 
     "password" fields and we will use "request.POST" method. Once we have got both of these and saved them inside variables, next we will use "auth.authenticate()" method to authenticate our users. Now
     this authenticate method requires two inputs by default which are "username" and "password" and it will check them against each username and password in our database and it will return a "User" object
     if credentials provided are valid. We will save that "User" object in a variable. However if credentials aren't valid it will return "None". 

     So to verify what did "auth.authenticate()" method returned, we will use if conditional. If it didn't returned 'None', we will use "auth.login()" method to login our user. This login method expects two
     inputs including request and the user that was created using "auth.authenticate()" method. We will also display the success method while redirecting our users to "dashboard" page. However for message
     to get displayed on dashboard page we need to include our _alerts partial in it somewhere.


MAKING OUR NAVBAR DYNAMIC IN RESPONSE TO LOGGING IN OF USER:
                    Next thing that we want is that when a user is logged in, instead of "Register" and "Login" links/buttons in the navbar, we want to show "dashboard" and "logout" buttons. For this we will
     use if conditional. To check if the user is logged in we will use a django method "user.is_authenticated". So we will use if conditional in our navbar just before list items "register" and "login" and
     we will say if the user is authenticated then show "Dashboard" and "Logout" buttons. Else if the user is not authenticated we will simply use the previous markup which is currently showing "register"
     and "login" links. 
    
    DASHBOARD:

     First we will make a dashboard link. We will make a dashboard list item and inside it we will use anchor tag similar to how we did for register list item. However instead of just displaying "DASHBOARD"
     we also want to say "Welcome username". We have access to this "user" object within all templates. So inside the anchor tags we will say "Welcome {{ user.username }} (Dashboard)". 
    LOGOUT:

     Next we want a "logout" button. However the logout cannot be an "anchor link" with a "GET" request. A logout has to be a "POST" request. So instead we will make a form which will look like a link. This
     is because to make a POST request we use forms. We could use javascript to fetch API or use something like AJAX, but here we will make a simple form to logout. So right below the dashboard link item we
     will use another "link item" and give it a classes of "nav-item" and "mr-3". Inside it we will put an anchor link and we will give it a class of "nav-link". In the href attribute of this anchor link
     we will use javascript to look for an element with an id of "logout" and submit that form. To that inside href we will say "javascript:{document.getElementById('logout').submit()}". javascript: allows
     us to write javascript. Then we will write logout inside these anchor tags. Next we will make a form with an id of logout and we will set its action attribute to go to logout route, method to 'POST' and
     ofcourse give it an id of "logout". Also remember that inside this form we will use csrf_token and below that we will use input element and set its type attribute to hidden.

     In our logout route we will first check if it is a post request (like we did with register and login), and if it is a post request we want to logout. For this we will use "auth.logout()" which only takes
     request as input. Along with that we will also display a success method and redirect our users to home page.

CUSTOM/DYNAMIC PAGE TITLES:

                At the moment no matter on which page we are in our web application, the title of our pages always remain the same i-e BT Real Estate. This BT Real Estate is what we put in our base.html inside
     the title tags. However we want to display the title of page differently for each page and also we want to show dynamic titles for individual listing page so that it shows the title of the listing at the
     title bar. We want the title such that for every page after "BT Real Estate" there is an or pipe character and then the custom/dynamic title.

     To implement this in the title tags of our base.html after "BT Real Estate" we will simply use {% block title %} {% endblock %}. And then on every page where we want to use custom/dynamic titles we will
     simply use this block and inside the block we will write our custom/dynamic title. For example for home page we want to include "Welcome" along with "BT Real Estate". To do this we will go to the top
     of our index.html and just above the block content we will write {% block title %} | Welcome {% endblock %}. We will do this on every page where we want to add custom but static title. Now on single
     listing page we want to use the title of our listing and for this we will write {% block title %} | {{listing.title}}{% endblock %}

DASHBOARD FUNCTIONALITY:

    At the moment if we look at the dashboard of any user we will see that there are 3 inquiries but they are all static html. However what we want is that only those enquiries which are made by users should
    go to there dashboard. For this we will need to import the 'Contact' model in the views.py file of accounts app because from here we are sending dashboard.html. So what we will do is that insdie the
    function where we are sending our dashboard.html, first we will get all of the contacts using 'Contact.objects.order_by' and then we will sort these by dates using .('-contact_date') at the end. And 
    finally we only want to display those inquiries to the user which are made by them so we will filter by user_id which has been logged in. To know the user_id of our logged in user we will simply write
    request.user_id. We will save all of these filtered inquiries, save them in a variable, pass this variable to the context dictionay and finally pass this context dictionary as a second parameter where
    we are rendering 'dashboard.html'. In this way we will access to these contacts in our dashboard.html and we will make it dynamic.

    To make our dashboard dynamic first we will change static Welcome message to dynamic by changing the part of our message {{user.first_name}}. Next we will only need one HTML markup for inquiries and so
    we will delete other two. And then we can make these dynamic by first using a if conditional to check if there are any enquiries made by this user and if there are we will simply loop through them 
    dynamically. And if there are no we will display a text saying that you have not made any enquiries yet. 



"""


from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
      # Get form inputs
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      password2 = request.POST['password2']

      # Check if both passwords match
      if password == password2:

          # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            # if username already exists
          messages.error(request, "Username already exists")
          return redirect('register')   
        else:
          if User.objects.filter(email=email).exists():
              # if email already exists
            messages.error(request, "An account already exists with similar email")
            return redirect('register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        # after user has been registered (We will use 2nd strategy)
        user.save()
        messages.success(request, "You have been registered successfully. Please login")
        return redirect('login')
        # if passwords do not match
      else:
        messages.error(request, "Passwords do not match")
        return redirect('login')



    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You have been successfully logged in")
            return redirect('dashboard')
        
        else:
            messages.error(request, "Could not find the user with provided username and password.")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have been successfully logged out')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts 
    }
    return render(request, 'accounts/dashboard.html', context)