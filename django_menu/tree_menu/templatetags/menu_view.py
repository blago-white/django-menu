import re

from django import template
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch
from ..models import TreeMenuItem
from django.db.models import Q
from ..highlighted import highlighted_items

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def draw_menu(slug: str):
    menu_items = TreeMenuItem.objects.select_related().filter(Q(parent_menu=slug) | Q(parent_sub_menu=slug))
    menu_items = [{'title': i.title,
                   'href': i.slug or '',
                   'highlight': True if i.slug in highlighted_items else False}
                  for i in menu_items]

    return {'menu': menu_items}
