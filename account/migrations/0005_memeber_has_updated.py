# Generated by Django 3.2.13 on 2023-08-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_memeber_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='memeber',
            name='has_updated',
            field=models.BooleanField(default=False),
        ),
    ]
