## Django Project Alt Template

features:

    - Docker containars for dev and production
    - Main app is flatpages like app for Menu Pages
    - Bootsrap 4
    - Start html temlates: base.html, header.html
    - default include html template for bootsrap form
    - include html template for messages contrib app
    - add sitemaps and robots.txt
    - makefile with automatization commands
    - postgresql docker container
    - redis for cache and sessions
    - Sentry logs for production
    - pipfile  
    - django-extensions
    - django-debug-toolbar for dev


### Start:


start project:

    $ django-admin.py startproject --template=https://github.com/assigdev/django-project-alt-template/archive/master.zip --name=Procfile project_name


#### For dev


Up docker containers:

    $ make dev b=1
    

For next up, use

    $ make dev

**if you run docker with sudo, run make with sudo**

    
for configure (migrate, collectstatic and createsuperuser) in another terminal session:

    $ make configure


#### For dev with sqlite without docker containers(Not recommended
)

clone repository:

    $ git clone https://github.com/assigdev/it_courses
    
Then up django dev server:

    $ make dev_light b=1
    
For next up use
    
    $ make dev_light

other manage commands:

    $ pipenv run python manage.py *command*

    
#### Production:

 - set domain_name in docker-compose.prod.yaml
 - set sentry url in settings/prod.py
 - up docker containers:
  
  
     $ make prod b=1  # b=1 for building containers
    
    
 - then configure (migrate, collectstatic and createsuperuser) in another terminal session

    $ make configure





for update collectstatic and migrations

    $ make update

for reload app

    $ docker-compose down
    $ make prod



