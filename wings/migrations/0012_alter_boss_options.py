# Generated by Django 3.2.9 on 2021-12-27 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wings', '0011_boss_raid_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boss',
            options={'ordering': ['id'], 'verbose_name_plural': 'Bosses'},
        ),
    ]
