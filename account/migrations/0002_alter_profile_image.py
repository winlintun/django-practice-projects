# Generated by Django 5.0.1 on 2024-01-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, default="default.webp", null=True, upload_to="img/profiles"
            ),
        ),
    ]
