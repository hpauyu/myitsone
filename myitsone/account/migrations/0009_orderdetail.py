# Generated by Django 4.2.4 on 2023-09-03 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_orderitems_order_delete_orderdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.CharField(default='A1000000001', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField()),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=254, null=True)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Delivering', 'Delivering'), ('Delivered', 'Delivered')], max_length=254, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, max_length=254, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('user_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.useraddress')),
                ('user_payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userpayment')),
            ],
        ),
    ]
