"""

CUSTOMIZATION:

   First we need to import the model that we want to register here. Once we did that next we will create a class to add customization of our contacts display on our admin area. This includes "list_display" to
   which we will give all the fields of our model that we want to get displayed. Next we will set some fields as links so that if a staff user click on that field that inquiry is opened. We will also setup our
   search_fields, and users can search filter all of the inquiries/contacts using these fields. And finally we will set list_per_page to 25 to show 25 contacts/inquiries per page.

REGISTER OUR MODEL:
   To register our Contact model we will write "admin.site.register()" method which takes two inputs. 1st is the model that we are registering and 2nd is the class object that we created for customization.

"""


from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
