from django.core.management.commands import startapp


APP_TEMPLATES = {
    'full': 'https://github.com/assigdev/django-startapp-alt-template/archive/full.zip',
    'default': 'https://github.com/assigdev/django-startapp-alt-template/archive/default.zip',
}


class Command(startapp.Command):
    help = "Alternative start app 'app_name' or 'app_name --type=full'"

    def add_arguments(self, parser):
        parser.add_argument('type', nargs='+')

    def handle(self, *args, **options):
        app_type = options.get('type', 'default')
        options['template'] = APP_TEMPLATES[app_type]
        options['extensions'] = 'py'
        super().handle(**options)
