# Generated by Django 3.2.4 on 2021-08-04 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210804_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='main_news',
        ),
    ]
