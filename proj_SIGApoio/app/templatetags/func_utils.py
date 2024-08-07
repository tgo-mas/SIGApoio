from django import template

register = template.Library()

@register.filter(name="to_int")
def to_int(value):
    return int(value)

@register.filter(name="to_str")
def to_str(value):
    return str(value)


