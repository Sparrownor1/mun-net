# Generated by Django 2.2.3 on 2019-08-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delegation', '0003_auto_20190808_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='delegate_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]