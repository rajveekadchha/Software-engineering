# Generated by Django 3.0.4 on 2020-04-01 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_auto_20200331_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_provider',
            old_name='job_provider_company_id',
            new_name='job_provider_company',
        ),
    ]
