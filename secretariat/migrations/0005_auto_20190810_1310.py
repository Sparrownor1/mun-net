# Generated by Django 2.2.3 on 2019-08-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0004_logisticsrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logisticsrequest',
            name='author',
        ),
        migrations.AddField(
            model_name='logisticsrequest',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
