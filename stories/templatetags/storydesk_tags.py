from django import template
from datetime import date

register = template.Library()


@register.simple_tag
def current_year():
    return date.today().year


@register.filter
def status_label(value):
    labels = {
        "draft": "Чернова",
        "in_progress": "В процес",
        "published": "Публикувана",
    }
    return labels.get(value, value)
