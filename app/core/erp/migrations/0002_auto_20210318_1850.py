# Generated by Django 3.1.6 on 2021-03-19 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de venta'),
        ),
    ]
