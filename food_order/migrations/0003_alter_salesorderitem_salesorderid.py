# Generated by Django 4.0.2 on 2022-04-23 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0002_delivery_salesorderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorderitem',
            name='salesOrderId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesorder_salesorderitem', to='food_order.salesorder'),
        ),
    ]
