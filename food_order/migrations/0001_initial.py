# Generated by Django 3.1.3 on 2022-02-02 13:13

from django.db import migrations, models
import django.db.models.deletion
import food_order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('categoryId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_subcategory', to='food_order.category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
                ('isRawMaterial', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=2000)),
                ('image', models.FileField(blank=True, null=True, upload_to=food_order.models.item_picture_path)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_item', to='food_order.category')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentMethod', models.TextField()),
                ('createdDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phone', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('email', models.CharField(max_length=1000)),
                ('password', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('userType', models.CharField(max_length=20)),
                ('provider', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_client', serialize=False, to='food_order.user')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('district', models.TextField()),
                ('streetName', models.TextField()),
                ('building', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('apartment', models.IntegerField()),
                ('createdDate', models.DateTimeField()),
                ('purchaseOrderId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='purchaseorder_delivery', serialize=False, to='food_order.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryMan',
            fields=[
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_deliveryman', serialize=False, to='food_order.user')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_supplier', serialize=False, to='food_order.user')),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_rawmaterial', to='food_order.item')),
                ('rawMaterialItemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rawmaterialitem_rawmaterial', to='food_order.item')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_purchaseorderitem', to='food_order.item')),
                ('purchaseOrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseorder_purchaseorderitem', to='food_order.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('clientId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='client_shoppingCart', serialize=False, to='food_order.client')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField()),
                ('statusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_track', to='food_order.status')),
                ('deliveryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_track', to='food_order.delivery')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('createdDate', models.DateTimeField()),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_review', to='food_order.item')),
                ('clientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_review', to='food_order.client')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('createdDate', models.DateTimeField()),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_rate', to='food_order.item')),
                ('clientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_rate', to='food_order.client')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='clientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_purchaseorder', to='food_order.client'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='supplierId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_purchaseorder', to='food_order.supplier'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_favorite', to='food_order.item')),
                ('clientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_favorite', to='food_order.client')),
            ],
        ),
        migrations.AddField(
            model_name='delivery',
            name='deliveryManId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveryman_delivery', to='food_order.deliveryman'),
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_shoppingcartitem', to='food_order.item')),
                ('shoppingCartId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppingcart_shoppingcartitem', to='food_order.shoppingcart')),
            ],
        ),
    ]
