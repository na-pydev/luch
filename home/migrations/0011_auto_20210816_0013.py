# Generated by Django 3.1.5 on 2021-08-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_newsletter_main_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
