# Generated by Django 3.0.6 on 2020-05-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(max_length=30),
        ),
    ]
