# Generated by Django 4.1.3 on 2023-02-15 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customer_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KhachHang',
        ),
    ]
