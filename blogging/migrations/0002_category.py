# Generated by Django 4.2.6 on 2023-10-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogging", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True)),
                (
                    "posts",
                    models.ManyToManyField(
                        blank=True, related_name="categories", to="blogging.post"
                    ),
                ),
            ],
        ),
    ]
