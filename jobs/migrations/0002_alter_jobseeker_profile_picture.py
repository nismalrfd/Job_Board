# Generated by Django 4.1.3 on 2023-11-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='profile_picture',
            field=models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='job_seeker_profile_pics/'),
        ),
    ]
