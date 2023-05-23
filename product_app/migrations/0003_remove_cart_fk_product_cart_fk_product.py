# Generated by Django 4.1.7 on 2023-05-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_alter_orderitem_fk_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='fk_product',
        ),
        migrations.AddField(
            model_name='cart',
            name='fk_product',
            field=models.ManyToManyField(to='product_app.product'),
        ),
    ]