# Generated by Django 3.2.9 on 2021-12-31 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wings', '0022_alter_raid_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raid',
            name='slug',
            field=models.SlugField(),
        ),
    ]
