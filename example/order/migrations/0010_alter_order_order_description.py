# Generated by Django 4.0.1 on 2022-01-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_remove_order_cart_order_total_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_description',
            field=models.TextField(default='', null=True),
        ),
    ]
