# Generated by Django 2.1.5 on 2019-02-10 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usersmodel_f_auth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersmodel',
            name='department',
        ),
    ]
