# Generated by Django 5.0.4 on 2024-05-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.CharField(max_length=100),
        ),
    ]
