# Generated by Django 4.1.2 on 2023-03-26 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0004_alter_treemenuitem_parent_menu'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='treemenuitem',
            name='only_one_parent',
        ),
    ]
