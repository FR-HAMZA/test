# Generated by Django 4.1.5 on 2023-01-15 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0012_alter_package_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryman',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.city'),
        ),
    ]
