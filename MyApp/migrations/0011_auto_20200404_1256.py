# Generated by Django 3.0.4 on 2020-04-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_auto_20200401_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_seeker',
            name='u_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
