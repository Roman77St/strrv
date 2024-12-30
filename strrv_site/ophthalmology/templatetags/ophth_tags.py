from django import template
from django.utils.safestring import mark_safe

import markdown
from markdown.extensions.tables import TableExtension

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text, extensions=['tables']))

