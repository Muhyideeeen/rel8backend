# Generated by Django 3.2.13 on 2023-06-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='manifesto_text',
            field=models.TextField(default='Let Make Record'),
        ),
    ]
