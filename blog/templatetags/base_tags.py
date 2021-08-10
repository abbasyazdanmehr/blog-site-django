from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "بهترین مقالات"


@register.inclusion_tag("blog/partials/category_nav.html")
def category_nav():
    return {
        "categories": Category.objects.filter(status=True)
    }
    