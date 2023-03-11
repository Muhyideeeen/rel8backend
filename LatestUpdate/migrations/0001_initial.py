# Generated by Django 3.2.13 on 2023-03-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LastestUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='latest_update/%d/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
