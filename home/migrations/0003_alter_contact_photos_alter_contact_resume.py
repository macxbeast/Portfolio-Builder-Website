# Generated by Django 5.0.2 on 2024-03-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_experience_contact_photos_contact_projects_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photos',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]