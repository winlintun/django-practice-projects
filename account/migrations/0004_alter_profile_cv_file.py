# Generated by Django 5.0.1 on 2024-01-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_profile_cv_file_profile_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="cv_file",
            field=models.FileField(blank=True, null=True, upload_to="cv-files/"),
        ),
    ]
