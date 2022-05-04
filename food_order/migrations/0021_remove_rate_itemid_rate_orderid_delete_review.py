# Generated by Django 4.0.2 on 2022-05-03 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0020_remove_rate_createddate_alter_rate_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='itemId',
        ),
        migrations.AddField(
            model_name='rate',
            name='orderId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_rate', to='food_order.salesorder'),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
