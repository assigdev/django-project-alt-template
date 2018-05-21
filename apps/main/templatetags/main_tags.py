from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def is_url_active(context, url):
    if url == context['request'].path:
        return 'active'
    return ''


@register.filter(name='add_class')
def add_class(field, class_name):
    return field.as_widget(attrs={"class": class_name})
