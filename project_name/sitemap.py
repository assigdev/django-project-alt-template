from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from apps.main.models import Page
from django.views.generic import TemplateView
from {{ project_name }}.settings import SITE_URL


class StaticSitemap(Sitemap):
    protocol = 'http'

    def items(self):
        return ['main:home', 'html_map']    # url names

    def location(self, obj):
        """
        need for static pages
        """
        return reverse(obj)


class PageSitemap(Sitemap):
    protocol = 'http'

    def items(self):
        return Page.objects.exclude(slug='home')


class HtmlMapView(TemplateView):
    template_name = 'sitemap.html'

    def get_context_data(self, **kwargs):
        context = super(HtmlMapView, self).get_context_data(**kwargs)
        # context['objects'] = ModelClass.objects.all()  # set your ModelClass with get_absolute_url
        return context


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['SITE_URL'] = SITE_URL
        return context
