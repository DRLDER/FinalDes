# Generated by Django 3.1.7 on 2021-05-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJ_App', '0010_auto_20210505_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comecilist',
            name='ProjectClass',
            field=models.CharField(default='其它项目', max_length=50),
        ),
        migrations.AlterField(
            model_name='comecolist',
            name='ProjectClass',
            field=models.CharField(default='其它项目', max_length=50),
        ),
    ]
