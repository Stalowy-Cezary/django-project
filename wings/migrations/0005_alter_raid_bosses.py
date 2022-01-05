# Generated by Django 3.2.9 on 2021-12-27 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wings', '0004_alter_raid_bosses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raid',
            name='bosses',
            field=models.OneToOneField(default='Vale Guardian', on_delete=django.db.models.deletion.CASCADE, to='wings.boss'),
        ),
    ]
