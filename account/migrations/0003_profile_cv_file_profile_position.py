# Generated by Django 5.0.1 on 2024-01-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="cv_file",
            field=models.FileField(blank=True, null=True, upload_to="None/cv"),
        ),
        migrations.AddField(
            model_name="profile",
            name="position",
            field=models.CharField(
                blank=True,
                help_text="I am Backend Developer",
                max_length=255,
                null=True,
            ),
        ),
    ]
