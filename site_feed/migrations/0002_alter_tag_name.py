# Generated by Django 3.2.3 on 2021-05-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name'),
        ),
    ]
