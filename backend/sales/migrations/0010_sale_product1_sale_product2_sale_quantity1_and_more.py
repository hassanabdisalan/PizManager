# Generated by Django 5.1.7 on 2025-03-18 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_price_product_buying_price_and_more'),
        ('sales', '0009_remove_sale_product1_remove_sale_product2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='product1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product1', to='inventory.product'),
        ),
        migrations.AddField(
            model_name='sale',
            name='product2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product2', to='inventory.product'),
        ),
        migrations.AddField(
            model_name='sale',
            name='quantity1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='quantity2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='selling_price1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='selling_price2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='total_price1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='total_price2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
