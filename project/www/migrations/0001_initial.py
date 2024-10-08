# Generated by Django 4.1 on 2024-08-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kierunek",
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
                ("nazwa", models.CharField(max_length=250)),
                ("utworzono", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Wydzial",
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
                ("nazwa", models.CharField(max_length=200)),
                ("logo", models.ImageField(upload_to="images")),
                ("utworzono", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("imie", models.CharField(max_length=100)),
                ("nazwisko", models.CharField(max_length=100)),
                ("nr_albumu", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=150)),
                ("zdjecie", models.ImageField(upload_to="images")),
                ("utworzono", models.DateTimeField(auto_now_add=True)),
                ("kierunki", models.ManyToManyField(to="www.kierunek")),
            ],
        ),
        migrations.AddField(
            model_name="kierunek",
            name="wydzialy",
            field=models.ManyToManyField(to="www.wydzial"),
        ),
    ]
