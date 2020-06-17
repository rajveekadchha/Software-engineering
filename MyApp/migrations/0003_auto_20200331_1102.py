# Generated by Django 3.0.4 on 2020-03-31 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_auto_20200330_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_provider',
            name='job_provider_id',
        ),
        migrations.RemoveField(
            model_name='job_provider',
            name='job_provider_uid_number',
        ),
        migrations.RemoveField(
            model_name='job_provider',
            name='job_provider_uid_type',
        ),
        migrations.AlterField(
            model_name='job_provider',
            name='company_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, primary_key=True, serialize=False, to='MyApp.company'),
        ),
    ]
