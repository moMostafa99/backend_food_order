# Generated by Django 4.0.2 on 2022-04-28 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0010_alter_category_categoryid_alter_item_categoryid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categoryId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_subcategory', to='food_order.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='categoryId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_item', to='food_order.category'),
        ),
    ]
