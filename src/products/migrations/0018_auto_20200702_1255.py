# Generated by Django 2.2 on 2020-07-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(),
        ),
    ]