# Generated by Django 3.1 on 2020-10-11 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_orders_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ('-added',)},
        ),
    ]
