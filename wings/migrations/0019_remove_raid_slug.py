# Generated by Django 3.2.9 on 2021-12-31 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wings', '0018_auto_20211231_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raid',
            name='slug',
        ),
    ]
