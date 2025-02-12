# Generated by Django 5.0.6 on 2024-07-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0005_alter_sociallink_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("comment", models.TextField(max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
