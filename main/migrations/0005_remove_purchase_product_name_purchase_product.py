# Generated by Django 5.1.1 on 2024-09-25 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='product_name',
        ),
        migrations.AddField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
            preserve_default=False,
        ),
    ]
