# Generated by Django 3.1.7 on 2021-05-04 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DJ_App', '0002_meminfolist_id2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meminfolist',
            name='id2',
        ),
    ]
