# Generated by Django 3.1.1 on 2020-10-02 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='year',
        ),
    ]
