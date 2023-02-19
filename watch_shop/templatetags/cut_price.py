from django import template

register = template.Library()


def cut_price(value):
    return '{0:,}'.format(value).replace(',', ' ')


register.filter('cut_price', cut_price)
