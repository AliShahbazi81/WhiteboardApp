# Generated by Django 4.1.9 on 2023-07-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WhiteboardApp", "0006_alter_instructor_user_alter_student_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="instructor",
            name="biography",
        ),
        migrations.AlterField(
            model_name="instructor",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
