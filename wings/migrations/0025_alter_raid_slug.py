# Generated by Django 3.2.9 on 2021-12-31 17:14

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wings', '0024_alter_raid_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raid',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]
