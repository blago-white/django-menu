from django.shortcuts import render
from .models import TreeMenu
from .highlighted import highlighted_items


def menu(request, slug: str):
    return render(request=request, template_name='tree_menu/menu_page.html', context={'slug': slug})


def home(request):
    menues = TreeMenu.objects.all()
    menues = [(item.title, item.slug, True if item.slug in highlighted_items else False) for item in menues]

    return render(request=request, template_name='tree_menu/home.html', context={'menues': menues})
