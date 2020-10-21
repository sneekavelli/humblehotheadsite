from django.template import Library

register = Library()

@register.filter(name='get_val')
def get_val(arg,val):
    return arg[val]
