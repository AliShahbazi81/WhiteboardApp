# Generated by Django 4.1.10 on 2023-07-23 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WhiteboardApp', '0017_remove_student_verification_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='verification_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
