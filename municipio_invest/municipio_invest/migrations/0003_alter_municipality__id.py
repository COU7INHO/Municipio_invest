# Generated by Django 5.1.3 on 2024-11-20 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipio_invest', '0002_alter_municipality__id_alter_municipality_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='_id',
            field=models.SmallIntegerField(unique=True),
        ),
    ]