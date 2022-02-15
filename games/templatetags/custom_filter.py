from django import template

register = template.Library()


@register.filter()
def my_filter(likes, id):
    exists = likes.filter(id=id).exists()
    return exists
