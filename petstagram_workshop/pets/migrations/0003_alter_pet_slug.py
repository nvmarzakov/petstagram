# Generated by Django 4.2.3 on 2023-07-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
