from django import template
register = template.Library()


@register.filter('fieldtype')
def fieldtype(field):
    return field.field.widget.input_type
