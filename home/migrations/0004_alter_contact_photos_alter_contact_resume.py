# Generated by Django 5.0.2 on 2024-03-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_photos_alter_contact_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photos',
            field=models.FileField(null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='resume',
            field=models.FileField(null=True, upload_to='resumes/'),
        ),
    ]
