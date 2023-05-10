# Generated by Django 4.1.7 on 2023-03-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=200)),
                ('product_id', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=5)),
                ('payment_status', models.CharField(max_length=15)),
                ('transaction_id', models.CharField(max_length=5)),
                ('shipment_status', models.CharField(max_length=20)),
            ],
        ),
    ]
