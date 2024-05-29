# Generated by Django 5.0.3 on 2024-04-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_remove_photoframe_discount"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhotoTour",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=100)),
                ("phoneno", models.CharField(max_length=200)),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
