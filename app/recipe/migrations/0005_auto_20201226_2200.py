# Generated by Django 3.1.4 on 2020-12-26 22:00

from django.db import migrations, models
import recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=recipe.models.recipe_image_file_path),
        ),
    ]
