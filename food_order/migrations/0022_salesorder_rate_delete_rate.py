# Generated by Django 4.0.2 on 2022-05-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0021_remove_rate_itemid_rate_orderid_delete_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='rate',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]