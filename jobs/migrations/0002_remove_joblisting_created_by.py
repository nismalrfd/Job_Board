# Generated by Django 4.1.3 on 2023-10-25 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblisting',
            name='created_by',
        ),
    ]