# Generated by Django 2.2 on 2021-12-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0031_ticket_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
