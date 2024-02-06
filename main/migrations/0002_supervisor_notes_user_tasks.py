# Generated by Django 5.0.1 on 2024-02-04 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('super_id', models.CharField(max_length=10, unique=True)),
                ('Name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note', models.CharField(max_length=200)),
                ('Timestamp', models.DateTimeField()),
                ('super_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.CharField(max_length=10, unique=True)),
                ('Name', models.CharField(max_length=20)),
                ('Projectname', models.CharField(max_length=20)),
                ('super_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=5, unique=True)),
                ('Deadline', models.DateField()),
                ('Task_heading', models.CharField(max_length=20, unique=True)),
                ('Task_details', models.CharField(max_length=250)),
                ('Progress', models.DecimalField(decimal_places=1, max_digits=4)),
                ('Timestamp', models.DateTimeField()),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]