# Generated by Django 3.2.15 on 2022-10-06 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='body',
            new_name='bio',
        ),
    ]