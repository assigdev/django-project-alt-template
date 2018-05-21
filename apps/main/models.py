from django.db import models


TEMPLATES = (
    ('default.html', 'default'),
    ('home.html', 'home'),
)


class PageManager(models.Manager):
    def get_home_page(self):
        try:
            return super().get(slug='home')
        except models.ObjectDoesNotExist:
            return None


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    sort = models.SmallIntegerField(default=1)
    template = models.CharField(max_length=100, choices=TEMPLATES)
    content = models.TextField(max_length=10000, blank=True)
    meta_keywords = models.CharField( max_length=100, blank=True)
    meta_description = models.TextField(max_length=400, blank=True)
    meta_tags = models.TextField(max_length=400, blank=True)
    scripts = models.TextField(max_length=500, blank=True)

    objects = PageManager

    class Meta:
        ordering = ['sort', 'id']

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'main:page', (self.slug,)

    def get_template(self):
        return 'main/%s' % self.template
