# Generated by Django 2.2.5 on 2019-10-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingroomlog',
            name='scheduled_time',
            field=models.CharField(default='', max_length=200),
        ),
    ]
