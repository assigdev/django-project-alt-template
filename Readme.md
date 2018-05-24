# Django Project Alt Template

#### Features:

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
- pipenv  
- django-extensions
- django-debug-toolbar for dev
- alternative startapp command altstartapp


### Start:


start project:

    $ django-admin.py startproject --template=https://github.com/assigdev/django-project-alt-template/archive/master.zip --name=Procfile project_name


### For dev


Up docker containers:

    $ make dev build=1
    

For next up, use

    $ make dev

_if you run docker with sudo, run make with sudo_

    
for configure (migrate, collectstatic and createsuperuser) in another terminal session:

    $ make configure


### For dev with sqlite without docker containers(Not recommended
)


    
Up django dev server:

    $ make dev_light build=1
    
For next up use
    
    $ make dev_light

other manage commands:

    $ pipenv run python manage.py *command*

    
### Production:

 - set domain_name in docker-compose.prod.yaml
 - set sentry url in settings/prod.py
 - up docker containers:


 
        $ make prod build=1  # build=1 for building containers
    

    
 - then configure (migrate, collectstatic and createsuperuser) in another terminal session



        $ make configure




for update collectstatic and migrations

    $ make update

for reload app

    $ docker-compose down
    $ make prod


#### altstartapp command

    
    $ python manage.py altstartapp
