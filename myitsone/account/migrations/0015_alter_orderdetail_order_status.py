# Generated by Django 4.2.4 on 2023-09-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_remove_orderitems_order_orderitems_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Completed', 'Completed')], max_length=254, null=True),
        ),
    ]
