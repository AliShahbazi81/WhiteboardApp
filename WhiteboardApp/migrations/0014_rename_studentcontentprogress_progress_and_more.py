# Generated by Django 4.1.9 on 2023-07-16 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("WhiteboardApp", "0013_remove_enrollment_is_completed_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="StudentContentProgress",
            new_name="Progress",
        ),
        migrations.AlterModelOptions(
            name="progress",
            options={"verbose_name": "progress"},
        ),
        migrations.AlterModelTable(
            name="progress",
            table="WhiteboardApp_progress",
        )
    ]
