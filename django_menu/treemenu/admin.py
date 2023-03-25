from django.contrib import admin
from .models import TreeMenu, TreeMenuItem

admin.site.register(TreeMenu)
admin.site.register(TreeMenuItem)


# @admin.register(Menu)
# class MenuAdmin(admin.ModelAdmin):
#     fields = ['title', 'slug']
#     list_display = ['__str__', ]
#
#
# @admin.register(MenuItem)
# class MenuItemAdmin(admin.ModelAdmin):
#
#     fields = ['title', 'category', 'path']
#     list_display = ['__str__', 'category', 'path']
#
#     # filter_horizontal = ['category__name', ]

