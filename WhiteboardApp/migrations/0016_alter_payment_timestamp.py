# Generated by Django 4.1.9 on 2023-07-25 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("WhiteboardApp", "0015_alter_membership_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
