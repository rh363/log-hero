# Generated by Django 4.2.13 on 2024-11-29 11:10

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loghero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='extra_data',
            field=models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
    ]