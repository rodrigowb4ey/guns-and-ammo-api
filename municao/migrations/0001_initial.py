# Generated by Django 4.0.4 on 2022-05-12 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("utils", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Municao",
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
                ("marca", models.CharField(max_length=64)),
                ("modelo", models.CharField(max_length=64)),
                ("valor_estimado", models.FloatField()),
                (
                    "calibre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="utils.calibre",
                    ),
                ),
                (
                    "objeto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="utils.objeto",
                    ),
                ),
            ],
        ),
    ]
