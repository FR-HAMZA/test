# Generated by Django 4.1.5 on 2023-01-11 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0010_rename_packageid_package_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='assigned_to_deliveryman',
        ),
    ]
