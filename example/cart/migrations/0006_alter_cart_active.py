# Generated by Django 4.0.1 on 2022-01-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cart_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
