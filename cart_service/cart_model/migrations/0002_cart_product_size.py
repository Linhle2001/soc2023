# Generated by Django 4.1.3 on 2023-05-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_size',
            field=models.CharField(default='36', max_length=2),
        ),
    ]