# Generated by Django 4.1.3 on 2023-03-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment_status",
            name="username",
            field=models.CharField(max_length=20),
        ),
    ]
