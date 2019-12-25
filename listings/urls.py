from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'listings'),                  #Now if we leave this empty it will pertain to address /listings which is what we want.

    path('<int:listing_id>', views.listing, name = 'listing'), #We want our address to like like "/listings/12" where 12 is id of a particular listing. For this we need to include a parameter in our url
                                                               #and not leave it empty. But this listing_id also needs to be passes in the views.py file of our listings app inside the function where
                                                               #we are rendering the listing page just next to the request parameter.

    path('search', views.search, name = 'search'),

    ]