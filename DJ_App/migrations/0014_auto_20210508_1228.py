# Generated by Django 3.1.7 on 2021-05-08 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJ_App', '0013_auto_20210506_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('TextContent', models.CharField(max_length=10000)),
                ('writername', models.CharField(max_length=20)),
                ('writedate', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='meminfolist',
            name='expText',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
