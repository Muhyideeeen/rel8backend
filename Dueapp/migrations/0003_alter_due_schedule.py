# Generated by Django 3.2.13 on 2023-04-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dueapp', '0002_auto_20230415_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='due',
            name='schedule',
            field=models.JSONField(default=None, null=True),
        ),
    ]
