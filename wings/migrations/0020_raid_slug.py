# Generated by Django 3.2.9 on 2021-12-31 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wings', '0019_remove_raid_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='raid',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
