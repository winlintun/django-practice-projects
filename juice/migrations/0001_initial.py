# Generated by Django 5.0.1 on 2024-01-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Juice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="juices/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_ordered", models.DateTimeField(auto_now_add=True)),
                ("juices", models.ManyToManyField(to="juice.juice")),
            ],
        ),
    ]
