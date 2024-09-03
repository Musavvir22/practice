# Generated by Django 5.0.3 on 2024-08-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicanted_id', models.IntegerField()),
                ('degree', models.CharField(max_length=100)),
                ('fiedl_of_specialization', models.CharField(max_length=200)),
                ('institute_name', models.CharField(max_length=200)),
                ('date_of_completion', models.DateField(default=True)),
            ],
        ),
    ]
