# Generated by Django 4.2 on 2023-05-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0031_remove_product_pamount1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pPrice',
            field=models.DecimalField(decimal_places=2, default=9.99, max_digits=5),
        ),
    ]