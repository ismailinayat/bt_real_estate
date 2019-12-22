"""
After making sure we are in our virtual environment, we will run "python manage.py startapp contacts" in our terminal. This will make the contact folder and inside all the standard and default files that
automatically get created. The next thing that we need to do is to include our app in INSTALLED_APPS list inside settings.py file or otherwise our migrations will not get created.

CONTACT MODEL:
            First thing that we want to do in our contacts app is to create a "Contact" model. We will do that in "models.py". Once we did that we will also need to make a table in our database and to do
  that we need to create and then run migrations. We can do both of these by writing "python manage.py makemigrations contacts" and "python manage.py migrate" to do both of these respectively.

CONTACTS ADMIN CUSTOMIZATION:
  Now that we have created our contacts table within our database we will register our Contact model in the admin.py file of our contacts app so that we can actually see them in the admin area. For this
  refer to the "admin.py" file.

  Once we have registered our models we can see and add our contacts from there. However it doesn't makes sense to make an inquiry from admin area. What we want is to actually create a new contact model
  instance when a user of our website makes an inquiry from the front end.

CONTACT FORM:
  Next we will work on the contact form. Essentially what we want is to have some dynamic inputs in the fields automatically. First we want to do is that to fill the first field of our contact form with the
  title of our listing for which the inquiry is being made. Similarly if a user is logged in we want to put his username and password automatically into that.

  Our form is in the listing.html page. So in there we will first change the action of our form to {% url 'contacts' %} and method to 'POST'. This is because we want this form to make a POST request to 
  contacts route and when we have a post form in django we want to secure it by writing "csrf_token" just below where form is created. However we have not yet created the url with name of contacts. So for
  this we will first create a "urls.py" file within our contacts folder and in this file we will have only one url. So after importing path and views in there we will create url pattern and init we will
  create our path. Just like every other url pattern we will also need to include it in the main urls file in btre folder and also we will need to create our views method in the views.py.

  Next we will set the value of listing field of our form to {{listing.title}}. We are able to do that in the listing.html because we have passed the Listing model to the listing.html via context while
  rendering the page. We also have access to user model. So what we want is that if a user is logged in then we want to send the user_id as hidden input because we will need that. So we will use if
  conditional to check if the user is authenticated and if it is we will create a hidden input with the name of "user_id" and value of {{ user.id }}. Else if user is not logged in we will simply send this
  hidden input with "0" value. Along with that we also want this form to send the email of the realtor to which this listing belongs to for which inquiry is being made and finally we will also need to get
  listing_id. However these two hidden fields should be outside the if conditional where we check if the user is authenticated because we want to get the realtors email and listing_id no matter if the user
  is logged in or not.

  Now the reason for why we want to get the "user_id" and "listing_id" from and enquiry and save them in our database for a contact enquiry is that later we will user them to implement some validations 
  so that a user with same user_id cannot make another enquiry for the listing with the same listing_id.

  Next in the name and email field within our form fields for the user, we will use the if conditional in the input element for the value attribute of input. If a user is logged in then we will use the same
  user.is_authenticated method, and if it is, we want value of our input to be equal to {{ user.name }} and {{ user.email}} to automatically input the value of user name and email fields in the inquiry form.

CONTACT SUBMISSION:
  Next we will handle the submission the contact form. So in our views.py we have already created the method for the 'contact' path that we are getting from urls.py file of our app. However previously we
  simply used an empty returned to get rid of the error when we were making our contact form dynamic.
  
  CAPTURING VALUES:
  Now first we will check if the request is the post request using if condtional and if it we will capture the fields from our form. So again if we want to get a field from our form which is being submitted
  through post request we will simply use 'request.POST['field_name']' to capture the value of that field.

  SAVING IN OUR MODEL:
  Once we have captured all of our values and save them using variables we will make another variable "contact" and then using our model 'Contact' we will create a new model instance. And then we will call
  contact.save() method to save this instance.

  Once we saved this contact inquiry in our Contact model we will also send a success message using our messages app. However for that we will also need to import messages app.

  CHECK IF INQUIRY OF THIS LISTING HAS BEEN MADE BY SAME USER:
  We also want to implement a validation check for our registered users that if a user has send an inquiry of a listing then that user won't be able to make another inquiry for same listing and we will 
  display them a message that an enquiry for this listing has already been made by you. So just below where we have got all the fields from post request and we have saved them inside the variables we will
  use an if conditional and we will check if the user is authenticated and then we will use a variable which we will set equal to 'Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)'. This
  will simply filter all of the contacts and return only those contacts which has same listing id and user id. If after applying filter if there is a contact with same listing_id and user_id then that contact
  will get saved in our variable. Then we will use another if condition to check if there is anything in that variable and if it does we will simply display the error that an inquiry for this listing has
  already been made by you and we will redirect the user to the same listing. Now that we have done this a user will not be able to make duplicate enquiries for same listings. We cant make such validations
  for non-registered users so we can't stop them to make duplicate inquiries. We can do so by adding ip tracking but we are not going to get into that.

SEND EMAIL TO REALTOR:
  Next thing that we want to implement in our application is that automatic email sending to our realtor for an enquiry of a listing related to that realtor. To do that we will first import "send_email" 
  from django.core.mail. When we will use this "send_email" app, it will require email subject, message, from, to (an array of emails to whom we want to send email), and we will also need to set fail_silently 
  and set it to False so that we get an error if something goes wrong. We will write these just after we have got our fields from the post request and we saved them in our database because we don't want to 
  send email to our realtors if there was an error during the submission of form. We will also need to configure our email app in the settings.py file. So in settings.py at the bottom end we will set 
  EMAIL_HOST (we will use gmail and so it will be 'smtp.gmail.com'), EMAIL_PORT (587 but depends on our smtp host), EMAIL_HOST_USER(from where we want to send the email), EMAIL_HOST_PASSWORD(the password 
  of email address which will use to send the emails), EMAIL_USE_LTS set to True.





"""



from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages

# Create your views here.

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing_id = listing_id, listing = listing, name = name, email = email, phone = phone, message = message, user_id = user_id)

    contact.save()

    # send email
    send_mail(
      'Property Listing Inquiry',
      'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
      'ismailinayat@gmail.com',
      [realtor_email, 'ismailinayat8672@gmail.com'],
      fail_silently=False,
    )

    messages.success(request, 'Your request has been submitted. A realtor will get back to you soon.')

    return redirect('/listings/' + listing_id)

