# Generated by Django 4.0.4 on 2024-03-08 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_orderproduct_saleorder_orderproduct_sale_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleorder',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='products',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
        migrations.DeleteModel(
            name='SaleOrder',
        ),
    ]