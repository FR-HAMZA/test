# Generated by Django 4.1.5 on 2023-01-10 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_book_category_grocery_delete_city_delete_client_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Grocery',
        ),
    ]