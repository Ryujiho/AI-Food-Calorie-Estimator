# Generated by Django 4.1.1 on 2022-09-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("counter", "0002_remove_foodies_calories_foodies_serving_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="foodies", name="calories", field=models.IntegerField(default=0),
        ),
    ]
