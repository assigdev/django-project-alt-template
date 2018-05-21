from .models import Page


def main_context(request):
    return {
        'pages': Page.objects.exclude(slug='home'),
    }
