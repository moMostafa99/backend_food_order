# Generated by Django 4.0.2 on 2022-04-28 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0007_adminuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categoryId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_subcategory', to='food_order.category'),
        ),
    ]
