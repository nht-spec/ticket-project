# Generated by Django 2.2 on 2021-12-05 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0034_auto_20211205_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.AddField(
            model_name='emailuser',
            name='userEmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.Ticket'),
        ),
    ]
