# Generated by Django 4.0.2 on 2022-05-01 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0016_alter_item_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=30)),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_recipy', to='food_order.item')),
            ],
        ),
    ]