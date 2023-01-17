# Generated by Django 4.1.5 on 2023-01-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_rename_category_city_alter_city_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('city', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Deliverymen',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_id', models.CharField(max_length=255)),
                ('city', models.IntegerField()),
                ('assigned_to_deliveryman', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'packages',
            },
        ),
    ]
