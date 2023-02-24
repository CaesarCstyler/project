# Generated by Django 4.1.7 on 2023-02-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Sneakers',
            new_name='sneakers',
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]