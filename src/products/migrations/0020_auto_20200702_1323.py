# Generated by Django 2.2 on 2020-07-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200702_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(verbose_name='abc'),
        ),
    ]
