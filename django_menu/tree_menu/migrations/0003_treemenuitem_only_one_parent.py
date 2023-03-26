# Generated by Django 4.1.2 on 2023-03-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0002_alter_treemenuitem_parent_sub_menu'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='treemenuitem',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('parent_menu__isnull', False), ('parent_sub_menu__isnull', True)), models.Q(('parent_menu__isnull', True), ('parent_sub_menu__isnull', False)), _connector='OR'), name='only_one_parent'),
        ),
    ]