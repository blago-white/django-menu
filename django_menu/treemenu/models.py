from django.db import models


class TreeMenu(models.Model):
    title = models.CharField('title', max_length=120, null=False, blank=True)
    slug = models.CharField('slug', max_length=120, unique=True, null=False, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'


class TreeMenuItem(models.Model):
    title = models.CharField('title', max_length=255, blank=True, null=False)
    category = models.ForeignKey(
        TreeMenu,
        to_field='slug',
        verbose_name='Category',
        blank=False,
        null=False)

    path = models.CharField('path', max_length=1000, blank=True, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menue Items'
