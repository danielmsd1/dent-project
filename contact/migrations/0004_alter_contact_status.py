# Generated by Django 4.0.6 on 2022-07-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
