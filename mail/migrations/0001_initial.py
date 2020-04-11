# Generated by Django 3.0.4 on 2020-04-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('other_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('department_select', models.CharField(max_length=100)),
                ('pno', models.CharField(max_length=8)),
                ('phone_no', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('department_hod_last_name', models.CharField(max_length=100)),
                ('department_hod_first_name', models.CharField(max_length=100)),
                ('department_hod_other_name', models.CharField(max_length=100)),
                ('department_hod_email', models.EmailField(max_length=254)),
            ],
        ),
    ]