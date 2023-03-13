# Generated by Django 3.2.13 on 2023-03-12 15:40

import cloudinary_storage.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationOfDeactivatedMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_most_recent_audited_financial_statement', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='submit_most_recent_audited_financial_statement/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='UpdateOnProductsManufactured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('most_recent_financial_statement', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='most_recent_financial_statement/%d/')),
                ('product_update_inspection_report', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='product_update_inspection_report/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='MergerOfMemberCompanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_requesting_merger_of_companies', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='letter_requesting_merger_of_companies/%d/')),
                ('most_recent_audited_finicial_statement', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='most_recent_audited_finicial_statement/%d/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('approved', 'Approved'), ('disapprove', 'Disapprove')], default='pending', max_length=300)),
                ('member', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.memeber')),
            ],
        ),
        migrations.CreateModel(
            name='LossOfCertificateServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affidavit_from_court_of_loss_of_cert', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='affidavit_from_court_of_loss_of_cert/')),
                ('amount_to_be_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year_one_audited_finacial_statements', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='year_one_audited_finacial_statements/%d/')),
                ('year_two_audited_finacial_statements', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='year_one_audited_finacial_statements/%d/')),
                ('certificate_of_incorporation', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='certificate_of_incorporation/%d/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('approved', 'Approved'), ('disapprove', 'Disapprove')], default='pending', max_length=300)),
                ('member', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.memeber')),
            ],
        ),
        migrations.CreateModel(
            name='DeactivationOfMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_requesting_deactivation', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='letter_requesting_deactivation/%d/')),
                ('original_membership_certificate', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='original_membership_certificate/%d/')),
                ('member', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.memeber')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeOfName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_membership_certificate', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='original_membership_certificate/%d/')),
                ('amount_to_be_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year_one_audited_finacial_statements', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='year_one_audited_finacial_statements/%d/')),
                ('year_two_audited_finacial_statements', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='year_one_audited_finacial_statements/%d/')),
                ('certificate_of_incorporation', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='certificate_of_incorporation/%d/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('approved', 'Approved'), ('disapprove', 'Disapprove')], default='pending', max_length=300)),
                ('member', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.memeber')),
            ],
        ),
        migrations.CreateModel(
            name='AllMembershipCertificatesAboutConcernedCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_certificates', models.TextField()),
                ('document', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='all_membership_certificates_about_concerned_company/%d/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('approved', 'Approved'), ('disapprove', 'Disapprove')], default='pending', max_length=300)),
                ('merger_of_member_companies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.mergerofmembercompanies')),
            ],
        ),
    ]
