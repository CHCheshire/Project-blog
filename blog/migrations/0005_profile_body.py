# Generated by Django 3.2.15 on 2022-10-05 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20221005_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='body',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]