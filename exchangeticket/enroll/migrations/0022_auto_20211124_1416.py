# Generated by Django 2.2 on 2021-11-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0021_auto_20211124_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
