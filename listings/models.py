"""
Now that we have designed our schemas, we will build models based on those schemas. And after that will run the migrations which will then create the tables in our database based on those models. Now
in our django documentation they told us that while building the models, along with fields we also must give the type of data for each field. The fields are CharField, DateField, IntegerField etc are
the few examples of fields which we will use.

When we created our apps using manage.py, in every app folder a models.py was also created. And the way we define our models is by using class and the name of model/class should be the single version
of our app.

By just creating the model it doesn't mean that our tables are created. For creating our tables we need to run our migrations. For this we will go to our terminal and write "python manage.py makemigrations
which will not affect our database instead it will only create the migrations file in the migrations directory of our related app that we will then run to create our tables. The migration file that will
be created will be based on our models. However if we run above command we will get an error. This is because in our models we are using ImageField and in order to use it we need to install a dependency
called "Pillow". After installing it when we will run our makemigration command again it will create the migration files for all of our models. If we want to create migration for a specific model we
will have to specify the name of our app at the end of our command.

Now that we have our migrations ready lets run them using "python manage.py migrate". Now here is when our database will get changed and we can verify it in the pgAdmin.


"""
from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)  #Our realtor field within Listing model will be the foreign key as we will get it from the Realtor model which will be defined
                                                                        #in the models.py file of realtors app. Sometimes when a model which is set as foreign key within another model, if it is deleted
                                                                        #then the other model is also gets deleted. But we don't want that our Listing model gets deleted even if Realtor model is deleted.
                                                                        #So we set another property "on_delete" to "DO_NOTHING".
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zip_code = models.CharField(max_length = 20)
    description = models.TextField(blank=True)                          
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d')      #Here we need to tell where the images gets uploaded to. In django there is a media folder, which we will set up and anything that
                                                                       #gets uploaded in the admin area gets added in the media folder. Here we will define the folder inside that media folder. Now what
                                                                       #we want is to up load our photos in a folder with date structure like year, month and day. 

    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default= datetime.now, blank = True)
    def __str__(self):                                                 #In our admin we will have a table that will display each listing. For this we need to pick a main field that will be displayed
        return self.title                                              #to identify that perticular listing. We want the title of the listing for this. These two lines will do this for us. 