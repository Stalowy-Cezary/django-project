# Generated by Django 3.2.9 on 2021-12-27 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wings', '0010_auto_20211227_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='raid_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wings.raid'),
        ),
    ]
