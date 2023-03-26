from importlib.util import find_spec

from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tree_menu.urls')),
]
