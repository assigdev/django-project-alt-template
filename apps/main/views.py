from django.views.generic import TemplateView, DetailView
from .models import Page


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get_home_page()
        return context


class PageDetailView(DetailView):
    model = Page

    def get_template_names(self):
        return self.object.get_template()
