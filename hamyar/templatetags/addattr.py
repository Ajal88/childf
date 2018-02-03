from django import template

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='addvalue')
def addvalue(field, value):
    return field.as_widget(attrs={"value": value})
