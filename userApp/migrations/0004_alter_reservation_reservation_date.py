# Generated by Django 5.1.5 on 2025-02-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0003_alter_reservation_reservation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="reservation_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
