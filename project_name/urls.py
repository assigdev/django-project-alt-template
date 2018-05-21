"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from {{ project_name }} import settings
from django.conf.urls.static import static
from {{ project_name }}.sitemap import StaticSitemap, PageSitemap, HtmlMapView, RobotsView
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static':   StaticSitemap,
    'pages': PageSitemap,
}

seo_urlpatterns = [
    path('robots.txt', RobotsView.as_view()),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('sitemap.html', HtmlMapView.as_view(), name="html_map"),
]


apps_urlpatterns = [
    path('', include('apps.main.urls', namespace="main")),

]

third_apps_urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = seo_urlpatterns + apps_urlpatterns + third_apps_urlpatterns

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
