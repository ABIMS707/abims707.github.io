# Generated by Django 3.1.5 on 2021-02-01 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carops', '0010_auto_20210201_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='first_name',
        ),
    ]
