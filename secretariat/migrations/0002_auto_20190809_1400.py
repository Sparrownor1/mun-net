# Generated by Django 2.2.3 on 2019-08-09 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progresssheet',
            name='committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delegation.Committee', unique=True),
        ),
    ]
