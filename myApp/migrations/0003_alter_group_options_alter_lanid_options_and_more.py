# Generated by Django 4.1.7 on 2023-04-12 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_lanid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'bp_group'},
        ),
        migrations.AlterModelOptions(
            name='lanid',
            options={'verbose_name': 'bp_lanid'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'bp_user'},
        ),
    ]
