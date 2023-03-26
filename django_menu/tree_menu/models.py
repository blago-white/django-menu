from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError


class TreeMenu(models.Model):
    title = models.CharField('title', max_length=120, null=False)
    slug = models.CharField('slug', max_length=120, unique=True, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'


class TreeMenuItem(models.Model):
    title = models.CharField('title', max_length=255, null=False)
    slug = models.CharField('slug', max_length=120, unique=True, null=False)
    parent_menu = models.ForeignKey(to=TreeMenu,
                                    to_field='slug',
                                    verbose_name='Parent menu',
                                    null=True,
                                    blank=True,
                                    on_delete=models.DO_NOTHING)

    parent_sub_menu = models.ForeignKey(to='self',
                                        to_field='slug',
                                        verbose_name='Parent sub-menu',
                                        null=True,
                                        blank=True,
                                        on_delete=models.DO_NOTHING)

    def clean(self):
        if self.parent_menu and self.parent_sub_menu:
            raise ValidationError("You can specify only one parent")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menue Items'
