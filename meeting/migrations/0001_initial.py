# Generated by Django 3.2.13 on 2023-02-03 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('details', models.TextField(default='..')),
                ('date_for', models.DateTimeField(default=None, null=True)),
                ('addresse', models.TextField(default='')),
                ('event_date', models.DateTimeField(default=None, null=True)),
                ('organiserName', models.CharField(default='', max_length=400)),
                ('organiserDetails', models.CharField(default='', max_length=400)),
                ('chapters', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.chapters')),
                ('exco', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.excorole')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingReshedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_reschedule_date', models.DateTimeField(default=None, null=True)),
                ('meeting', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='meeting.meeting')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.memeber')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingAttendies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='meeting.meeting')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.memeber')),
            ],
        ),
    ]
