# Generated by Django 5.1.7 on 2025-03-18 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_remove_sale_product_remove_sale_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='products',
        ),
        migrations.AlterField(
            model_name='saleproduct',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_products', to='sales.sale'),
        ),
    ]
