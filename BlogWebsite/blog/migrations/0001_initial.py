# Generated by Django 5.0 on 2023-12-07 23:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("ID", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("ID", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("content", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=255)),
                ("date_published", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Usern",
            fields=[
                ("ID", models.IntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("ID", models.IntegerField(primary_key=True, serialize=False)),
                ("content", models.CharField(max_length=255)),
                ("date_posted", models.DateField(null=True)),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.post"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.usern"
                    ),
                ),
            ],
        ),
    ]
