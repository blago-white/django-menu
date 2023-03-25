import re

from django import template
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch

from ..models import TreeMenuItem

register = template.Library()


@register.inclusion_tag('menu/base.html', takes_context=True)
def draw_menu(context: RequestContext, slug: str = ''):
    """
    :param slug:
    :param context:
    :type context: RequestContext
    :return:
    """
    is_url = re.compile(r'^http[s]?://')

    print('_________slug ', slug)

    data = TreeMenuItem.objects.select_related().filter(category=slug)
    menu = []
    for idx, item in enumerate(data):
        path = item.path.strip()
        target = '_self'

        if is_url.match(path):
            url = path
            target = '_blank'

        else:
            try:
                url = reverse(path)
            except NoReverseMatch:
                url = path

        menu.append({
            'id': item.pk,
            'url': url,
            'target': target,
            'name': item.title,
            'parent': slug,
        })

    return {
        'menu': menu,
    }
