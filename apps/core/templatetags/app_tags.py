from django import template

register = template.Library()


@register.simple_tag
def equals(arg, comparator):
    return arg == comparator
