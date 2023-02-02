# Generated by Django 4.0.6 on 2022-08-19 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DailySummary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("date", models.DateField(unique=True)),
                ("summary", models.JSONField()),
            ],
            options={
                "verbose_name_plural": "daily summaries",
            },
        ),
        migrations.CreateModel(
            name="System",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("system_id", models.UUIDField()),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="OnlineWorkers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("processes", models.IntegerField()),
                ("hosts", models.IntegerField()),
                (
                    "system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pulpanalytics.system"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "online workers",
            },
        ),
        migrations.CreateModel(
            name="OnlineContentApps",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("processes", models.IntegerField()),
                ("hosts", models.IntegerField()),
                (
                    "system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pulpanalytics.system"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "online content apps",
            },
        ),
        migrations.CreateModel(
            name="Component",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.TextField()),
                ("version", models.TextField()),
                (
                    "system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pulpanalytics.system"
                    ),
                ),
            ],
        ),
    ]
