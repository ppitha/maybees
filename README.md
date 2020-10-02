Beekeeping records python project

Requirements:
* The purpose is record the observations and actions taken by beekeepers relating to hives and colonies at apiaries.
* An apiary is a location with one or more hives. 
* A hive is infrastructure (deeps, supers, equipment) housing one colony at a time.
* A colony is the collective organism of bees attached to one queen, which lives in a hive at an apiary.

Functional requirements
* Creating an apiary, hive, colony should allow the ability to upload one or more pictures associated with the object, one of which is designated the primary picture.

Ideas for further development
* Mobile interface (API + mobile app)
* Reminders/tasks - by hive (colony)
* Colony, hive and apiary level analytics
* Frame and honey production data gathering
* Activity time logging
* Cost tracking


> Set up a virtual environment

    C:\Projects>mkdir .venv

    C:\Projects>python -m venv .venv\maybees

    C:\Projects\maybees>.venv\maybees\Scripts\activate.bat

    (maybees) C:\Projects>

> Install Django in the virtual environment
    
    (maybees) C:\Projects>python -m pip install Django
    Collecting Django
    ...
    Successfully installed Django-3.1 asgiref-3.2.10 pytz-2020.1 sqlparse-0.3.1

https://twitter.com/explore> Start project

    (maybees) C:\Projects>django-admin startproject maybees

> Start app "colony"
    (maybees) C:\Projects\maybees>python manage.py startapp colony

> Install a database
    version 11.8
    server: PostgreSQL 11
    database: postgres
    username: postgres 
    password: don6t)PinkFleeze

    pgagent - job scheduler

    pgadmin - Master password: torpidIf5(gleep$

    new server: 
    server: postgres
    database: postgres
    username: postgres
    password: don6t)PinkFleeze

    Set up maybees/settings.py for postgres db

    * If you’re using PostgreSQL, you’ll need the psycopg2 package. Refer to the PostgreSQL notes for further details.

    >pip install psycopg2

    Set up basic database tables for Django
    python manage.py migrate

> Create models

    Add models to colony/models.py
    Install the colony app
    add     
        'Colony.apps.ColonyConfig',
    to INSTALLED_APPS in maybees/settings.py. This names a class in colony/apps.py (already created)

    Note: Self-referential foreign key is done by passing the name of the class (which has not yet been created) as a string:
        class Colony (models.Model):
           parent_id = models.ForeignKey("Colony", on_delete=models.DO_NOTHING)
       

    Run:
        python manage.py makemigrations colony

    to create a migration to create/change the tables 

    See the DDL that will be run for this migration (does nothing): 
        python manage.py sqlmigrate colony 0001

    Apply migrations (any that have not been applied)
        python manage.py migrate

> Create an admin

    python manage.py createsuperuser
    admin
    ppitha@gmail.com
    part&Forge^white

    Register models Apiary, Colony, Hive for admin in admin.py

> Set up views
    
    add stub index view to colony/views.py
    create colony/urls.py and add a URLconf for index stubs
    set up the root urlconf in maybees/urls.py

now /admin and /colony are valid routes

8/29

> Add support for uploading media

    Install pillow
        pip install pillow

    Create a media folder:
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    Create the directories
        mkdir media
        mkdir media/images

    Use image fields like these in models
        title = models.TextField()
        cover = models.ImageField(upload_to='images/')
    The location of the uploaded image will be in MEDIA_ROOT/images.

    After migrating this changes, the admin forms for the models with ImageField columns will include a file chooser for uploading images

Add CSS file and templates for displaying images on apiaries and hives.

9/7
    Add functionality to create colonies (map table)

    Add colony has a parent for the parent colony, but nothing for what hive it's in.

    Tutorial
        #2 - Models, basic admin
        #3 - Views, templates, rendering
        #4 - Forms and more on views
        #5 - Tests
        #6 - Adding CSS, images
        #7 - Improved admin 

    Used "Inline" to add hive_colony_map form to the admin page for colony. But there's functionality that should happen when you add a new hive-colony-map (HCM) record, which means it should probably have its own form:
    * When a new HCM record is added, if there is another HCM record for the same hive and colony, these records should be ordered by start_date.
        * Two records may not have the same start_date.
        * A record may not have the same start_date and end_date
        * The end_date of the one before the new record should be set to the start date of the new record. This update should be confirmed.
        * If the new HCM record has a null end_date (expected), then it should be the last HCM record
        * If the new HCM record has an end_date, then the start_date of the following record should be set to the end date of the new HCM record. This update should be confirmed.

    Fields to add
        Colony.Variety (Carniolan, Italian, etc.)
        date acquired (different from birth date)

9/19
    Integrating approach by Marina Mele - http://www.marinamele.com/taskbuster-django-tutorial
    Installed Selenium for tests. On Windows, I needed to download geckodriver.exe, and put the path to it in the PATH system variable.

    With the requirements folder, now a user can do the following to work on the project:
    * create their own virtual environments (one for testing, one for dev)
    * run .venv\<dev env>\Scripts\activate.bat 
    * run pip install -r requirements\development.txt 
    * run .venv\<test env>\Scripts\activate.bat 
    * run pip install -r requirements\testing.txt 

    Why is there a different virtual environment for the tests (separate from the app)? It is clumsy to remember. In my case:
    * maybees is the app venv
    * maybees-test is the testing venv

    The reason is, you don't want to bundle testing to the actual app - which, in production, should run without testing. 

    I really ought to brand my app differently, as "maybees" is for my apiary suite (? or "business"?)





