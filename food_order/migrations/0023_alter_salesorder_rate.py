# Generated by Django 4.0.2 on 2022-05-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0022_salesorder_rate_delete_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='rate',
            field=models.IntegerField(default=0, null=True),
        ),
    ]