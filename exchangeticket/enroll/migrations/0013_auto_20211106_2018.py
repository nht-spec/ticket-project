# Generated by Django 2.2 on 2021-11-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0012_auto_20211106_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
