# Generated by Django 3.2.13 on 2023-10-31 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_memeber_has_updated'),
        ('Dueapp', '0005_due_item_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='due',
            name='exco',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.excorole'),
        ),
    ]
