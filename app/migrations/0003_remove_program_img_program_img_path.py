# Generated by Django 4.2.16 on 2025-04-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_program_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='img',
        ),
        migrations.AddField(
            model_name='program',
            name='img_path',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
