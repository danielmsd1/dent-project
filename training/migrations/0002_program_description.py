# Generated by Django 4.0.6 on 2022-07-22 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='description',
            field=models.TextField(default='A training program'),
        ),
    ]
