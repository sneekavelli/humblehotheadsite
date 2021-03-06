# Generated by Django 3.1 on 2020-09-28 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women'), ('kids', 'Kids')], default='men', max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
