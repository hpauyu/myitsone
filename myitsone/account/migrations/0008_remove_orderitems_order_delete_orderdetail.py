# Generated by Django 4.2.4 on 2023-09-03 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_orderitems_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='order',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]
