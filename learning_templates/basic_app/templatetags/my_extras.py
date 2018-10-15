from django import template

register = template.Library()


@register.filter(name='cutto')
def cut(value, arg):
    """
    Cut out all the values of  "arg" from the string
    """

    return value.replace(arg,'')

# register.filter('cutto', cut)