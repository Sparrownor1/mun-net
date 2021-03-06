# Generated by Django 2.2.3 on 2019-08-16 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delegation', '0004_auto_20190814_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('delegate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='delegation.Delegate')),
            ],
        ),
    ]
