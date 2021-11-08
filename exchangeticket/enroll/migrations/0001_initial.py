# Generated by Django 2.2 on 2021-11-06 04:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('quality', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('time_pub', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
