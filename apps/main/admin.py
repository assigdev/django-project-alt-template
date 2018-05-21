from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sort', 'template')
    list_editable = ('sort', 'template')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'sort', 'template', 'content')
        }),
        ('SEO', {
            'classes': ('collapse',),
            'fields': ('meta_keywords', 'meta_description', 'meta_tags', 'scripts'),
        }),
    )

