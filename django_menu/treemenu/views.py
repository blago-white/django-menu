from django.shortcuts import render
from .models import TreeMenu

# Create your views here.


def base(request, slug):
    return render(request, 'menu/items.html', {'slug': slug})


def home(request):
    menues = TreeMenu.objects.select_related()
    menues = [(item.title, item.slug) for item in menues]

    return render(request, 'menu/home.html', {'menues': menues})
