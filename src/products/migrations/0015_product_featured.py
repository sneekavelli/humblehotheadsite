# Generated by Django 2.2 on 2020-06-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]