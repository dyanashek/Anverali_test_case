from django import template

register = template.Library()

@register.filter 
def addclass(field, css):
    return field.as_widget(attrs={'class': css})

@register.filter 
def list_unpack(value: list):
    return ', '.join(eval(value))