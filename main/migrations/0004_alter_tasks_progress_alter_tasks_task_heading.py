# Generated by Django 5.0.1 on 2024-02-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_note_notes_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='progress',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_heading',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]