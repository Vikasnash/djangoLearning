pip install django \
django-admin startproject firstProject . \
django-admin startapp home \
python manage.py runserver 

*how to create the project in django*\
**django-admin startproject firstProject .**\
django-admin is first command and startproject is sub command

project name folder would have all configuration files
urls and setting.py are two main file
setting.py has lots of global variables are defined

**django has app system, so we can create apps in separate folders**
sub command is **startapp** post creating the main app

**django-admin startapp home**

***every time we create app we need to add this in settings folder*** , we do this in main app
then we can update the views also and need to add this views to urls.py of main app

1. cycle to running app \
**endpoint /home -> urls.py -> views.py -> def home since it has request response**
2. templates can be created in *template/projectName* folder and arguments can be passed from view.py using render
3. django template language (DTL): - this helps use to create the dynamic output
4. Django project is made up of apps and all apps should be self-contained that means everything needed for that apps should be there in that app
5. for example *firstProject* app is dependent on home app,  
6. Django Admin interface to view and manipulate the data-ONE OF THE POWERFUL INTERFACE, ADMIN ENDPOINT IS ALSO AVAILABLE IN DJANGO FRAMEWORK
7. Migration explains what kind of changes a database can perform, we have to apply the changes to app by running the command *migrate*
   * python manage.py migrate

**Chapter 2** 
1. Django Admin interface to view and manipulate the data-ONE OF THE POWERFUL INTERFACE, ADMIN ENDPOINT IS ALSO AVAILABLE IN DJANGO FRAMEWORK 
2. **Migration** explains what kind of changes a database can perform, we have to apply the changes to app by running the command *migrate*
   * python manage.py migrate 
   * Django know whether the database is behind the system changes because of Migrations
3. Creating the *createsuperuser*, we have to provide the username, email and pwd
   * python manage.py createsuperuser
4. Easily visualizing the data and creating the data :- user can be created and deleted from the web page and that will keep a track of activities 
5. User Authentication in two simple steps:
   * now there are three endpoints and authorised in using decorator 
   * admin/
   * home
   * authorised

**Chapter 3**
1. How Django interacts with database * using Django ORMs
   * how structure of models works 
   * class models to database tables , each class attribute is a column is table
   * Classes -> defining a model -> MakeMigrations -> Migrate -> Database
2. first Model using Django ORM 
   * create an app called notes , **django-admin startapp notes
   * don't forget to add the app in main app settings folder
   * open models.py to create the models, it would be the first model, so far we are creating views and endpoints
   * third step is makemigrations using ** python manage.py makemigrations _because migrations come from models
   * last step is apply the migrations ** python manage.py migrate , 
   * so we have created the first model and changes have been applied to database
3. Using admin for data and manipulation 
   * which model can be displayed using the admin.py of an app, Say notes app
   * admin.py have configuration settings and 
   * we have to register the model as well before going on web to see the model in admin location
4. using Django shell for creating and querying the data, handle models through codes
   * Django shell ** python manage.py shell
   * from notes.model import Notes -> mynote = Notes.objects.get(pk = '1')
   
Following are lines of codes to run in the shell:

    >>> from notes.models import Notes
    >>> mynote = Notes.objects.get(pk = '1')
    >>> mynote.title
    'My First note'
    >>> mynote.text
    'Django is so amazing'
    >>> Notes.objects.all()
    <QuerySet [<Notes: Notes object (1)>]>
       
    Notes : return of Notes.objects.all() is querySet datatype, whcih is very usefull, its kind of list with super power
   
    >>> new_note = Notes.objects.create(title = 'second Note', text = 'this is second note')
    >>> Notes.objects.all()
    <QuerySet [<Notes: Notes object (1)>, <Notes: Notes object (2)>]>
    >>> Notes.objects.filter(title__startswith = "second" )
    <QuerySet [<Notes: Notes object (2)>]>
    >>> Notes.objects.exclude(title__startswith = "second").exclude(text__icontains = 'Django')


Chapter 4 **Building dynamic webpages**\
Since we have created the Notes app, lets creates views in notes
1. creating dynamic webpages
    * open view.py files and add views for the model from model.py
    * add urls.py file under notes and add the path
    * now include the notes urls to firstProject main app urls.py file with some endpoint
    * create the html notes_html.html template within notes with dynamic template language \using {% %}. Everything within curly brackets {} is DTL 
    * Notes can be created from shell or in code
    * run the app using **python manage.py runserver**








