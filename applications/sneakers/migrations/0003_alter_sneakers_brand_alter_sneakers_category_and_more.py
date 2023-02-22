# Generated by Django 4.1.7 on 2023-02-21 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('category', '0001_initial'),
        ('sneakers', '0002_alter_sneakers_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakers',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sneakers', to='brand.brand'),
        ),
        migrations.AlterField(
            model_name='sneakers',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sneakers', to='category.category'),
        ),
        migrations.AlterField(
            model_name='sneakers',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название кроссовки'),
        ),
        migrations.AlterField(
            model_name='sneakersimage',
            name='image',
            field=models.ImageField(upload_to='sneakers_images'),
        ),
        migrations.AlterField(
            model_name='sneakersimage',
            name='sneaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sneakers', to='sneakers.sneakers'),
        ),
    ]
