# Generated by Django 4.0 on 2022-01-05 08:42

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_image_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
