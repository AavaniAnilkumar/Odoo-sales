# Generated by Django 4.0.4 on 2024-01-31 11:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_saleorder_saleorderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleorder',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='pricelist',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='quotation_template',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='recurring_plan',
        ),
        migrations.AddField(
            model_name='saleorder',
            name='custom_id',
            field=models.CharField(default=datetime.datetime(2024, 1, 31, 11, 28, 31, 561115, tzinfo=utc), editable=False, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SaleOrderItem',
        ),
    ]